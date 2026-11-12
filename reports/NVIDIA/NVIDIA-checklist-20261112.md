# NVIDIA Corporation (Nasdaq: NVDA) — Buffett Value Investing Pre-Buy Checklist

**Date**: 2026-11-12 (prices are intraday, mid-morning ET)
**Information Richness Grade: A, with a fast-moving-event warning.** NVIDIA is one of the most heavily covered companies in the world, and the repo already holds 14 Chinese-language research files on it (`reports/英伟达/`, April 2026). Two traps apply here:
- **Consensus trap.** Abundant data can make the future look more certain than it is.
- **Breaking-news trap.** The founder-CEO resigned *today*. Several facts below are hours old, come from same-day reporting, and may be revised.

**What changed since the April 2026 research** (verdict then: "good company, wrong price — wait for $120–140"):

| | April 20, 2026 | November 12, 2026 |
|---|---|---|
| Price | $200 | ~$160 (intraday range $148.80–$162) |
| P/E (TTM) | 40.8x | **20.2x** |
| Earnings base | FY2026 EPS $4.90 | TTM EPS $7.91; run-rate ~$9.88 (est.) |
| CEO | Jensen Huang (founder, since 1993) | **Colette Kress, interim** (Huang resigned 2026-11-11/12) |
| Repo verdict | Expensive → don't buy | **Avoid for now (Gate 4)** — see below |

---

## 0. Data Cross-Validation

- **Market cap.** $173.73 (Nov 11 close) × 24.3B shares = $4.22T calculated, vs. $4.19T reported (Google Finance). Deviation **0.76%** ✅. Checked with `financial_rigor.py verify-market-cap`. At today's ~$160: **~$3.89T**.
- **TTM EPS $7.91.** Two independent sources agree exactly (deviation 0.00%, `cross-validate`):
  - MarketBeat: $228.87 ÷ 28.93x P/E (Sep 22)
  - Google Finance: $173.73 ÷ 21.96x P/E (Nov 11)
- **Q2 FY2027 revenue.** $96.22B (Google Finance) vs. $96.2B (CME/eciks earnings preview). Deviation 0.01% ✅.
- **Today's price.** ~$160: CNBC "about $160"; Benzinga $160.24, down 7.76%. The intraday low was $148.80 (The Hill).
- **Flagged discrepancies** (disclosed, not hidden):
  - **TTM free cash flow ~$119B** comes from a single source (est.). The verified figure is FY2026 FCF of $96.7B (10-K, via the repo's April report).
  - **Book value per share $6.44** is from FY2026 year-end (Jan 2026) and is stale. P/B and ROE derived from it are approximate.
  - **The resignation reason** has not been stated by the company. The affair reports are described as "admitted" (first relationship, per CNBC/Bloomberg) in some outlets and as "allegations" in others. NVIDIA has not commented on the second (Kimberly Powell) report.
  - **Analysts' prior price targets** differ across outlets for the same firm (e.g., Baird's prior target is quoted as both $400 and $500). Only the new targets are used here.
  - **Share count.** Shares outstanding of 24.3B is an estimate between FY2026's 24.43B and the 24.12B implied by Google's Nov 11 market cap.

---

## Gate 1 — Do I Understand This Business? (Circle of Competence)

- **One-sentence business model:** NVIDIA designs AI accelerators (GPUs) and full rack-scale systems, plus the networking (NVLink, InfiniBand/Spectrum-X) and CUDA software that tie them together. It sells mainly to cloud providers and AI labs, and TSMC does the manufacturing. Data center was 89.7% of FY2026 revenue.
- **10-year outlook:** Very likely still the leading AI compute platform. Its share of the market and its margins are much less certain:
  - Every top customer is building in-house chips (Google TPU, Amazon Trainium, Meta MTIA, Microsoft Maia).
  - Inference is fragmenting faster than training.
- **Key variables:**
  - Hyperscaler AI capex cycle
  - Training vs. inference share against custom silicon
  - China export controls
  - Annual product cadence (Blackwell → Rubin)
  - New this week: who leads the company
- **Basis of knowledge:** Deep, documented research (14 repo reports plus current data), not hearsay.

**Score: ★★★★☆** — The model is clear but has a real technical dimension, and the industry changes fast. 10-year *existence* is high-certainty; 10-year *economics* are not.

---

## Gate 2 — Is This a Good Business? (Economic Characteristics)

