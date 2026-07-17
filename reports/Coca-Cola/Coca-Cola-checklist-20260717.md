# The Coca-Cola Company (NYSE: KO) — Buffett Value Investing Pre-Buy Checklist

**Date**: 2026-07-17
**Information Richness Grade: A** — Coca-Cola has been public since 1919, has decades of clean audited data, and is one of the most widely covered companies in the world. The main analytical risk here is not data scarcity but the "consensus trap": everything looks clear and well-understood, which can create false confidence about future certainty (GLP-1 drugs and sugar taxes are genuine structural unknowns, not noise).

---

## 0. Data Cross-Validation

- Price $81.57 × Shares outstanding 4.30B = **$350.75B** (calculated) vs. reported market cap **$350.95B** (stockanalysis.com, Jul 17, 2026). Deviation: **0.06%** — verified via `financial_rigor.py verify-market-cap`. ✅ Pass.
- Sources cross-checked: stockanalysis.com, macrotrends.net, financecharts.com, SEC EDGAR (10-K filed 2026-02-20, DEF 14A filed 2026-04-29), Coca-Cola investor relations, Yahoo Finance, GuruFocus, TipRanks.
- **Flagged discrepancies** (disclosed, not hidden):
  - ROE varies 37.8%–46.99% depending on source/year and equity-base definition. Directionally consistent: high-30s to mid-40s%.
  - Book value per share: $7.48 (GuruFocus) vs. $7.73–$7.97 (macrotrends-linked). Used $7.73 (mid-range) for calculations below.
  - Net debt: source-reported $29.7B vs. this analysis's independent recalculation from the same source's own debt/cash line items ($35.2B) — a ~$5.5B unreconciled gap, likely short-term investments not broken out. Treated conservatively (higher figure) where it affects judgment.
  - Global beverage market share: Coca-Cola vs. PepsiCo essentially tied (26–30%) depending on scope definition — no primary Nielsen/Euromonitor source found.

---

## Gate 1 — Do I Understand This Business? (Circle of Competence)

- **One-sentence business model**: Coca-Cola manufactures beverage concentrate and syrups, sells them to a global network of licensed bottlers who add water/sugar, package, and distribute finished drinks to retailers — Coca-Cola itself owns almost no physical bottling assets after refranchising.
- **10-year outlook**: Very likely still selling Coca-Cola, Sprite, Fanta, and an expanding portfolio of "total beverage" categories (water, tea, coffee via Costa, protein/dairy via Fairlife) through the same bottler-license model. High certainty on business *existence*; moderate uncertainty on *growth rate* given health-trend headwinds.
- **Key variables for success**: brand equity retention, bottler relationship health, ability to pivot the portfolio away from sugary carbonated drinks fast enough to offset GLP-1/sugar-tax volume pressure, pricing power holding up as volume growth flattens.
- **Basis of knowledge**: This is one of the most extensively documented businesses in the world (it is literally the textbook Buffett case study) — assessment is based on deep, verifiable data, not hearsay.

**Score: ★★★★★**
Simple, timeless business model (Buffett has held it since 1988 for this exact reason). No hard veto — clearly within circle of competence.

> 段永平: "能看懂的生意，才配拿一辈子。可口可乐从我小时候就没变过配方逻辑——这就是简单的力量。"

---

## Gate 2 — Is This a Good Business? (Economic Characteristics)

```
python tools/financial_rigor.py verify-valuation --price 81.57 --eps 3.18 --bvps 7.73 --fcf-per-share 2.92 --dividend 2.12
→ PE (TTM) 25.65x | ROE 41.14% | P/B 10.55x | P/FCF 27.93x | FCF Yield 3.58% | Dividend Yield 2.60%
```

