# R-InvestIQ Verdict Report — One-Page English Summary

Generate a standardized one-page English verdict report for $ARGUMENTS.

**Supported input**: Company name or ticker. Example: `Apple`, `AAPL`, `Microsoft MSFT`

> This report is for research and education only. It is not investment advice.
> Always do your own research before making any financial decisions.

---

## What This Skill Does

Takes the output of `/investment-checklist-EN` (or raw company research) and condenses it into a clean, one-page verdict that any reader can understand in under 2 minutes.

This is R-InvestIQ's signature output format.

---

## Execution Flow

### Step 1: Check for Existing Research

Look for an existing checklist report in `reports/{CompanyName}/` from the last 30 days.

- If found → use it as the source. Do not re-run the full checklist.
- If not found → run `/investment-checklist-EN {company}` first, then return here.

### Step 2: Extract the 6 Key Inputs

From the checklist report, extract:

1. **Gate scores** — the six ★ ratings
2. **Core financial snapshot** — price, P/E, FCF yield, gross margin, net margin
3. **Three-scenario valuation** — Bull / Base / Bear intrinsic value and margin of safety
4. **Moat summary** — one sentence on what the competitive advantage is
5. **Top 2 risks** — the two most important things that could go wrong
6. **Mirror test result** — Pass / Fail / Grey Zone

### Step 3: Determine the Traffic Light

Apply this logic strictly — no exceptions:

| Result | Condition |
|--------|-----------|
| 🟢 **PASS** | Gates 1–4 all ★★★★☆ or above AND Gate 5 ★★★★☆ or above (price ≤ 70% of base-case intrinsic value) |
| 🟡 **WATCH** | Gates 1–4 strong BUT Gate 5 ★★★☆☆ or below (business is good, price is not right yet) |
| 🔴 **AVOID** | Any of Gates 1–4 is ★★☆☆☆ or below, OR any hard veto triggered |

**Important**: A WATCH rating means "good business, wrong price." It does not mean the business has problems.
A PASS with no margin of safety is not possible — price discipline is non-negotiable.

### Step 4: Generate the One-Page Report

Output exactly this Markdown structure — no more, no less:

```markdown
# R-InvestIQ Verdict Report

## {Company Name} ({Ticker}) · {Exchange} · {Date}

---

## Verdict: {🟢 PASS / 🟡 WATCH / 🔴 AVOID}

**One-line reason:** {Single sentence explaining the verdict — e.g. "Exceptional business but trading at 34x earnings with no margin of safety at $287."}

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

## Mirror Test

> "I am buying {company} at ${price}/share because:
> 1. The business is {description}, and I understand it;
> 2. Its moat is {moat}, and it is {widening/narrowing};
> 3. Management {assessment}, and is {trustworthy/not};
> 4. The price is {X}% of intrinsic value, {with/without} margin of safety;
> 5. Even if I'm wrong, downside is {manageable/not} because {reason}."

**Mirror Test: {✅ PASS / ❌ FAIL / ⚠️ GREY ZONE}**

---

## ⚠️ Disclaimer

This report is produced by **R-InvestIQ**, a research and education tool built on the open-source AI-Berkshire framework (MIT License).

**This is NOT investment advice.** It is a structured research summary for educational purposes only. All data is sourced from public information and may contain errors or be out of date. Past performance of any company does not guarantee future results.

Do your own research. Consult a licensed financial advisor before making any investment decisions.

*R-InvestIQ · Nehal Varma Pericherla · Relanto · {date}*
*AI-Berkshire base by xbtlin · MIT License*
```

### Step 5: Save the Report

Save to: `reports/{CompanyName}/{CompanyName}-verdict-{YYYYMMDD}.md`

Example: `reports/Apple/Apple-verdict-20260706.md`

### Step 6: Confirm to User

After saving, display:
- The full one-page report
- The file path where it was saved
- A one-line prompt: "Run `/verdict-report-EN {next company}` to screen another company."

---

## Core Rules

- **One page maximum** — if it doesn't fit on one page, cut it. The value is in the discipline of condensing.
- **No hedge words** — say WATCH, not "it depends." Say AVOID, not "there are concerns."
- **Price discipline is absolute** — a great business at the wrong price is always WATCH, never PASS.
- **Disclaimer is mandatory** — never omit it. Research and education only.
- **Cite your sources** — every financial figure needs a source and date inline.
- **Use proper Markdown** — always use ## headers, tables, and **bold**. Never use ━━━ border characters — they do not render in GitHub or browser previews.