```
python tools/financial_rigor.py verify-valuation --price 160 --eps 7.911 --bvps 6.44 --fcf-per-share 4.90 --dividend 1.00
→ PE (TTM) 20.23x | Earnings yield 4.94% | P/B 24.84x | P/FCF 32.65x | FCF Yield 3.06% | Dividend Yield 0.62%
```

| Metric | Value | Benchmark | Judgment |
|---|---|---|---|
| ROE | 124.4% (FY2026), 115.3% (FY2025) | >15% good, >20% excellent | ✅ Exceptional |
| Gross margin | 71.1% (FY2026). Q3 FY2027 guided ~74% ±0.5pt | >40% suggests pricing power | ✅ Exceptional, and back up from the 71% trough the April report worried about |
| Free cash flow | FY2026 $96.7B = **81% of net income** ($120.1B). TTM ~$119B (est.) | Consistently positive, ≈ net income | ✅ High-quality earnings |
| Capex intensity | Fabless; manufacturing outsourced to TSMC | Asset-light better | ✅ Asset-light |
| Debt level | Total debt $8.5B vs. net income $120.1B = **0.07 years** | Debt / net income < 3 years | ✅ Effectively debt-free |

**Criteria met: 5 of 5.**

**Score: ★★★★★**

**Counter-evidence (cycle caveat):** Revenue roughly doubled in a year (Q2 FY2027 $96.2B, +106% YoY), and Q3 is guided to ~$108B. Spectacular economics at the *top of a capex cycle* are exactly what cyclical peaks look like. This gate grades the economics, which are outstanding; how long they last is for Gates 3 and 5.

---

## Gate 3 — Is the Moat Deep Enough? (Competitive Advantage)

| Moat Type | Present? | Evidence | Widening or Narrowing? |
|---|---|---|---|
| Pricing power | Yes | Gross margin 71%→~74% guided. But largest customers' in-house chips exist specifically to break NVIDIA's pricing | **Mixed:** holding for now, under structural attack at the top |
| Switching costs (CUDA) | Yes | Two decades of CUDA libraries and developer tooling; deepest lock-in among startups, universities and researchers | **Narrowing at the top:** OpenAI Triton, PyTorch multi-backend and Google TorchTPU make CUDA "optional" for the largest buyers |
| Network effects | Partial | CUDA developer ecosystem reinforces itself | Stable in the long tail |
| Scale | Yes | Largest buyer of leading-edge foundry/packaging capacity. Reported ~$279B supply commitments (single source) | Stable |
| Technology barriers | Yes | NVLink/NVSwitch rack-scale systems are roughly 1–2 years ahead | **Narrowing slowly:** UALink consortium (AMD, Intel, Google, Meta, Microsoft) targets a replacement |

**"Could a competitor replicate this with $50B?"** Not the full stack, and not quickly. But the customers *themselves* are spending tens of billions on alternatives, and Google now sells TPUs externally (Anthropic, Meta).

- **Customer concentration:** the top 4 customers were 61% of FY2026 revenue, and all four are building their own chips.

**Score: ★★★☆☆** — The training moat is strong and margins recovered, but erosion at inference and at the largest customers makes the trend *unclear*, not *widening*. This is consistent with the repo's April score of 3.2/5.

---

## Gate 4 — Can Management Be Trusted? (The Human Factor)

**What happened (Nov 8–12, 2026):**
1. **Nov 8.** The board opened an independent investigation into whether founder-CEO Jensen Huang was targeted by a foreign intelligence effort.
   - Huang told staff he had an affair with Alice Huang (no relation). She is affiliated with Megaspeed, a cloud company and NVIDIA customer.
   - U.S. intelligence agencies reportedly suspect she passed information to Beijing. China calls the "spy narrative" unsubstantiated.
   - The board said it had no reason to believe national security or NVIDIA secrets were compromised, and expressed confidence in Huang.
2. **Nov 10.** The board retained Wachtell, Lipton, Rosen & Katz, overseen by a committee of independent directors.
3. **Nov 11.** The New York Times reported a second relationship, with senior NVIDIA executive Kimberly Powell. The Wall Street Journal and Reuters then reported the board was meeting to remove Huang.
4. **Nov 11–12.** Huang **resigned as president, CEO and director, effective immediately** (8-K).
   - CFO **Colette Kress is interim CEO**.
   - **Harvey C. Jones** becomes the company's first-ever board chair.
   - A permanent-CEO search (internal and external) is under way.
   - The company gave no reason for the resignation.