| Metric | Value | Benchmark | Judgment |
|---|---|---|---|
| ROE (5-yr trend) | 37.8%–43.3% (2021–2025), ~41% recalculated | >15% good, >20% excellent | ✅ Excellent |
| Gross margin | 61.6% (FY2025) | >40% suggests pricing power | ✅ Excellent |
| Free cash flow | FY2023 $9.7B → FY2024 **$4.7B (-51% YoY)** → FY2025 $5.3B → TTM $12.6B | Consistently positive, ≈ net income | ⚠️ Positive but volatile; FY2024 FCF was under half of net income ($10.6B) — working-capital/tax-timing distortion per company explanation, not yet a multi-year pattern |
| Capex intensity | 4.05%–4.40% of revenue (2023–2025) | Asset-light better than asset-heavy | ✅ Asset-light (bottling refranchised to partners) |
| Debt level | Total debt $45.5B; net debt $29.7B (sourced) to $35.2B (recalculated) vs. net income $13.1B | Interest-bearing debt / net income < 3 years | ⚠️ Borderline: 2.3x–2.7x net income, within but near the upper edge of the benchmark |

**Criteria met: 4 of 5** (ROE, gross margin, capex intensity clear passes; FCF volatility and debt level are the two soft spots — neither is disqualifying, both warrant monitoring).

**Score: ★★★★☆**

> 巴菲特: "我们喜欢的生意是那种，即使是傻瓜也能经营好的生意，因为迟早会有傻瓜来经营它。" — Coca-Cola的经济特征依然符合这个标准，但FCF的年度波动值得关注。

---

## Gate 3 — Is the Moat Deep Enough? (Competitive Advantage)

| Moat Type | Present? | Evidence | Widening or Narrowing? |
|---|---|---|---|
| Brand / Pricing power | Yes | Brand Strength Index 93.4/100 (10th strongest brand globally, 2025); operating margin expanded ~24%→~32% (2020–2025) largely via price increases | **Contested**: pricing-led growth in FY2025, but Q1 2026 growth mix shifted toward volume (8pp) over price (2pp) — some analysts read this as pricing power "fizzling" |
| Switching costs (bottler network) | Yes | ~200 bottling partners, ~900 production facilities, 200+ countries — an irreplicable distribution asset built over a century | Stable |
| Network effects | No | Not applicable to this business model | N/A |
| Cost / Scale advantage | Yes | 2.2 billion servings/day; system unit case volume 33.8B (2025) | **Flat**: unit case volume grew only +0.3% in FY2025 — scale is not currently translating into volume growth |
| Technology / patent barriers | Weak | Formula secrecy is more marketing legend than real economic moat at this scale | N/A |

**"Could a competitor replicate this with $50B?"** No — the century-built bottler relationships and shelf-space/distribution density cannot be bought quickly at any price. This remains the core of the moat.

**Widening evidence**: record operating margins, brand value +32% (2025 BrandZ-style estimate), successful category diversification (Zero Sugar +13% Q1 2026, Fairlife capturing GLP-1-era protein demand).
**Narrowing evidence**: GLP-1 drugs cutting sugary-drink intake ~65% in GLP-1-user households (~20% of higher-income US households); sugar taxes cutting taxed-market sales 15–33%; FY2025 physical volume growth essentially flat; global market share roughly tied with PepsiCo, not clearly gaining share.

**Score: ★★★★☆**
Strong, durable distribution/brand moat — but genuine structural questions (GLP-1, sugar tax, flat volumes) mean this is "stable" rather than "clearly still widening," which is why it doesn't score the top mark.

---

## Gate 4 — Can Management Be Trusted? (The Human Factor)

| Check | Assessment |
|---|---|
| Integrity (promises vs. delivery) | Q1 2026 results beat guidance (comparable EPS $0.86 vs. $0.81 est.); no accounting-integrity red flags found in this research pass |
| Capital allocation | Dividend raised **64 consecutive years** (Dividend King); ~$102B returned via dividends since 2010 (~28% of current market cap); buybacks modest and secondary to dividends; M&A track record mixed-to-good (Costa $5.1B 2019, BodyArmor $5.6B 2021 — both strategic category bets, outcomes reasonably validated by Zero Sugar/protein growth) |
| Shareholder alignment | Insider ownership is low in absolute terms (CEO holds ~132K shares combined across accounts vs. 4.30B shares outstanding) — typical of a hired-manager mega-cap, not founder-owner alignment |
| Owner mindset | Hired-manager company, not founder-led. Partially offset by **Berkshire Hathaway's ~9% stake** — the largest single shareholder, providing long-term-oriented external accountability |
| Corporate governance | Standard large-cap governance; no related-party or audit red flags surfaced |
| Succession risk | **Material recent event**: James Quincey (CEO for 9 years) moved to Executive Chairman effective March 31, 2026; Henrique Braun (internal, prior COO) became CEO the same day. First CEO change in 9 years — track record under the new CEO is, by definition, **untested** |

