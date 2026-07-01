# Investment Research: Buffett-Munger-Duan Yongping-Li Lu Four Masters Framework

Run a systematic investment research analysis on $ARGUMENTS.

## Research Framework

Based on the methodologies of four investment masters — Warren Buffett, Charlie Munger, Duan Yongping, and Li Lu — execute research in the following seven modules in order:

### Pre-Step: AI Research Bias Awareness (Mandatory)

Before starting research, assess the company's "AI Researchability" and identify potential data biases:

**Information Richness Rating**:
| Grade | Characteristics | AI Research Trap | Mitigation |
|-------|----------------|-----------------|------------|
| A (Information-rich) | Listed for many years, broad analyst coverage, dense media reporting | Consensus too strong; AI output converges with market pricing; limited alpha | Focus on counter-testing: why aren't smart people buying? What risks are being ignored? |
| B (Moderate information) | Listed 1–3 years, limited coverage, some figures need estimation | AI may fill gaps with "reasonable assumptions" — looks complete but carries false certainty | Label each estimated figure with confidence level; distinguish "evidence-based estimate" from "gap-filling" |
| C (Information-scarce) | Recently listed / obscure / frontier market, almost no coverage | AI may be overly conservative due to scarce data, misreading "unclear = bad" | Use first-principles questions (see below); extract business essence from limited information |

**First-Principles Research for Grade C Companies**:
When public data is insufficient, don't try to assemble a "looks complete" report. Instead focus on these foundational questions:
1. Who are the customers? Why do they pay? Do alternatives exist?
2. What drives repeat business — habit, lock-in, or continued value creation?
3. Could a competitor replicate this business with $1 billion?
4. What key decisions has management made? What do those decisions reveal about their judgment and values?

**Bias Self-Check** (maintain throughout the research):
- [ ] Is my sense of "certainty" coming from the business itself, or from the volume of data?
- [ ] If I halved the available data on this company, would my conclusion change?
- [ ] Is the AI's analysis highly similar to market consensus? If so, where is my information edge?
- [ ] Is there a possibility that "few public records but excellent business" is being underestimated?

Include the Information Richness Rating at the start of the report, and note the distinction between "AI research confidence" and "investment certainty" in the final conclusion.

### Step 1: Data Collection

> **Data source standards**: See `skills/financial-data.md`. All financial data must come from two independent sources; discrepancies >1% must be flagged.
> - US stocks: Macrotrends (primary) + StockAnalysis (secondary)
> - HK stocks: AAStocks (primary) + Macrotrends ADR (secondary)
> - A shares: East Money (primary) + CNINFO (secondary)

Use the Task tool to launch a background Agent to collect the following data from the web:

1. Revenue structure: Most recent fiscal year and last 4 quarters by segment, growth rates, gross margins
2. Financial metrics: Revenue, net income, gross margin, operating margin, free cash flow, cash reserves over last 5 years
3. Competitive landscape: Market share, comparison with key competitors
4. Business model and moat: Sources of core competitive advantage
5. Technology capabilities: Core tech stack, R&D investment
6. Management: Founder/CEO background, ownership %, key decision history
7. Industry outlook: TAM (Total Addressable Market), growth forecasts
8. Risk factors: Geopolitics, regulation, supply chain, etc.
9. Current valuation: Market cap, P/E, P/S, PEG, EV/Revenue
10. Bull and bear core arguments

#### Data Cross-Validation (Mandatory — use Financial Rigor Tool)

After data collection, **call `tools/financial_rigor.py` to programmatically verify key data points** — no LLM mental math.

**Data points that must be verified**:
- Total share count (confirm from exchange, Yahoo Finance, StockAnalysis — at least 2 sources)
- Current price and market cap (**manually calculate price × shares and compare to reported market cap to prevent unit errors**)
- Most recent fiscal year revenue and net income (company annual report + at least 1 third-party source)
- Cash reserves and net cash (cash + short-term investments − total debt; note definition differences)
- Management ownership % (distinguish economic interest from voting rights; note dual-class share structures)