| Check | Assessment |
|---|---|
| Integrity (promises vs. delivery) | Operational delivery has been outstanding (guidance beats, annual product cadence). **The integrity issue is personal conduct at the top:** an undisclosed relationship with a senior employee, and an alleged foreign-intelligence exposure through a customer-linked contact |
| Capital allocation | Historically excellent: FY2026 buybacks $40.1B, $62.2B authorization remaining, $8.5B total debt. Landmark deals: Mellanox ($7B, 2020), Groq ($20B, Dec 2025) |
| Shareholder alignment | Strong while the founder ran it. The new leadership's alignment is **unknown** |
| Owner mindset | **Lost.** A 33-year founder-operator is replaced by an interim hired manager |
| Corporate governance | **The board's response is a positive:** independent investigation, outside counsel, an independent chair created, and 10 of 11 directors independent. **But** it went from "confidence" (Sunday) to removal (Wednesday), so information is still emerging. The investigation is **open** |
| Can the company run normally if the CEO leaves? | **Being tested right now.** The repo flagged "no succession plan — single point of failure" in April 2026. Kress has been CFO since 2013 and is credible with Wall Street, but she is not a product or architecture leader |

**Score: ★★☆☆☆** — Integrity/governance issues are present and unresolved: the investigation is open, there is no permanent CEO, and the strategic track record this gate grades left with the founder.

This is **not** a judgment that Kress or the board is untrustworthy. It means there is nothing yet to grade. The score should be re-run when a permanent CEO is named and the investigation concludes.

> Buffett: "We look for three things when we hire people… intelligence… initiative or energy… and integrity. And if they don't have the latter, the first two will kill you."

---

## Gate 5 — Is the Price Low Enough? (Margin of Safety)

| Metric | Value | Context | Judgment |
|---|---|---|---|
| P/E (TTM) | **20.23x** (tool) | 40.8x in April; now below the 52-week low ($164.27–$243.37 range) | Cheap vs. its own history |
| Run-rate P/E | **16.19x** | Q3 FY2027 consensus EPS $2.47 × 4 = $9.88 (est.) | Looks cheap, but these are peak-cycle earnings |
| P/B | 24.8x (stale BVPS) | Asset-light; not diagnostic | — |
| Dividend yield | 0.62% | Token dividend | Not diagnostic |
| FCF yield | 3.06% TTM (est.) / 2.49% FY2026 basis | Would be compelling above ~5% | Fair |

```
python tools/financial_rigor.py three-scenario --price 160 --eps 9.88 --shares 243 \
  --growth 0.18 0.06 -0.15 --pe 22 18 13 --years 3 --currency USD

Scenario      Growth/yr   Target P/E   Target EPS   Target Price   Change (3 yrs)
Bull            18%         22x         16.23        $357.1        +123.2%
Base             6%         18x         11.77        $211.8         +32.4%
Bear           -15%         13x          6.07         $78.9         -50.7%
```

**Assumptions:**
- **P/E multiples are about 2 points lower than the pre-resignation screen** (25/20/15). That's a leadership discount: the market won't pay a founder premium without the founder.
- **The Bear case** is the AI capex cycle turning in 2027–28, with execution slipping under new leadership. That roughly matches the April report's "capex peak" scenario.

| Threshold | Price | Basis |
|---|---|---|
| **Intrinsic value today (base)** | **$159.14** | Base 3-year target $211.8 discounted at 10%/yr |
| Watch price (10% MoS) | $143.22 | 90% of intrinsic |
| Buy price (25% MoS) | $119.35 | 75% of intrinsic |
| Gate 5 ★★★★☆ threshold (70%) | $111.40 | Repo's PASS standard |
| *If a credible permanent CEO is named* (base P/E back to 20x) | intrinsic $176.82 · watch $159.14 · buy $132.61 · PASS ≤ $123.77 | Leadership discount removed |
| Probability-weighted 3-year target (25/50/25, assumption) | $214.90 (+34%) | Bull/Base/Bear weighted |

- **Maximum loss if wrong:** −51% in the modeled Bear case. The April report's extreme scenario (Cisco-2000-style) was ~$30, or −81%.
- **"If it drops 50%, would you add?"** Only after Gate 4 is re-scored. Today you would be adding to an unknown leadership team.

**Score: ★★★☆☆** — Fair value, with no margin of safety. At ~$160 the stock trades almost exactly at the leadership-adjusted base-case value ($159). The market has already priced the CEO hit; it has not priced a cushion.

> Buffett: "Price is what you pay; value is what you get." Right now the two numbers are the same.

---

## Gate 6 — Position Sizing and Decision Discipline

