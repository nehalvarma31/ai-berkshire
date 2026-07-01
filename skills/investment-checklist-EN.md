# Buffett Value Investing Pre-Buy Checklist

Run a Buffett value investing checklist analysis on $ARGUMENTS.

**Supported input formats**: Single or multiple companies, separated by commas or spaces. Examples: `Tesla, Microsoft, Coca-Cola` or `TSLA AAPL MSFT`

## Execution Flow

### Step 1: Parse Input — Identify All Companies

From $ARGUMENTS, extract all company names/tickers. For each company determine:
- Full company name, ticker symbol, exchange
- If the company is private/unlisted, mark as "Unlisted" with a brief note (any indirect investment routes), and skip the full checklist

### Step 1.5: AI Research Bias Warning

Rate each company's "Information Richness" (A/B/C) and include in the report:

| Grade | Criteria | Impact on Checklist |
|-------|----------|---------------------|
| A | Listed for many years, abundant data | Proceed normally, but watch for "consensus trap" — all metrics looking clear doesn't mean certainty |
| B | Limited data, some figures need estimation | Flag each estimated metric with confidence level; weight "good business" judgment by data reliability |
| C | Extremely scarce information | Don't force-fill all six gates; honestly mark "insufficient data to judge"; focus on verifiable core questions |

**Core principle**: The checklist's goal is to **eliminate bad choices**. For Grade C companies, "insufficient data" ≠ "fail" and ≠ "pass" — honestly mark as "grey zone, needs primary research."

Duan Yongping said: "'Can't understand' comes in two types — the business is genuinely too complex, or you haven't spent enough time on it yet. Don't confuse 'scarce data' with 'can't understand.'"

### Step 2: Parallel Data Collection

Use the Task tool to launch an independent background Agent for **each company** simultaneously. Each Agent collects:

1. **Profitability**: ROE (5–10 year trend), gross margin, net margin, free cash flow
2. **Valuation data**: Current price, market cap, P/E (TTM), forward P/E, P/B, dividend yield
3. **Growth trends**: Revenue and profit growth over past 3 years
4. **Financial health**: Debt levels, capex requirements, cash reserves, net cash/debt
5. **Competitive landscape**: Market share, key competitors, share trend
6. **Moat evidence**: Specific evidence of brand/switching costs/network effects/scale/tech barriers
7. **Management track record**: CEO background, key decisions, ownership, capital allocation history
8. **Recent developments**: Major events in last 6 months (earnings, M&A, regulatory, leadership changes)

### Step 3: Run All Six Gates for Each Company

For each listed company, evaluate sequentially:

---

#### Gate 1: Do I Understand This Business? (Circle of Competence)

Must answer:
- [ ] Can I explain in one sentence how this company makes money?
- [ ] What will it most likely be doing in 10 years?
- [ ] What are the key variables that determine success or failure?
- [ ] Is my knowledge of this industry from deep research or hearsay?

**Scoring** (★1–5):
- ★★★★★: Extremely simple and clear business model, high 10-year certainty (e.g. Coca-Cola: make and sell beverages)
- ★★★★☆: Clear model but with a technical dimension requiring some domain knowledge
- ★★★☆☆: Understandable model but low 10-year certainty; fast-changing industry
- ★★☆☆☆: Complex business lines or industry in upheaval; hard to predict future
- ★☆☆☆☆: Completely outside circle of competence

**Hard veto**: If you cannot explain how the company makes money, immediately mark "Outside circle of competence — no analysis."

---

#### Gate 2: Is This a Good Business? (Economic Characteristics)

Let the data speak. **Key metrics must be precisely calculated using tools**:

```bash
python tools/financial_rigor.py verify-valuation \
  --price {price} --eps {EPS} --bvps {book value per share} --fcf-per-share {FCF per share} --dividend {dividend per share}
```

| Metric | Company Value | Benchmark | Judgment |
|--------|--------------|-----------|----------|
| ROE (5-year avg) | | >15% good, >20% excellent | |
| Gross margin | | >40% suggests pricing power | |
| Free cash flow | | Consistently positive, ≈ net income | |
| Capex intensity | | Asset-light better than asset-heavy | |
| Debt level | | Interest-bearing debt / net income < 3 years | |

**Scoring** (★1–5):
- ★★★★★: ROE>25%, high margins, strong FCF, asset-light, low debt (all criteria met)
- ★★★★☆: 4 criteria met
- ★★★☆☆: 3 criteria met
- ★★☆☆☆: 2 criteria met or trend deteriorating
- ★☆☆☆☆: Most criteria unmet or FCF persistently negative

---

#### Gate 3: Is the Moat Deep Enough? (Competitive Advantage)

Check each type:

| Moat Type | Present? | Specific Evidence | Widening or Narrowing? |
|-----------|---------|-------------------|----------------------|
| Brand / Pricing power | | | |
| Switching costs | | | |
| Network effects | | | |
| Cost / Scale advantage | | | |
| Technology / Patent barriers | | | |

Additional test: If a competitor received $1 billion, could they replicate this business?

**Scoring** (★1–5):
- ★★★★★: Multiple overlapping moats that are widening
- ★★★★☆: At least one strong moat that is stable
- ★★★☆☆: Moat exists but isn't deep, or trend unclear
- ★★☆☆☆: Moat is being eroded
- ★☆☆☆☆: No clear moat