**Mandatory Verification Steps (run via Bash)**:

Step 1 — Market cap verification (precise decimal, not floating point):
```bash
python tools/financial_rigor.py verify-market-cap \
  --price {price} --shares {total shares} --reported {reported market cap} --currency {currency}
```

Step 2 — Multi-source cross-validation for key data:
```bash
python tools/financial_rigor.py cross-validate \
  --field {field name} --values '{"Source1": value, "Source2": value}' --unit {unit}
```
Run separately for revenue, net income, and cash reserves.

Step 3 — Precise valuation metric verification (P/E, P/B, ROE, FCF Yield, etc.):
```bash
python tools/financial_rigor.py verify-valuation \
  --price {price} --eps {EPS} --bvps {book value per share} --fcf-per-share {FCF per share} --dividend {dividend per share}
```

**Verification rules**:
1. At least 2 independent sources for each key data point
2. When sources disagree, prioritize company annual report/exchange data and note the discrepancy reason
3. **All data involving calculations must be verified by the tool — no LLM mental math**
4. Tool output goes directly into the report appendix under "Key Data Cross-Validation Record"
5. If the tool reports ❌ excessive deviation, investigate the cause before proceeding

**Common error prevention**:
- Market cap units: HKD billions vs RMB billions vs USD billions — easy to drop or add a zero
- FCF definition: Different sources may define capex differently (including/excluding leases, acquisitions)
- Debt definition: Whether operating lease liabilities are included
- Ownership %: Economic interest ≠ voting rights for dual-class share companies

### Step 2: Business Essence Analysis — Duan Yongping's "Right Business"

Analysis points:
- Define the essence of this business in one sentence
- Revenue structure breakdown (table/chart)
- 5-year profitability trend (table/chart)
- Business model canvas: One-time sale vs. subscription/repeat purchase? Hardware vs. software vs. platform?
- Ecosystem stickiness / customer lock-in strength
- Gross margin level vs. industry peers — explain why it is high/low
- Operating leverage analysis
- **Duan Yongping's question**: What makes this business good? If you had to describe it in one sentence, what would it be?

### Step 3: Moat Assessment — Buffett's "Economic Moat"

Verify each of the five moat types:

| Moat Type | Verification Method |
|-----------|-------------------|
| Brand / Pricing power | Can they raise prices without losing sales volume? |
| Switching costs | How high is the cost for customers to migrate to a competitor? |
| Network effects | Does the product get better as more people use it? |
| Scale advantage | How large is the cost advantage from scale? |
| Technology / Patent barriers | How many years ahead technologically? Can it be replicated? |

Analyze moat trend: Has it widened or narrowed over the past 5 years? Project for the next 5 years.

**Buffett's question**: Will this moat still exist in 10 years? What could destroy it?

### Step 4: Reverse Thinking and Risk Inventory — Munger's "Invert, Always Invert"

- List all paths by which this company could fail (table: path / probability / severity)
- Historical analogy: Find companies that were in a similar position historically — what happened to them?
- Cross-disciplinary analysis: Validate using network effect theory, technology adoption curves, competitive game theory
- Bias check: Narrative bias, anchoring effect, survivorship bias
- Collect the bear case's core arguments

**Munger's question**: Where am I most likely to be wrong? Why would a smart person not buy — or short — this company?

### Step 5: Management Assessment — Duan Yongping's "Right People" + Buffett's "Management Integrity"

- CEO/Founder key decision retrospective (table: date / decision / outcome / rating)
- Capital allocation ability: R&D ROI, M&A success rate, buyback timing
- Shareholder alignment: Management ownership, compensation structure, insider selling record
- Organizational capability: Team stability, key talent risk
- Corporate culture characteristics

