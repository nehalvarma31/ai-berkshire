# R-InvestIQ — Research Workflow

**Built by:** Nehal Varma Pericherla · Relanto
**Base:** AI-Berkshire · MIT License · xbtlin

---

## What This Does

You type a company name. R-InvestIQ runs it through a Buffett-style analysis and gives you a one-page verdict — Pass, Watch, or Avoid.

Takes about 10–15 minutes per company.

---

## How to Run It

### 1. Open the project

Open PowerShell and run:

```
cd OneDrive/Desktop/ai-berkshire
claude
```

Select **"Yes, I trust this folder"** when prompted.

---

### 2. Run the checklist

```
/investment-checklist-EN {company}
```

Examples:
```
/investment-checklist-EN AAPL
/investment-checklist-EN GOOGL
/investment-checklist-EN Microsoft
```

This collects financial data, runs all 6 Buffett gates, and verifies the numbers using `financial_rigor.py`. Takes 7–10 minutes.

Report saves to: `reports/{Company}/{Company}-checklist-{date}.md`

---

### 3. Run the verdict report

```
/verdict-report-EN {company}
```

This reads the checklist and produces a clean one-page summary. Takes 1–2 minutes.

Report saves to: `reports/{Company}/{Company}-verdict-{date}.md`

---

### 4. Push to GitHub

```
git add reports/{Company}/
git commit -m "Add {Company} checklist and verdict - {PASS/WATCH/AVOID}"
git push origin main
```

---

## The Six Gates

| Gate | What it checks |
|------|---------------|
| 1. Circle of Competence | Do I understand this business? |
| 2. Good Business | Is it profitable with strong cash flow? |
| 3. Moat | Does it have a durable competitive advantage? |
| 4. Management | Can I trust the people running it? |
| 5. Margin of Safety | Is the price low enough to buy safely? |
| 6. Decision Discipline | Am I buying for the right reasons? |

---

## The Verdict

| 🟢 PASS | Gates 1–4 strong AND price is at least 25% below base case value |
|---------|------------------------------------------------------------------|
| 🟡 WATCH | Gates 1–4 strong BUT price is too high right now |
| 🔴 AVOID | Any of Gates 1–4 failed OR a hard veto was triggered |

---

## Companies Screened So Far

| Company | Date | Verdict | Key Reason |
|---------|------|---------|------------|
| Apple (AAPL) | 2026-07-01 | 🟡 WATCH | Great business, no margin of safety at $287 |
| Google (GOOGL) | 2026-07-09 | 🟡 WATCH | Great business, thin margin of safety at $355 |
| Coca-Cola (KO) | 2026-07-17 | 🟡 WATCH | Wonderful business, razor-thin margin of safety at $81 |

---

## Disclaimer

This tool is for research and education only. It is not investment advice.
Always do your own research before making any financial decisions.

R-InvestIQ · Relanto · Built on AI-Berkshire (MIT License · xbtlin)