- **FOMO check:** ⚠️ This screen was prompted by a headline-driven drop: the post-midterm data-center selloff, then the CEO scandal. Buying a falling stock mid-scandal is the classic "buy the dip" impulse.
- **Recommendation-driven?** No. This is self-directed research.
- **5-year trading-halt test:** The business would very likely still be intact and highly profitable. **Who runs it** is the unknown.
- **200-word thesis test:** It can't be completed honestly today, because sentence 3 of the Mirror Test (management) has no answer yet.
- **Timing:** Earnings are on **Nov 17**, five days away, and will be the interim CEO's first major test.

**Assessment: ❌ Fail (today).** The decision would be driven by price action and news flow, not a completed thesis.

---

## Mirror Test

> "I am buying **NVIDIA (NVDA)** at **~$160** per share because:
> 1. The essence of this business is selling the dominant AI compute platform (chips, systems, networking and CUDA software) to cloud providers and AI labs, and **I understand it**;
> 2. Its moat is CUDA plus full-stack systems, and it is **stable in training but narrowing at inference and at its largest customers**;
> 3. Management **is unknown**. The founder-CEO resigned today, the interim CEO is the CFO, the permanent CEO is not yet chosen, and a national-security investigation is open. I **cannot yet say whether it is trustworthy**;
> 4. The current price represents **~100% of leadership-adjusted intrinsic value ($159)**, **without** margin of safety;
> 5. Even if I'm wrong, the downside risk is **not clearly manageable**. The Bear case is −51%, and the leadership vacuum adds execution risk at the exact moment the AI capex cycle and custom-silicon competition are testing the moat."

**Verdict: ❌ FAIL.** Sentences 3, 4 and 5 cannot be completed honestly. Per the checklist rule: **don't buy.**

---

## Quick Veto Checklist

- [ ] Cannot explain how this company makes money — **No.** Easily explained.
- [ ] FCF negative for 3+ consecutive years — **No.** FCF is ~$97–119B per year.
- [x] Management has integrity blemishes — **⚠️ Triggered at the former CEO level.** The individual has left and the board acted decisively, but the investigation is open and its conclusions are unknown.
- [ ] Competitive advantage being irreversibly eroded — **Not established.** Erosion is partial (inference and top customers), not irreversible.
- [ ] Requires a "greater fool" to profit — **No.** The thesis would rest on cash flows.
- [ ] Cannot afford this investment going to zero — **Position-sizing decision.** The repo's guidance is ≤3–5% of a portfolio for NVDA.
- [x] Buy thesis is mainly "it's been moving" or "everyone's talking about it" — **⚠️ At risk.** The research was triggered by price drops and headlines.
- [x] Cannot write the buy thesis in under 200 words — **⚠️ Today, yes.** The management sentence has no answer.

