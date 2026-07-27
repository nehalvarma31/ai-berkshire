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


def save_report(company: str, text: str) -> str:
    company_clean = company.strip().title()
    folder = f"reports/{company_clean}"
    os.makedirs(folder, exist_ok=True)
    date = datetime.now().strftime("%Y%m%d")
    path = f"{folder}/{company_clean}-verdict-{date}.md"
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
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
        clean = re.sub(r"<[^>]+>", "", existing)
        await status.edit_text(f"Found existing report for {company}")
        await send_report(update, clean)
        return

    # Call Claude API
    try:
        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=2000,
            system=SYSTEM_PROMPT,
            messages=[
                {
                    "role": "user",
                    "content": (
                        f"Screen {company} using the Buffett 6-gate framework.\n\n"
                        "Write the verdict in plain text only. No markdown, no HTML, no tables.\n"
                        "Keep it under 3000 characters total.\n"
                        "Use this exact structure:\n\n"
                        "🏦 [COMPANY] ([TICKER]) · [EXCHANGE]\n\n"
                        "VERDICT: [🟢 PASS / 🟡 WATCH / 🔴 AVOID]\n"
                        "Reason: [one sentence — the SO WHAT]\n\n"
                        "── BUSINESS ──\n"
                        "What it does: [one sentence]\n"
                        "Moat: [one sentence]\n"
                        "10-yr outlook: [one sentence]\n\n"
                        "── GATE SCORECARD ──\n"
                        "1 Circle of Competence  [★★★★☆]  [note]\n"
                        "2 Good Business         [★★★★★]  [note]\n"
                        "3 Moat                  [★★★★☆]  [note]\n"
                        "4 Management            [★★★★☆]  [note]\n"
                        "5 Margin of Safety      [★★☆☆☆]  [note]\n"
                        "6 Decision Discipline   [Pass/Watch/Avoid]\n\n"
                        "── KEY FINANCIALS ──\n"
                        "Price: $X  |  P/E: Xx  |  Market Cap: $XB\n"
                        "Revenue: $XB  |  FCF: $XB  |  Gross Margin: X%\n"
                        "Net Income: $XB  |  ROE: X%\n\n"
                        "── VALUATION ──\n"
                        "Bull $X  (X% growth · Xx P/E)\n"
                        "Base $X  (X% growth · Xx P/E)\n"
                        "Bear $X  (X% growth · Xx P/E)\n"
                        "Current $X · MoS: [NONE/THIN/ADEQUATE/STRONG]\n"
                        "Watch price: $X  |  Buy price: $X\n\n"
                        "── TOP RISKS ──\n"
                        "1. [specific risk]\n"
                        "2. [specific risk]\n\n"
                        "⚠️ R-InvestIQ · Nehal Varma Pericherla · Relanto · Not investment advice."
                    ),
                }
            ],
        )

        print(f"[DEBUG] Stop reason: {response.stop_reason}")
        print(f"[DEBUG] Raw content: {response.content}")
        try:
            text = response.content[0].text
        except Exception as ex:
            print(f"[DEBUG] Direct access failed: {ex}")
            text = ""
        print(f"[DEBUG] Response: {len(text)} chars")

        if not text.strip():
            await status.edit_text("Error: Got empty response from AI.")
            return

        saved_path = save_report(company, text)
        await status.edit_text(f"Done — {company}\nSaved to {saved_path}")
        await send_report(update, text)

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