**Score: ★★★★☆**
Excellent, long-proven capital allocation discipline (dividend consistency is close to unmatched), but the brand-new, untested CEO and low insider ownership keep this just short of the top score.

> 芒格: "我们只想和值得信赖、能力出众的人共事。" Quincey的记录值得信赖；Braun尚待用业绩证明自己。

---

## Gate 5 — Is the Price Low Enough? (Margin of Safety)

| Metric | Value | Historical Context | Judgment |
|---|---|---|---|
| P/E (TTM) | 25.65x (per tool) / 26.70x (stockanalysis.com headline) | KO's historical range is roughly 20–25x; current sits at or slightly above the top of that range | Rich |
| Forward P/E | 25.73x | Essentially flat vs. TTM — market is not pricing meaningful near-term multiple compression or expansion | Fair-to-rich |
| P/B | 10.55x–10.86x | High, but expected for an asset-light brand company; not a useful standalone signal here | Not diagnostic |
| Dividend yield | 2.60% | Below KO's own long-term historical average yield (~3%) | Rich vs. own history |
| FCF Yield | 3.58% (TTM basis) | Modest; would be more attractive above ~5% | Rich |

```
python tools/financial_rigor.py three-scenario --price 81.57 --eps 3.18 --shares 43 \
  --growth 0.09 0.06 0.02 --pe 27 23 17 --years 5 --currency USD

情景        年增速   目标PE   目标EPS   目标股价   涨跌幅(5年)
乐观 Bull    9%      27x     4.89      $132.1     +62.0%
中性 Base    6%      23x     4.26      $97.9      +20.0%
悲观 Bear    2%      17x     3.51      $59.7      -26.8%
```

At the current price of $81.57, the base case implies roughly +20% total return over 5 years (~3.7%/year price appreciation, before dividends) — modest for a 5-year hold. The bear case (-26.8%) is nearly as large in magnitude as the base case's upside, an unfavorable risk/reward skew for a "margin of safety" test. This is consistent with KO trading at the upper end of its historical valuation band rather than at a discount.

**Score: ★★☆☆☆**
Slightly expensive; margin of safety is thin-to-none at the current price. This is a wonderful business priced for its quality, not a bargain.

> 巴菲特: "用平庸的价格买入一家优秀的公司，远好过用优秀的价格买入一家平庸的公司。" — 但"优秀的价格"依然要求价格本身合理，而不是当前这种略贵的水平。

---

## Gate 6 — Position Sizing and Decision Discipline

- **FOMO check**: No — KO is not a momentum stock; the case for owning it (or not) rests on decade-scale compounding logic, not recent price action.
- **Recommendation-driven?**: This is a screen run at user request (ticker "KO"), not driven by a hot tip — self-directed research.
- **5-year trading halt test**: Passable in principle for a Dividend King — the business would very likely still be intact and paying dividends 5 years from now regardless of market closure. This is one of KO's genuine strengths as an investment.
- **200-word thesis test**: Achievable (see Mirror Test below) — but the thesis currently has to concede "price is full," which is itself informative.

**Assessment: Grey Zone** — the business quality and long-hold logic pass cleanly; the entry price does not.

---

## Mirror Test

> "I am buying **Coca-Cola (KO)** at **$81.57** per share because:
> 1. The essence of this business is licensing concentrate and brand equity to a century-old global bottler network, and I understand it;
> 2. Its moat is brand + irreplicable distribution scale, and it is **stable, with genuine open questions (GLP-1, sugar tax, flat unit-case volume) rather than clearly widening**;
> 3. Management (new CEO Henrique Braun, backed by 64 years of dividend discipline under predecessor Quincey) is **provisionally trustworthy on capital allocation, but unproven in the new-CEO seat**;
> 4. The current price represents **roughly fair-to-slightly-rich value versus a 5-year base-case target of ~$98** (three-scenario model), **without** sufficient margin of safety;
> 5. Even if I'm wrong on growth, the downside risk is **manageable** because Coca-Cola's bear case (-26.8% over 5 years per the model) reflects multiple compression on a still-profitable, dividend-paying business, not business failure — but it is **not a low-risk entry point today**."