**Not a hard veto** (the former CEO's integrity issue left with him), but three soft flags are raised. Combined with Gate 4 at ★★☆☆☆, the strict verdict logic gives **AVOID**.

---

## The Other Side (Bull Arguments, Weighed Fairly)

1. **The business didn't change overnight.**
   - Q3 FY2027 revenue is guided to ~$108B with ~74% gross margin.
   - Consensus is ~$108.8–109B revenue and $2.47 EPS.
   - Analysts still see NVIDIA as 2–3 years ahead of China in AI chips.
2. **Governance may come out stronger.**
   - First independent chair, a fully independent investigation, and a board that acted within four days.
   - A Janus Henderson portfolio manager called the resignation a "clearing event."
3. **Continuity in finance and operations.** Kress has run finance since 2013 and has delivered most of the guidance the market relied on during the AI boom.
4. **Wall Street is split, not unanimously negative:**

| Stance | Firms (new rating / price target) |
|---|---|
| **Downgraded** | Bernstein (market perform, $200), Melius (hold, $185), Baird (neutral, $200), Oppenheimer (perform, no target), KeyBanc, William Blair, StoneX (hold) |
| **Kept positive, cut target** | BMO ($240 from $340), Citi ($225 from $285), Wedbush/Ives ($225 from $300); Morgan Stanley kept Overweight but removed it from its preferred list |
| **Kept positive** | Goldman Sachs (Buy, $220), Raymond James (Strong Buy, $515) |

> Munger: "Invert, always invert." The bull case is real. But the question this checklist asks is not "could it go up?" It is "do I know enough, at a price low enough, to not lose money?" Today the answer is no.

---

## Key Risks (3–5, specific)

1. **Leadership vacuum with no succession plan.**
   - A 33-year founder who personally drove the CUDA bet, the AI pivot and the annual architecture cadence is gone.
   - The interim CEO is a finance executive, not a product architect.
   - A permanent search (internal and external) could take months, and senior talent loyal to Huang may leave in the meantime.
2. **National-security spillover into export policy.**
   - The alleged foreign-intelligence link runs through a person tied to a customer (Megaspeed).
   - Lawmakers are already calling for inquiries and new limits on foreign chip sales.
   - The board's Nov 8 statement ("no reason to believe" secrets were compromised) came *before* the investigation concludes.
3. **Peak-cycle earnings plus customer concentration.**
   - Run-rate EPS (~$9.88) is about 2× FY2026 ($4.90). That's why the P/E looks cheapest exactly when risk is highest.
   - The top 4 customers (61% of FY2026 revenue) are all building replacement chips.
4. **Neocloud stress and circular financing.**
   - NVIDIA helps finance customers like CoreWeave and Nebius.
   - CoreWeave carries ~$50B of debt, had −$5.74B FCF, has bonds yielding 15%+, and its stock is down 57% in 6 months.
   - This is close to the April report's warning signal for "circular financing chain breaks."
5. **Political limits on data-center demand.**
   - After the Democratic midterm sweep, Texas Gov.-elect Gina Hinojosa pledged to ban new data-center approvals. Texas holds ~27% of planned capacity, and Texas plus Georgia ~⅓ of AI data-center spending.
   - Goldman *expects* conditional moratoria in TX/GA/MI. This is a forecast, not enacted law.

---

## Final Conclusion

**❌ Checklist Failed — red line: Gate 4 (Management) ★★☆☆☆.**

NVIDIA's economics are still among the best ever recorded (Gate 2 ★★★★★). But the founder-CEO resigned today amid an open national-security investigation, there is no permanent successor, and at ~$160 the stock trades at fair value ($159), not at a discount.

This is **"a great business temporarily without a captain, priced at fair value."** It is not a broken business. That distinction matters for *when* to look again:

| Re-screen trigger | What it would change |
|---|---|
| A permanent CEO with a credible track record is named | Gate 4 can be re-scored. If ≥ ★★★★☆, the verdict upgrades to WATCH; with leadership-adjusted intrinsic value of ~$177, the buy price is ~$133 and PASS ≤ ~$124 |
| The investigation concludes with no compromise of secrets and no new export restrictions | Removes the national-security tail risk |
| Nov 17 earnings: guidance ≥ consensus and gross margin ≥ 70% | Confirms the business hasn't wobbled under interim leadership |
| Price ≤ $119 (current buy price) or ≤ $111 (PASS threshold) | Margin of safety appears even with the leadership discount |

**Warning signals to watch** (from the repo's April framework, still valid):
- Hyperscaler capex growth turning negative
- A major neocloud financing failure
- Gross margin below 65% for two quarters
- Data-center moratoria actually enacted

---

## Summary Scorecard

| Company | Circle of Competence | Good Business | Moat | Management | Margin of Safety | Decision Discipline | Key Conclusion |
|---|---|---|---|---|---|---|---|
| NVIDIA (NVDA) | ★★★★☆ | ★★★★★ | ★★★☆☆ | ★★☆☆☆ | ★★★☆☆ | ❌ Fail (today) | AVOID for now — world-class economics, no proven leader, no margin of safety |

---

*"Rule No. 1: Never lose money. Rule No. 2: Never forget rule No. 1." — Warren Buffett*

**Sources** (pulled November 6–12, 2026):
- SEC EDGAR NVIDIA 8-K (CEO transition, Nov 11–12, 2026)
- NVIDIA newsroom (Statement From NVIDIA Board of Directors)
- NVIDIA FY2026 10-K (via repo `reports/英伟达/最终报告-安全边际-20260420.md`)
- Google Finance (Nov 11 quote)
- MarketBeat
- CNBC, NPR, CNN, Bloomberg, Reuters (via Apple News and Semafor), ABC News, CBS News, Forbes, The Hill, CoinDesk, Benzinga, Investing.com, Yahoo Finance, MLQ.ai
- CME Group / eciks.org (Q3 FY2027 preview)
- io-fund, 24/7 Wall St (CoreWeave/Nebius data)
- StockTitan, Yahoo Finance (post-midterm data-center selloff)

All valuation figures verified with `tools/financial_rigor.py` (verify-market-cap, cross-validate, verify-valuation, three-scenario, calc).

*This is research and education, not investment advice.*
