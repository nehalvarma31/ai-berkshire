import os
import glob
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
🟢 PASS  — Gates 1–4 all strong AND Gate 5 shows adequate margin of safety (price ≤ 70% of base case)
🟡 WATCH — Gates 1–4 strong BUT Gate 5 weak (good business, wrong price)
🔴 AVOID — Any of Gates 1–4 failed OR hard veto triggered (debt crisis, fraud, no moat)

Always give a definitive verdict. Never hedge. Price discipline is absolute.
This is for research and education only. Not investment advice."""


def find_existing_report(company: str) -> Optional[str]:
    company_clean = company.strip().title()
    ticker = company.strip().upper()

    search_names = [company_clean, ticker, company.strip()]
    for name in search_names:
        pattern = f"reports/{name}/{name}-verdict-*.md"
        files = glob.glob(pattern)
        if files:
            latest = sorted(files)[-1]
            with open(latest, "r", encoding="utf-8") as f:
                return f.read()
    return None


def format_for_telegram(text: str) -> str:
    lines = text.split("\n")
    result = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("|") and all(
            c in "-| " for c in stripped.replace("|", "")
        ):
            continue
        if stripped.startswith("|"):
            cells = [c.strip() for c in stripped.split("|") if c.strip()]
            if cells:
                result.append("  " + "  |  ".join(cells))
        else:
            result.append(line)
    return "\n".join(result)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = (
        "🏦 *R-InvestIQ* — AI Value Investing Research\n"
        "Built by Nehal Varma Pericherla · Relanto\n\n"
        "Type any company name or ticker to get a Buffett-style verdict:\n\n"
        "  • Apple  •  MSFT  •  Coca-Cola  •  TSLA\n\n"
        "Already screened:\n"
        "  🟡 Apple (AAPL)\n"
        "  🟡 Google (GOOGL)\n"
        "  🟡 Coca-Cola (KO)\n"
        "  🔴 Intel (INTC)\n\n"
        "_Research and education only. Not investment advice._"
    )
    await update.message.reply_text(msg, parse_mode="Markdown")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = (
        "Just type a company name or ticker:\n\n"
        "Apple · GOOGL · Microsoft · TSLA · Berkshire\n\n"
        "I'll run a full Buffett-style analysis and return a "
        "🟢 PASS / 🟡 WATCH / 🔴 AVOID verdict.\n\n"
        "Takes about 1–2 minutes for a new company."
    )
    await update.message.reply_text(msg)


async def screen(update: Update, context: ContextTypes.DEFAULT_TYPE):
    company = update.message.text.strip()
    if not company:
        await update.message.reply_text("Please type a company name or ticker.")
        return

    status = await update.message.reply_text(
        f"🔍 Screening *{company}*...\nThis takes 1–2 minutes.",
        parse_mode="Markdown",
    )

    existing = find_existing_report(company)
    if existing:
        await status.edit_text(
            f"✅ Found existing report for *{company}*", parse_mode="Markdown"
        )
        text = format_for_telegram(existing)
    else:
        try:
            response = client.messages.create(
                model="claude-sonnet-5",
                max_tokens=2000,
                system=SYSTEM_PROMPT,
                messages=[
                    {
                        "role": "user",
                        "content": (
                            f"Screen {company} using the Buffett 6-gate framework.\n\n"
                            "Give me a one-page verdict with:\n"
                            "- Verdict: 🟢 PASS / 🟡 WATCH / 🔴 AVOID\n"
                            "- One-line reason (the SO WHAT, not just data)\n"
                            "- Business summary: what it does, moat, 10-year outlook\n"
                            "- Gate scorecard: all 6 gates with ★ ratings (1–5)\n"
                            "- Key financials: price, P/E, market cap, revenue, FCF, gross margin, ROE\n"
                            "- Valuation range: Bull / Base / Bear with growth assumptions\n"
                            "- Watch price (10% MoS on base) and Buy price (25% MoS on base)\n"
                            "- Top 2 specific risks\n\n"
                            "Use real current market data. Be specific. No hedging.\n\n"
                            "End with:\n"
                            "⚠️ R-InvestIQ by Nehal Varma Pericherla · Relanto · Not investment advice."
                        ),
                    }
                ],
            )
            text = response.content[0].text
            await status.edit_text(
                f"✅ Done screening *{company}*", parse_mode="Markdown"
            )
        except Exception as e:
            await status.edit_text(f"❌ Error: {str(e)}")
            return

    # Telegram limit is 4096 chars per message
    chunk_size = 4000
    for i in range(0, len(text), chunk_size):
        await update.message.reply_text(text[i : i + chunk_size])


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
