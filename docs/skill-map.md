# AI Berkshire Skill Map

All 18 skills in this toolkit, organized by use case. Each skill is a structured prompt in `skills/` that tells Claude exactly how to research a company or topic.

---

## How to Use a Skill

Copy the skill file to your Claude commands folder and invoke it:
```bash
/investment-checklist AAPL
/investment-research Tesla
/quality-screen MSFT, GOOGL, AMZN
```

---

## Skill Index

### Tier 1 — Start Here (Core Research)

| Skill | File | What It Does | When to Use |
|-------|------|-------------|-------------|
| **Investment Checklist** | `investment-checklist.md` | Buffett's 6-gate pre-buy checklist: circle of competence, business quality, moat, management, margin of safety, discipline | Before any buy decision — eliminates bad choices |
| **Investment Checklist (EN)** | `investment-checklist-EN.md` | English version of above | Same as above, for English-language research |
| **Investment Research** | `investment-research.md` | Deep 8-module analysis using all 4 masters' frameworks | When checklist passes — go deeper |
| **Investment Research (EN)** | `investment-research-EN.md` | English version of above | Same as above, for English-language research |
| **Quality Screen** | `quality-screen.md` | 7-metric quick filter to eliminate non-tier-1 companies fast | First pass on a watchlist — cut the weak ones |

---

### Tier 2 — Team Analysis (Multi-Agent Parallel)

| Skill | File | What It Does | When to Use |
|-------|------|-------------|-------------|
| **Investment Team** | `investment-team.md` | 4 agents run in parallel: Duan Yongping (business), Buffett (financials), Munger (risks), Li Lu (industry) — Team Lead synthesizes | When you want maximum depth and multiple perspectives |
| **Earnings Team** | `earnings-team.md` | 4 masters analyze an earnings report in parallel + WeChat article output | After quarterly earnings release |

---

### Tier 3 — Specialist Research

| Skill | File | What It Does | When to Use |
|-------|------|-------------|-------------|
| **Earnings Review** | `earnings-review.md` | Deep read of a single earnings report using primary sources | When you want to understand a specific quarter |
| **Management Deep Dive** | `management-deep-dive.md` | Focused research on founders/CEOs: decisions, capital allocation, integrity | "Buying stock = buying the people" — do this before large positions |
| **Industry Research** | `industry-research.md` | Full industry value chain scan + 4-masters analysis of individual stocks | When entering a new industry |
| **Industry Funnel** | `industry-funnel.md` | Narrow entire market down to 3 companies using value investing filter | Starting from scratch in an unfamiliar sector |
| **Bottleneck Hunter** | `bottleneck-hunter.md` | Identify global supply chain bottlenecks and arbitrage opportunities | Macro-driven investment themes |
| **Private Company Research** | `private-company-research.md` | Multi-agent deep research framework for unlisted companies | Pre-IPO research or private market analysis |

---

### Tier 4 — Ongoing Portfolio Management

| Skill | File | What It Does | When to Use |
|-------|------|-------------|-------------|
| **Thesis Tracker** | `thesis-tracker.md` | Track your buy thesis over time — flag when assumptions break | Maintain discipline after buying |
| **Portfolio Review** | `portfolio-review.md` | Review overall portfolio: concentration, correlation, position sizing | Monthly/quarterly portfolio check |
| **News Pulse** | `news-pulse.md` | 4 parallel agents diagnose abnormal stock moves: events / regulation / competitors / sentiment | When a stock moves sharply and you need to know why |

---

### Tier 5 — Content & Communication

| Skill | File | What It Does | When to Use |
|-------|------|-------------|-------------|
| **WeChat Article** | `wechat-article.md` | Author-Editor-Reader 3-agent collaboration to write a publishable article | When sharing research publicly |
| **Deep Company Series** | `deep-company-series.md` | 8-article series to fully deconstruct one company | Long-form public research project |
| **Duan Yongping Ask** | `dyp-ask.md` | Answer investment questions the way Duan Yongping would think | Gut-check a decision using his mental models |

---

### Supporting Tools

| Tool | File | What It Does |
|------|------|-------------|
| **Financial Data Standards** | `financial-data.md` | Data source rules, cross-validation requirements, acceptable error thresholds |
| **Financial Rigor Toolkit** | `tools/financial_rigor.py` | CLI math engine: verify market cap, valuation metrics, cross-validate data, Benford's law, three-scenario valuation |

---

## Recommended Workflow

```
New company idea
      ↓
/quality-screen          ← 5 min: eliminate obvious failures
      ↓
/investment-checklist    ← 30 min: 6-gate filter
      ↓ (if passes)
/investment-research     ← 2–4 hours: full deep dive
      ↓ (if buy decision)
/thesis-tracker          ← ongoing: track assumptions post-buy
      ↓
/portfolio-review        ← monthly: manage the whole picture
```

---

## 4 Masters Quick Reference

| Master | Core Question | Primary Skills |
|--------|--------------|----------------|
| **Warren Buffett** | Is this a great business at a fair price? | investment-checklist, investment-research |
| **Charlie Munger** | What can go wrong? Invert, always invert. | investment-research (Step 4), investment-team |
| **Duan Yongping** | Is this the right business, right people, right price? | investment-checklist, management-deep-dive |
| **Li Lu** | Is this company on the right side of civilizational progress? | investment-research (Step 6), industry-research |

---

*Last updated: 2026-07-01 | Skills: 18 | Languages: Chinese (primary), English (EN variants)*
