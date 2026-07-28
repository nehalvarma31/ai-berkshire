import os
import glob
import re
import asyncio
from datetime import datetime
from typing import Optional
from dotenv import load_dotenv
import anthropic
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

load_dotenv()

ANTHROPIC_KEY = os.getenv("ANTHROPIC_API_KEY")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

client = anthropic.Anthropic(api_key=ANTHROPIC_KEY)

SYSTEM_PROMPT = """You are R-InvestIQ, an AI-powered value investing research assistant built by Nehal Varma Pericherla at Relanto, India.

You analyze companies using Warren Buffett's 6-gate framework:
1. Circle of Competence — Do I understand this business?
2. Good Business — Is it profitable with strong cash flow?
3. Moat — Does it have a durable competitive advantage?
4. Management — Can I trust the people running it?
5. Margin of Safety — Is the price low enough to buy safely?
6. Decision Discipline — Am I buying for the right reasons?

Traffic light verdict rules (apply strictly):
🟢 PASS  — Gates 1-4 all strong AND Gate 5 adequate margin of safety (price at least 25% below base case)
🟡 WATCH — Gates 1-4 strong BUT Gate 5 weak (good business, wrong price)
🔴 AVOID — Any of Gates 1-4 failed OR hard veto triggered

Always give a definitive verdict. Never hedge. Price discipline is absolute.
This is for research and education only. Not investment advice."""

REPORT_PROMPT_TEMPLATE = """Screen {company} using the Buffett 6-gate framework.

Write the verdict as clean Markdown, following this EXACT structure and style (headers, tables, bold) — this file gets rendered directly on a website, so the Markdown must be well-formed:

# R-InvestIQ Verdict Report

## {{Company Name}} ({{Ticker}}) · {{Exchange}} · {date}

---

## Verdict: {{🟢 PASS / 🟡 WATCH / 🔴 AVOID}}

**One-line reason:** {{single sentence — the SO WHAT, not just data}}

---

## Business Summary

| | |
|---|---|
| **What it does** | {{one sentence}} |
| **Moat** | {{one sentence}} |
| **10-year outlook** | {{one sentence}} |

---

## Gate Scorecard

| Gate | Score | Note |
|------|-------|------|
| 1 — Circle of Competence | {{★★★★☆}} | {{note}} |
| 2 — Good Business | {{★★★★★}} | {{note}} |
| 3 — Moat | {{★★★★☆}} | {{note}} |
| 4 — Management | {{★★★★☆}} | {{note}} |
| 5 — Margin of Safety | {{★★☆☆☆}} | {{note}} |
| 6 — Decision Discipline | {{Pass / Fail / Grey Zone}} | {{note}} |

---

## Key Financials

| Metric | Value | Metric | Value |
|--------|-------|--------|-------|
| Current Price | ${{price}} | P/E (TTM) | {{x}}x |
| Market Cap | ${{cap}} | FCF Yield | {{%}}% |
| Revenue | ${{rev}} | Gross Margin | {{%}}% |
| Net Income | ${{ni}} | ROE | {{%}}% |

---

## Valuation Range (three-scenario model)

| Scenario | Price Target | Assumptions |
|----------|-------------|-------------|
| 🟢 Bull | ${{bull}} | {{x}}% growth · {{x}}x P/E |
| 🟡 Base | ${{base}} | {{x}}% growth · {{x}}x P/E |
| 🔴 Bear | ${{bear}} | {{x}}% growth · {{x}}x P/E |

**Current price: ${{price}} · Margin of Safety: {{NONE/THIN/ADEQUATE/STRONG}}**

| | Price |
|--|-------|
| Watch price | ${{watch}} |
| Buy price | ${{buy}} |

---

## Top Risks

1. **{{Risk name}}:** {{specific risk}}
2. **{{Risk name}}:** {{specific risk}}

---

## ⚠️ Disclaimer

This report is produced by **R-InvestIQ**, a research and education tool built on the open-source AI-Berkshire framework (MIT License).

**This is NOT investment advice.** All data is sourced from public information and may contain errors or be out of date.

*R-InvestIQ · Nehal Varma Pericherla · Relanto · {date}*
*AI-Berkshire base by xbtlin · MIT License*

Use real, plausible current market data. Be specific, not generic. Fill in every {{placeholder}} — output ONLY the final Markdown, no preamble, no commentary before or after."""


def save_report(company: str, markdown_text: str) -> str:
    company_clean = company.strip().title()
    folder = f"reports/{company_clean}"
    os.makedirs(folder, exist_ok=True)
    date = datetime.now().strftime("%Y%m%d")
    path = f"{folder}/{company_clean}-verdict-{date}.md"
    with open(path, "w", encoding="utf-8") as f:
        f.write(markdown_text)
    return path


