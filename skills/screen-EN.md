# R-InvestIQ — Screen One Company

Screen $ARGUMENTS using the full R-InvestIQ research pipeline.

**Usage**: `/screen-EN {company}` — Examples: `/screen-EN Microsoft`, `/screen-EN NVDA`, `/screen-EN Coca-Cola`

> This report is for research and education only. Not investment advice.

---

## What This Does

One command. One output. No steps in between.

Takes a company name → runs the full Buffett-style analysis → outputs a clean one-page verdict with a Pass / Watch / Avoid traffic light.

Total time: 10–15 minutes.

---

## Execution Flow

### Step 1: Parse Input

From $ARGUMENTS extract:
- Full company name
- Ticker symbol
- Exchange (NYSE / Nasdaq / etc.)

Tell the user:
```
Screening {Company} ({TICKER})...
This takes about 10–15 minutes. Starting now.
```

---

### Step 2: Check for Existing Research

Look for an existing checklist report in `reports/{Company}/` dated within the last 7 days.

- **If found (less than 7 days old):** Skip to Step 4. Tell the user:
  ```
  Found recent checklist from {date}. Using existing research.
  Generating verdict report now...
  ```

- **If not found (or older than 7 days):** Proceed to Step 3.

---

### Step 3: Run the Investment Checklist

Run the full `/investment-checklist-EN` analysis on {company}:

1. Collect financial data from two independent sources
2. Run all 6 Buffett gates
3. Verify key metrics using `tools/financial_rigor.py`
4. Save the full report to `reports/{Company}/{Company}-checklist-{YYYYMMDD}.md`

Show progress to the user:
```
Step 1/2: Running investment checklist...
  Collecting financial data...
  Running 6-gate analysis...
  Verifying numbers with financial_rigor.py...
  Checklist complete. Saved to reports/{Company}/
```

**If the checklist fails for any reason — stop immediately. Do not attempt to generate the verdict report. Tell the user exactly what went wrong.**

---

### Step 4: Generate the Verdict Report

Once the checklist is complete, immediately run the verdict report:

1. Read the checklist report from `reports/{Company}/`
2. Extract the 6 gate scores, financials, valuation range, top risks, mirror test
3. Apply the traffic light logic:

| Verdict | Condition |
|---------|-----------|
| 🟢 PASS | Gates 1–4 all ★★★★☆ or above AND Gate 5 ★★★★☆ or above |
| 🟡 WATCH | Gates 1–4 strong BUT Gate 5 ★★★☆☆ or below |
| 🔴 AVOID | Any of Gates 1–4 is ★★☆☆☆ or below OR hard veto triggered |

4. Generate the one-page verdict in this exact Markdown format:

```markdown
# R-InvestIQ Verdict Report

## {Company} ({Ticker}) · {Exchange} · {Date}

---

## Verdict: {🟢 PASS / 🟡 WATCH / 🔴 AVOID}

**One-line reason:** {Single sentence — synthesis not just data. Explain the SO WHAT.}

---

## Business Summary

| | |
|---|---|
| **What it does** | {One sentence — how the company makes money} |
| **Moat** | {One sentence — what protects it from competition} |
| **10-year outlook** | {One sentence — where it will likely be in 10 years} |

---

## Gate Scorecard

| Gate | Score | Note |
|------|-------|------|
| 1 — Circle of Competence | {★★★★☆} | {one-line note} |
| 2 — Good Business | {★★★★★} | {one-line note} |
| 3 — Moat | {★★★★☆} | {one-line note} |
| 4 — Management | {★★★★☆} | {one-line note} |
| 5 — Margin of Safety | {★★☆☆☆} | {one-line note} |
| 6 — Decision Discipline | {Pass / Fail / Grey Zone} | {one-line note} |

---

## Key Financials (FY{year})

| Metric | Value | Metric | Value |
|--------|-------|--------|-------|
| Current Price | ${price} | P/E (TTM) | {x}x |
| Market Cap | ${cap} | FCF Yield | {%}% |
| Revenue | ${rev} | Gross Margin | {%}% |
| Net Income | ${ni} | Net Margin | {%}% |
| Free Cash Flow | ${fcf} | ROE | {%}% |

*Data verified: financial_rigor.py · Sources: {source1}, {source2}*

---

## Valuation Range ({horizon}, three-scenario model)

| Scenario | Price Target | Assumptions |
|----------|-------------|-------------|
| 🟢 Bull | ${bull} | {bull growth}% growth · {bull PE}x P/E |
| 🟡 Base | ${base} | {base growth}% growth · {base PE}x P/E |
| 🔴 Bear | ${bear} | {bear growth}% growth · {bear PE}x P/E |

**Current price: ${price} · Margin of Safety: {NONE/THIN/ADEQUATE/STRONG}**

| | Price |
|--|-------|
| Watch price (10% MoS on base) | ${watch} |
| Buy price (25% MoS on base) | ${buy} |

---

## Top Risks

1. **{Risk name}:** {Risk one — specific, not generic}
2. **{Risk name}:** {Risk two — specific, not generic}

---

## ⚠️ Disclaimer

This report is produced by **R-InvestIQ**, a research and education tool built on the open-source AI-Berkshire framework (MIT License).

**This is NOT investment advice.** It is a structured research summary for educational purposes only. All data is sourced from public information and may contain errors or be out of date. Past performance of any company does not guarantee future results.

Do your own research. Consult a licensed financial advisor before making any investment decisions.

*R-InvestIQ · Nehal Varma Pericherla · Relanto · {date}*
*AI-Berkshire base by xbtlin · MIT License*
```

5. Save the verdict to `reports/{Company}/{Company}-verdict-{YYYYMMDD}.md`

Show progress:
```
Step 2/2: Generating verdict report...
  Done.
```

---

### Step 5: Final Output

Print the complete one-page verdict to the terminal.

Then show:
```
Reports saved:
  Checklist → reports/{Company}/{Company}-checklist-{date}.md
  Verdict   → reports/{Company}/{Company}-verdict-{date}.md

Run /screen-EN {next company} to screen another company.
```

---

## Core Rules

- **Never skip the checklist** — verdict without data is opinion, not research
- **Never skip the disclaimer** — every output must carry it
- **Synthesis not aggregation** — the one-line reason must say the SO WHAT, not just report a number
- **One page maximum** — if it doesn't fit on one page, cut it
- **Stop on failure** — if checklist fails, do not guess or estimate. Report the error.
- **Use proper Markdown** — always use ## headers, tables, and **bold**. Never use ━━━ border characters — they do not render in GitHub or browser previews.
