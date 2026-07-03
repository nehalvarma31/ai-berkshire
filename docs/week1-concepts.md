# Week 1 Learning Note — Value Investing Concepts
**Nehal Varma Pericherla | Jun 29 – Jul 3, 2026**

---

## How I approached this week

I'll be honest — I came into this with basically zero background in finance. I'd heard of Buffett but never actually understood what value investing meant in practice. So this week was a lot of first-time moments.

Rather than just reading theory, I decided to learn everything through a real company — Apple. The idea was: if I can understand Apple's numbers, I can understand any company's numbers. Looking back, that was the right call.

---

## What I learned

### 1. Revenue — the starting point
Revenue is simply the total money a company collects from selling its products or services. For Apple in FY2025, that's $391 billion — from iPhones, Macs, iPads, and Services like the App Store and iCloud.

The first question I learned to ask: is revenue growing? Apple grew from ~$383B to ~$391B year over year. Modest, but it's a $391 billion base — growing that is genuinely hard.

---

### 2. Gross Margin — the first filter
After you earn revenue, you subtract the cost of making the product. What's left is gross profit.

**Gross Margin = Gross Profit ÷ Revenue**

Apple's gross margin is 46.91% overall — and 75% on Services. That Services number shocked me. It basically means for every $100 Apple earns from the App Store or iCloud, $75 is pure profit. That's not a product company, that's closer to a software business hiding inside a hardware brand.

---

### 3. Net Income — what actually stays
Even after gross profit, a company has salaries, R&D, marketing, taxes. What's left after all of that is net income — the real profit.

Apple's net income: $112 billion on $391 billion revenue. That's a 26.92% net margin. For every $100 Apple earns, it keeps $27. I looked up what's normal — grocery stores keep 1-3%, car companies 5-10%. Apple at 27% is exceptional, especially for a hardware company.

---

### 4. Free Cash Flow — Buffett's favourite number
This one surprised me the most. Net income can be manipulated through accounting. Free cash flow (FCF) is harder to fake — it's the actual cash that hits the company's account.

**FCF = Operating Cash Flow − Capital Expenditure**

Apple's FCF: $98.8 billion. That's nearly $100 billion in real cash generated in a single year. Buffett famously values businesses by their ability to generate cash over time, not by what their accounting says. After learning this, I understand why.

---

### 5. ROE — efficient or distorted?
Return on Equity measures how much profit a company generates per dollar of shareholder investment.

Apple's ROE is 151.9% — which sounds impossible. And in a way, it is misleading. Apple has spent ~$700 billion buying back its own shares over the past decade, which shrinks the equity base and makes ROE look astronomical. 

The lesson here wasn't the number — it was learning to ask *why* a number looks the way it does. High ROE sounds great until you understand what's driving it.

---

### 6. EPS and P/E — how investors price a company
EPS (Earnings Per Share) = Net Income ÷ Total Shares. Apple's EPS is $8.25.

P/E (Price-to-Earnings) = Stock Price ÷ EPS. At $287, Apple's P/E is ~34.8x.

This means investors are paying $34.80 for every $1 of Apple's earnings. Whether that's cheap or expensive depends entirely on how fast earnings are growing. Apple's revenue growth is ~6%, which makes 34x feel stretched.

---

### 7. Moat — the concept that changed how I see businesses
This was the biggest mindset shift of the week. Numbers tell you where a company is today. The moat tells you if it'll still be there in 10 years.

Buffett defines a moat as a sustainable competitive advantage — something that protects profits from competition. The five types are: brand/pricing power, switching costs, network effects, cost/scale advantages, and technology/patents.

Apple has switching costs (iCloud, iMessage lock-in) and brand (most valuable in the world). But the honest question the checklist asks is whether the moat is *widening or narrowing* — and for Apple, AI and regulation are genuinely nibbling at the edges. That's not obvious from the numbers alone.

---

### 8. Margin of Safety — the principle behind the checklist
This came from Benjamin Graham, Buffett's teacher. The idea is simple: never pay full price. Always buy at a discount to what the business is actually worth.

Running Apple through the three-scenario model:
- **Bull case** (strong AI growth): intrinsic value ~$380/share
- **Base case** (moderate growth): ~$260/share  
- **Bear case** (slowing growth): ~$180/share

At $287, Apple is above the base case. There's no margin of safety at current prices. This is actually why Buffett has been *selling* Apple — not because it's a bad business, but because the price doesn't offer enough cushion if you're wrong.

---

## The most important thing I learned

Running the Apple checklist, I expected the answer to be "buy Apple." It's a famous company, everyone knows it, the numbers look clean. But the checklist said no — not because Apple is a bad business (it's exceptional), but because the price is wrong.

That's the core lesson: **a great business at the wrong price is still a bad investment.**

Before this week, I didn't have a framework for thinking about that. Now I do.

---

## What I built this week

- Forked and set up the ai-berkshire repo on GitHub
- Ran the investment checklist on Apple — Chinese and English versions
- Translated 2 core skills into English (`investment-checklist-EN.md`, `investment-research-EN.md`)
- Documented all 18 skills in `docs/skill-map.md`
- Verified Apple's financial data using `tools/financial_rigor.py`

---

## What I want to understand better

- How analysts decide which growth rate to use in scenario models (the numbers feel somewhat arbitrary right now)
- How to evaluate moats in industries I'm less familiar with — Apple is easy because I use the products
- When Buffett says "circle of competence" — how do you honestly define the boundary of what you know?

---

*Next: Week 2 — designing a standardized English report template for R-InvestIQ.*