def find_existing_report(company: str) -> Optional[str]:
    company_clean = company.strip().title()
    ticker = company.strip().upper()
    for name in [company_clean, ticker, company.strip()]:
        files = glob.glob(f"reports/{name}/{name}-verdict-*.md")
        if files:
            with open(sorted(files)[-1], "r", encoding="utf-8") as f:
                return f.read()
    return None


def markdown_to_telegram_text(md: str) -> str:
    """Convert full Markdown into clean, readable plain text for Telegram chat."""
    lines = md.split("\n")
    out = []
    for raw in lines:
        line = raw.rstrip()
        stripped = line.strip()

        # Skip table separator rows like |---|---|
        if stripped.startswith("|") and set(stripped.replace("|", "").strip()) <= set("- "):
            continue

        # Table rows -> "Label: Value  |  Label: Value"
        if stripped.startswith("|"):
            cells = [c.strip() for c in stripped.split("|") if c.strip()]
            if cells:
                out.append("  " + "   ".join(cells))
            continue

        # Headers
        if stripped.startswith("# "):
            out.append(stripped[2:].upper())
            continue
        if stripped.startswith("## "):
            out.append("\n" + stripped[3:].upper())
            continue

        # Horizontal rules
        if stripped == "---":
            continue

        # Bold / italics -> strip markers, keep text
        clean = re.sub(r"\*\*(.+?)\*\*", r"\1", line)
        clean = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"\1", clean)
        out.append(clean)

    # Collapse 3+ blank lines into 1
    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


async def send_report(update: Update, text: str):
    """Send report in chunks, guaranteed."""
    chunk_size = 4000
    chunks = [text[i: i + chunk_size] for i in range(0, len(text), chunk_size)]
    print(f"[DEBUG] Sending {len(chunks)} chunk(s), total {len(text)} chars")
    for i, chunk in enumerate(chunks):
        try:
            await update.message.reply_text(chunk)
            print(f"[DEBUG] Sent chunk {i + 1}/{len(chunks)}")
            await asyncio.sleep(1)
        except Exception as e:
            print(f"[DEBUG] Error on chunk {i + 1}: {e}")
            await update.message.reply_text(f"[Error on part {i + 1}: {str(e)}]")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = (
        "🏦 R-InvestIQ — AI Value Investing Research\n"
        "Built by Nehal Varma Pericherla · Relanto\n\n"
        "Type any company name or ticker to get a Buffett-style verdict:\n\n"
        "  Apple · MSFT · Coca-Cola · TSLA\n\n"
        "Already screened:\n"
        "  🟡 Apple (AAPL)\n"
        "  🟡 Google (GOOGL)\n"
        "  🟡 Coca-Cola (KO)\n"
        "  🔴 Intel (INTC)\n\n"
        "Research and education only. Not investment advice."
    )
    await update.message.reply_text(msg)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Type any company name or ticker:\n\n"
        "Apple · GOOGL · Microsoft · TSLA · Berkshire\n\n"
        "I'll run a full Buffett-style analysis and return a "
        "PASS / WATCH / AVOID verdict. Takes 1-2 minutes."
    )


async def screen(update: Update, context: ContextTypes.DEFAULT_TYPE):
    company = update.message.text.strip()
    if not company:
        await update.message.reply_text("Please type a company name or ticker.")
        return

    status = await update.message.reply_text(
        f"Screening {company}... This takes 1-2 minutes."
    )

    # Check for existing saved report
    existing = find_existing_report(company)
    if existing:
        await status.edit_text(f"Found existing report for {company}")
        await send_report(update, markdown_to_telegram_text(existing))
        return

    # Call Claude API
    try:
        date_str = datetime.now().strftime("%Y-%m-%d")
        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=2000,
            system=SYSTEM_PROMPT,
            messages=[
                {
                    "role": "user",
                    "content": REPORT_PROMPT_TEMPLATE.format(company=company, date=date_str),
                }
            ],
        )

        print(f"[DEBUG] Stop reason: {response.stop_reason}")
        try:
            markdown_text = response.content[0].text
        except Exception as ex:
            print(f"[DEBUG] Direct access failed: {ex}")
            markdown_text = ""
        print(f"[DEBUG] Response: {len(markdown_text)} chars")

        if not markdown_text.strip():
            await status.edit_text("Error: Got empty response from AI.")
            return

        saved_path = save_report(company, markdown_text)
        await status.edit_text(f"Done — {company}\nSaved to {saved_path}")
        await send_report(update, markdown_to_telegram_text(markdown_text))

    except Exception as e:
        print(f"[DEBUG] Error: {e}")
        await status.edit_text(f"Error: {str(e)}")


def main():
    if not TELEGRAM_TOKEN:
        raise ValueError("TELEGRAM_BOT_TOKEN not set in .env")
    if not ANTHROPIC_KEY:
        raise ValueError("ANTHROPIC_API_KEY not set in .env")

    app = Application.builder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, screen))

    print("R-InvestIQ bot is running. Press Ctrl+C to stop.")
    app.run_polling()


if __name__ == "__main__":
    main()