**Verdict: FAIL on price (Gate 5); PASS on all other sentences.** Per the checklist's own rule, an incomplete mirror test (here, the margin-of-safety sentence) means: **don't buy at this price** — but keep watching.

---

## Quick Veto Checklist

- [ ] Cannot explain how this company makes money — **No, easily explained**
- [ ] FCF negative 3+ consecutive years — **No, FCF has been positive throughout, despite FY2024 volatility**
- [ ] Management integrity blemishes — **No blemishes found in this research pass**
- [ ] Competitive advantage being irreversibly eroded — **Not established; genuine open questions but no irreversible erosion confirmed**
- [ ] Requires "greater fool" to profit — **No, thesis rests on cash flows and dividends, not resale to a bigger buyer**
- [ ] Cannot afford this investment going to zero — **N/A, position-sizing decision for the individual investor**
- [ ] Buy thesis is "everyone else is buying" — **No**
- [ ] Cannot write thesis in under 200 words — **No, see Mirror Test above**

**No hard vetoes triggered.**

---

## Key Risks (3–5, specific)

1. **GLP-1 weight-loss drugs are a structural demand risk, not noise**: households with a GLP-1 user (≈20% of higher-income US households, early-2026 data) show ~65% lower sugary-drink intake — this is a multi-year secular headwind on core carbonated soft drink volume, not a one-quarter blip.
2. **FY2024 free cash flow collapsed 51% year-over-year** ($9.7B → $4.7B) on working-capital/tax-timing items per company explanation; TTM has recovered to $12.6B, but a single data point of recovery does not yet confirm FY2024 was purely one-off — earnings-quality monitoring warranted.
3. **First CEO transition in 9 years is unproven**: Henrique Braun became CEO March 31, 2026, after James Quincey moved to Executive Chairman. Capital allocation discipline under a new CEO carries execution uncertainty by definition, regardless of his prior COO track record.
4. **Physical volume growth has gone essentially flat** (+0.3% unit cases, FY2025), meaning recent revenue growth has been overwhelmingly price/mix-driven — if pricing power is genuinely "fizzling" (as some Q1 2026 coverage suggests, given the shift toward volume-led organic growth), the next leg of growth is less certain than the historical pattern implies.
5. **Valuation offers little cushion**: P/E 25.65–26.7x, dividend yield 2.60% (below KO's own historical average), FCF yield 3.58% — the three-scenario model's bear case (-26.8% over 5 years) is nearly symmetric with the base case's modest upside (+20%), an unfavorable risk/reward setup for a new buyer today.

---

## Final Conclusion

**❓ Grey Zone (5.5/6 gates favorable)** — Coca-Cola clears the business-quality gates (Circle of Competence ★★★★★, Good Business ★★★★☆, Moat ★★★★☆, Management ★★★★☆) comfortably. It fails the price gate (Margin of Safety ★★☆☆☆): the stock is fairly-to-fully valued, not cheap, and carries two live structural questions (GLP-1 drug impact, new/untested CEO) that argue for patience over urgency.

This is a "great business, not-great price" situation — textbook territory for a **watchlist entry with a target buy-price trigger**, not an immediate buy.

---

## Summary Scorecard

| Company | Circle of Competence | Good Business | Moat | Management | Margin of Safety | Key Conclusion |
|---|---|---|---|---|---|---|
| Coca-Cola (KO) | ★★★★★ | ★★★★☆ | ★★★★☆ | ★★★★☆ | ★★☆☆☆ | Grey Zone — quality confirmed, price too high |

---

*"Rule No. 1: Never lose money. Rule No. 2: Never forget rule No. 1." — Warren Buffett*

**Sources**: stockanalysis.com, macrotrends.net, financecharts.com, SEC EDGAR (10-K filed 2026-02-20, DEF 14A filed 2026-04-29), coca-colacompany.com investor relations, Yahoo Finance, GuruFocus, TipRanks, Motley Fool, TheStreet, 24/7 Wall St, market.us, beveragedaily.com — all pulled July 2026. Key valuation figures independently verified via `tools/financial_rigor.py`.
