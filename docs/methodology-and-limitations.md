# R-InvestIQ — How It Works, and Where It Falls Short

**Nehal Varma Pericherla | Relanto | Week 5 Summary | 2026-07-27**

---

## What I built

R-InvestIQ is an AI research assistant that screens a company the way Warren Buffett would, and gives you a straight answer: buy-worthy, watch it, or stay away. You type a company name — in a terminal, or now in Telegram — and about a minute later you get back a one-page report with a verdict.

It's built on top of an open-source project called AI-Berkshire, which I forked and adapted. I didn't write the investing logic from scratch — that framework already existed. What I built on top of it is the English-language version, the one-page report format, the automated pipeline that chains the steps together, and the two ways of actually using it: a Telegram bot and a website.

---

## How the screening actually works

Every company gets run through six checks, back to back. I think of them less as a checklist and more as six ways a good idea can quietly go wrong.

**1. Circle of Competence** — Do I actually understand how this company makes money? If the answer requires ten qualifications, it fails here.

**2. Good Business** — Is it consistently profitable, with real cash coming in, not just accounting profit on paper?

**3. Moat** — Is there something durable stopping a competitor from eating this company's lunch? A brand, a network effect, switching costs, something.

**4. Management** — Do the people running it make decisions I'd trust with my own money?

**5. Margin of Safety** — This is the one that trips up almost every "obviously great" company. Even if a business is wonderful, if the stock price already assumes years of perfect execution, there's no room for error. I learned this the hard way running the Apple checklist in Week 1 — great business, but the price left no cushion.

**6. Decision Discipline** — A gut check at the end: am I buying this because the numbers actually support it, or because everyone else is talking about it?

If any of the first four gates fail outright, the verdict is an automatic 🔴 **AVOID** — no amount of cheapness saves a bad business. If the business is strong but the price isn't, it's 🟡 **WATCH**. Only when the business is strong *and* the price has genuine room built in does it get a 🟢 **PASS**.

For valuation, the tool doesn't try to predict one "correct" price. It builds three scenarios — Bull, Base, and Bear — with different growth and P/E assumptions, and checks how much cushion exists between today's price and the Base case. That cushion is the margin of safety.

---

## What's actually running under the hood

- **Claude Code skill files** (`screen-EN.md`, `verdict-report-EN.md`) — these are structured prompts that tell the AI exactly what steps to follow and what format to output in. I wrote and rewrote these several times this project, mostly because my first version used decorative text borders that looked fine in a terminal but broke completely when viewed on GitHub or in a browser.
- **`financial_rigor.py`** — a Python script that cross-checks numbers like market cap (price × shares outstanding) so the AI isn't just trusting whatever figure it generates.
- **A Telegram bot** (`bot.py`) — built in Python using the Anthropic API and python-telegram-bot. Type a company name, get a verdict back in chat, and it auto-saves the report to the GitHub repo.
- **A static website** (`index.html`) — pulls the saved Markdown reports and renders them as a proper webpage, hosted for free on GitHub Pages.

---

## What I actually screened

| Company | Verdict | Why |
|---|---|---|
| Apple (AAPL) | 🟡 WATCH | Exceptional business, but the price already assumes flawless execution — no cushion left |
| Google (GOOGL) | 🟡 WATCH | Same story — strong moat, but priced for the bull case already |
| Coca-Cola (KO) | 🟡 WATCH | Genuinely wonderful business, but the price only offers a razor-thin margin of safety |
| Intel (INTC) | 🔴 AVOID | Negative free cash flow, an eroded moat (lost ground to TSMC and Nvidia), no stable earnings to even value against |

I want to be upfront about something: three WATCHes in a row can look like the tool is broken or overly cautious. It isn't. That's actually what a disciplined framework is supposed to produce — most good companies, most of the time, are not trading at a discount. Finding a genuine 🟢 PASS is supposed to be rare. If I'd forced a PASS just to have one in the demo, that would have defeated the entire point of building this.

---

## Where this genuinely falls short

I'd rather list these honestly than have someone find them for me.

**The numbers aren't independently audited.** `financial_rigor.py` checks internal consistency (does market cap match price × shares), but it doesn't verify the underlying data against a live source like SEC EDGAR in real time. If the AI pulls a slightly outdated revenue figure, the tool won't catch that on its own.

**Growth and valuation assumptions are still somewhat arbitrary.** The Bull/Base/Bear growth rates and P/E multiples are reasoned estimates, not derived from a rigorous model. Two different runs on the same company, weeks apart, could produce slightly different numbers. I flagged this as an open question after Week 1 and it's still true now.

**It has no sense of timing or catalysts.** The tool tells you if a price is cheap relative to value — it says nothing about *when* that gap might close, or what might trigger it to.

**Six companies is not a large sample.** I can't yet say how the framework holds up across sectors I haven't tested — financials, industrials, small caps. Everything so far has been large, well-covered US companies with abundant public data.

**It has no memory across runs.** Each screening is independent. It doesn't know it screened Apple in Week 1, so if the price or story has changed, you have to re-run it and compare manually.

**It can't replace judgment on qualitative risk.** Things like management character, regulatory shifts, or geopolitical exposure get a one-line note, not real investigative depth. A human analyst spending a week on a company would catch things this tool won't.

**This is not investment advice**, and every report says so. It's a structured way to organize research and enforce discipline — not a signal to act on blindly.

---

## What I'd do next with more time

- Wire in a live data source (like an actual stock API) instead of relying on the AI's training knowledge for prices and financials
- Test the framework on a wider mix of industries to see where the six-gate logic breaks down
- Add a simple way to re-screen a company and see how the verdict changed over time

---

*R-InvestIQ · Built by Nehal Varma Pericherla · Relanto · Built on the open-source AI-Berkshire framework (MIT License)*