---

#### Gate 4: Can Management Be Trusted? (The Human Factor)

| Check | Assessment |
|-------|-----------|
| Integrity (promises vs. delivery) | |
| Capital allocation (buyback/dividend/M&A track record) | |
| Shareholder alignment (ownership, compensation) | |
| Owner mindset (founder vs. hired manager) | |
| Corporate governance (related-party transactions, goodwill, audit) | |
| Can the company run normally if the CEO leaves? | |

**Scoring** (★1–5):
- ★★★★★: Founder-led, excellent capital allocation, fully aligned interests
- ★★★★☆: Strong management with minor blemishes
- ★★★☆☆: Competent management but governance concerns
- ★★☆☆☆: Integrity or governance issues present
- ★☆☆☆☆: Serious integrity problems (→ hard veto)

---

#### Gate 5: Is the Price Low Enough? (Margin of Safety)

| Metric | Value | Historical Percentile | Judgment |
|--------|-------|-----------------------|----------|
| P/E (TTM) | | | |
| Forward P/E | | | |
| P/B | | | |
| Dividend yield | | | |
| FCF Yield | | | |

Additional test (**must use tool — no mental math**):
```bash
python tools/financial_rigor.py three-scenario \
  --price {price} --eps {EPS} --shares {shares in billions} \
  --growth {bull} {base} {bear} --pe {bull PE} {base PE} {bear PE} --currency {currency}
```
- Valuation range across three scenarios (use tool output)
- If your judgment is wrong, what is the maximum loss at the current price?
- If the stock drops 50%, would you add more?

**Scoring** (★1–5):
- ★★★★★: Below 50% of intrinsic value — extreme margin of safety
- ★★★★☆: At 70% of intrinsic value — good margin of safety
- ★★★☆☆: Fair value — average margin of safety
- ★★☆☆☆: Slightly expensive — insufficient margin of safety
- ★☆☆☆☆: Severely overvalued

---

#### Gate 6: Position Sizing and Decision Discipline (Preventing Emotional Errors)

Check the following emotional signals:
- Am I buying because of FOMO?
- Am I buying because someone recommended it?
- If trading halted for 5 years, would I be okay with that?
- Can I write my buy thesis in under 200 words?

---

### Step 4: Mirror Test

For each company, write out the mirror test statement:

> "I am buying ___ at $___ per share because:
> 1. The essence of this business is ___, and I understand it;
> 2. Its moat is ___, and it is widening / narrowing;
> 3. Management ___, and is / is not trustworthy;
> 4. The current price represents ___% of intrinsic value, with / without sufficient margin of safety;
> 5. Even if I'm wrong, the downside risk is manageable / not manageable because ___."

**If you can't complete all 5 sentences — don't buy.** Explicitly mark "Pass" or "Fail."

---

### Step 5: Quick Veto Checklist

Check each item for every company — any one triggered → mark as "Vetoed":

- [ ] Cannot explain how this company makes money
- [ ] Free cash flow negative for 3+ consecutive years with no improvement in sight
- [ ] Management has integrity blemishes
- [ ] Competitive advantage being irreversibly eroded
- [ ] Need "a greater fool to pay more" to make money (speculation)
- [ ] Cannot afford this investment going to zero
- [ ] Buy thesis is mainly "everyone else is buying" or "it's been going up lately"
- [ ] Cannot write the buy thesis in under 200 words

---

### Step 6: Summary Comparison Table (Required for Multiple Companies)

When analyzing multiple companies, generate a comparison table:

| Company | Checklist Pass? | Circle of Competence | Good Business | Moat | Management | Margin of Safety | Key Conclusion |
|---------|----------------|---------------------|---------------|------|------------|-----------------|----------------|
| | | ★☆☆☆☆ | ★☆☆☆☆ | ★☆☆☆☆ | ★☆☆☆☆ | ★☆☆☆☆ | |

---

### Step 7: Final Conclusion and Write to File

Give a clear, unambiguous conclusion for each company:
- ✅ **Checklist Passed** (X/6 gates) — ready to proceed to deep research
- ❌ **Checklist Failed** — state which red line was triggered
- ❓ **Grey Zone** — state the key disputed points and what the investor needs to determine independently
- N/A — Unlisted / not investable

Write the full report to `reports/{CompanyName}/{CompanyName}-checklist-{YYYYMMDD}.md`

## Output Format Requirements

1. Each company gets its own section with: six-gate scorecard + core data table + key risks (3–5 items) + mirror test + clear conclusion
2. For multiple companies, append a summary comparison table at the end
3. All scores must use ★ symbols (★1–5), no half stars
4. Data must include source and date; estimated values must be marked "Estimated"
5. Close with a quote referencing Buffett's first rule: "Rule No. 1: Never lose money."
6. Tone: Direct, sharp, no filler. Intersperse Buffett / Munger / Duan Yongping quotes as commentary

## Core Principles

- **Better to miss than to err**: The checklist's goal is to eliminate bad choices, not to find the best one
- **Honest about circle of competence**: If you don't understand it, say so — don't force the analysis
- **Margin of safety is the lifeline**: A great company bought at the wrong price will still lose you money
- **Mirror test cannot be skipped**: No reason = no buy. No exceptions