**Duan Yongping's question**: If the CEO retired, could this company maintain its competitiveness?

### Step 6: Industry and Civilization Trends — Li Lu's "Civilizational Progress Framework"

- Determine whether the industry is in a "civilization-level paradigm shift"
- Historical technology revolution analogy (steam engine / electricity / internet / AI)
- TAM growth curve and ceiling analysis
- Company's position in the industry value chain
- Technology roadmap risk
- Customer/supplier concentration analysis

**Li Lu's question**: Looking back from 20 years in the future, will this company be "the Standard Oil of its era" or "a flash-in-the-pan 3Com"?

### Step 7: Valuation and Margin of Safety — Buffett's "Intrinsic Value" + Duan Yongping's "Right Price"

- Current market pricing (key valuation metrics table) — **must be verified by tool**
- Reverse DCF: What growth expectations are implied by the current stock price?
- Three-scenario valuation — **must be calculated precisely by tool, no mental math**:
```bash
python tools/financial_rigor.py three-scenario \
  --price {price} --eps {EPS} --shares {total shares in billions} \
  --growth {bull growth} {base growth} {bear growth} \
  --pe {bull PE} {base PE} {bear PE} --years 3 --currency {currency}
```
- Compare to the company's own historical valuation
- Compare to peer valuations

**Duan Yongping's question**: If the stock market closed tomorrow for 5 years, would you be willing to hold at this price?

### Step 8: Comprehensive Decision Memo

Summary table:

| Dimension | Conclusion | Confidence |
|-----------|-----------|-----------|
| Business quality (Duan Yongping) | | |
| Moat (Buffett) | | |
| Management (Duan Yongping + Buffett) | | |
| Biggest risk (Munger) | | |
| Civilization trend (Li Lu) | | |
| Valuation (Buffett + Duan Yongping) | | |

Final decision table:

| Strategy | Recommendation |
|----------|---------------|
| No position | |
| Existing holder | |
| Sell signal | |
| Add signal | |

Simulated commentary from each of the four masters (use quote format).

## Output Requirements

1. All analysis must be data-supported with sources cited
2. Use Markdown tables for key data
3. Each module must end with the relevant master's "key question"
4. Write the full report to `reports/{CompanyName}/{CompanyName}-research-{YYYYMMDD}.md`
5. Conclusions must be explicit — do not avoid giving a buy / hold / avoid recommendation
6. Valuation section must provide a specific price range
7. **Report opening** must include "Information Richness Rating" (A/B/C) and "AI Research Limitations Disclosure"
8. **Report closing** must distinguish "AI analysis confidence" from "investment certainty" — the former depends on data volume, the latter on business fundamentals. Explicitly tell the reader which conclusions are based on solid data and which on limited-information reasoning
9. If the company is Grade C (information-scarce), the report must end with a "Questions Requiring Primary Verification" list — encourage the reader to supplement AI blind spots through field research, product experience, supply chain interviews, etc.

## Data Spot-Check (Pre-Publication Flow)

After writing the report, **must** run a data spot-check before publishing:

**Step 1 — Extract spot-check list (15% random sample)**:
```bash
python tools/report_audit.py extract \
  --report <report file path>
```
Outputs a JSON template; each item contains `fetched_value` (to be filled).

**Step 2 — Source verification**:
For each data point in the list, retrieve figures from reliable sources per `skills/financial-data.md` standards (US: Macrotrends + StockAnalysis; HK: AAStocks + Macrotrends; A shares: East Money + CNINFO), and fill in `fetched_value` / `fetched_source` / `fetched_value2` / `fetched_source2`.

**Step 3 — Issue verdict**:
```bash
python tools/report_audit.py verdict \
  --results '<completed JSON>' \
  --report <report file name>
```

- **[PASS]**: All spot-check points within ≤1% deviation → report may be published
- **[REJECT]**: Any point >1% deviation → correct the data and re-run spot-check until passing
