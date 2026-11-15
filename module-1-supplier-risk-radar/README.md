# Module 1: Supplier Risk Radar

> **The question:** "Which of our suppliers could hurt us most, and what should
> we do about it this quarter?"

You will use a free AI chat tool to turn a supplier spreadsheet and a handful
of news stories into a risk score for every supplier, a heatmap, a mitigation
plan and a one-page summary for your leadership team. You will not write any
code yourself. The AI writes it, explains it, and runs it (or you run it in
Google Colab with one click).

**Time:** 60 to 90 minutes · **You need:** a free account on Claude, ChatGPT or
Gemini · **Data:** synthetic, so it is safe to upload anywhere

| What you get at the end | Where it lives |
|---|---|
| A risk score (1 to 25) for 30 suppliers | Your AI chat, and [the live dashboard](https://jawdat-rana.github.io/learn-ai-with-usecases/dashboards/supplier-risk.html) |
| A likelihood × impact heatmap | The dashboard on your own GitHub Pages site |
| A mitigation plan with owners and dates | Your AI chat, pasted into [your journal](../my-ai-journal.md) |
| An exec one-pager | [output/one_pager.md](output/one_pager.md) (example) |

---

## The files

| File | What it is |
|---|---|
| [data/suppliers.csv](data/suppliers.csv) | 30 made-up suppliers: spend, category share, region, lead time, on-time %, financial health, single-source flag |
| [data/news-snippets.md](data/news-snippets.md) | 8 made-up news stories. Some matter, some don't, one is a trap |
| [prompts.md](prompts.md) | **Every prompt used in this module, in order.** Copy and paste them |
| [analysis/supplier_risk.py](analysis/supplier_risk.py) | The Python the AI wrote in Step 3 |
| [analysis/supplier_risk.ipynb](analysis/supplier_risk.ipynb) | The same code as a notebook. [Open it in Google Colab](https://colab.research.google.com/github/jawdat-rana/learn-ai-with-usecases/blob/main/module-1-supplier-risk-radar/analysis/supplier_risk.ipynb) |
| [../dashboards/supplier-risk.html](../dashboards/supplier-risk.html) | The interactive dashboard the AI built in Step 6 ([see it live](https://jawdat-rana.github.io/learn-ai-with-usecases/dashboards/supplier-risk.html)) |

---

## The steps

Each step has a ready-made prompt in [prompts.md](prompts.md). Keep everything
in **one chat** so the AI remembers what came before.

### Step 1: Ask the AI to understand the data before it analyses anything

Upload `suppliers.csv` and use **Prompt 1**. A good AI answer describes each
column in plain English and points out problems. **It should notice that
Torque Precision (S20) has no lead time.** If it doesn't, ask: "Are there any
missing values?" This is the habit that matters most: make the AI look at the
data before it draws conclusions.

### Step 2: Agree the scoring rubric together

Use **Prompt 2**. The AI proposes how to score risk. Your job is to push back,
because you know supply chains and it doesn't know your business. Ask why
lead time matters as much as financial health. Ask what it would do with
missing data. The rubric this course settled on is below.

### Step 3: Have the AI write the code and run it

Use **Prompt 3**. This is the moment the course is about: you described what
you want in plain English and the AI writes a program for it. Then:

- **If your AI can run code** (it shows a "running code" or "analysis" step),
  let it run and show you the results.
- **If it can't**, open the notebook in
  [Google Colab](https://colab.research.google.com/github/jawdat-rana/learn-ai-with-usecases/blob/main/module-1-supplier-risk-radar/analysis/supplier_risk.ipynb),
  sign in with any Google account, and press **Runtime → Run all**. Nothing to
  install.

Then use **Prompt 3b** to make the AI explain the code to you like you are a
new team member. You should be able to say what each step does, even if you
couldn't write it.

### Step 4: Turn news into data

Paste the contents of `news-snippets.md` and use **Prompt 4**. The AI reads
eight stories and says which suppliers each one affects. This is AI's real
superpower: turning messy text into structured data. **Check every match.**
Story 6 is about "Northwind Circuit Solutions", which is *not* our supplier
Northwind Circuits. Many AIs get this wrong.

### Step 5: Draft the mitigation plan

Use **Prompt 5**. For each high-risk supplier you get actions such as
qualifying a second source, holding buffer stock or adding contract terms,
with an owner, a date and a rough cost. Push back with **Prompt 5b** ("which
of these would you cut if I only had budget for two?").

### Step 6: Build the dashboard and the one-pager

Use **Prompt 6** to ask for a web page dashboard, and **Prompt 7** for the
exec one-pager. The finished dashboard is already in this repository at
[dashboards/supplier-risk.html](../dashboards/supplier-risk.html), and it is on
your GitHub Pages site once you switch Pages on (see
[START-HERE.md](../START-HERE.md)). The original is [live here](https://jawdat-rana.github.io/learn-ai-with-usecases/dashboards/supplier-risk.html); yours
will be at `https://YOUR-USERNAME.github.io/learn-ai-with-usecases/dashboards/supplier-risk.html`.

---

## The rubric, in plain English

Every factor gets a score from 1 (low risk) to 5 (high risk).

**Likelihood: how likely is a problem?** (average of four scores)

| Factor | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| Region risk (given in the data) | 1 | 2 | 3 | 4 | 5 |
| Financial health (5 = strong) | 5 | 4 | 3 | 2 | 1 |
| On-time delivery | 95%+ | 90-94% | 85-89% | 80-84% | under 80% |
| Lead time (days) | up to 14 | 15-30 | 31-45 | 46-60 | over 60, or missing |

**Impact: how much would it hurt?** (average of three scores)

| Factor | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| Annual spend | under $0.5M | $0.5-1M | $1-2M | $2-4M | $4M+ |
| Share of its category's spend | under 10% | 10-24% | 25-39% | 40-59% | 60%+ |
| Can we switch? | 3+ qualified alternates | 2 | 1 | 0 alternates | single source |

**Risk = likelihood × impact** (1 to 25). High is 15 or more, Medium is 8 to 14,
Low is 7 or less. A supplier named in a relevant news story gets +1 likelihood.

---

## Check your answers

If your numbers differ, that's fine as long as you can explain why. If you
used the rubric above you should see:

- **4 high-risk suppliers:** Voltaria Cells (25), Northwind Circuits (20),
  Ampere Storage (16), Nimbus Semicon (15). Together $15.3M, 29% of spend.
- **Single-source spend:** $13.75M, 26% of total spend of $52.0M.
- **Data gap:** Torque Precision has no lead time, so it is scored as worst case.
- **Most concentrated categories:** Specialty chemicals (Sable, 70%) and
  Batteries (Voltaria, 66%, single source).

---

## Where AI is wrong (read this before using it at work)

These are real failure patterns. Watch for each one in your own chat.

1. **Name confusion.** Story 6 is about a different company with a similar
   name. AI matches on words, not on facts. Always check entity matches.
2. **Good news read as bad, or the other way round.** Kestrel's new aerospace
   contract (story 4) could mean more capacity *or* that we become a smaller
   customer who loses priority. The AI often picks one reading confidently. Ask
   it to argue both.
3. **Maths done "in its head".** If the AI works out totals in plain text rather
   than by running code, it can be wrong by a lot. Ask it to calculate with
   code, or check one or two numbers yourself.
4. **Invented thresholds sound official.** The rubric above is a judgement
   call. If the AI says "industry standard is 95% on-time", ask for a source.
   It often has none.
5. **Missing data quietly filled in.** Some AIs replace blanks with an average
   without telling you. Always ask "how did you handle missing values?"
6. **Made-up alternative suppliers.** Ask for dual-sourcing options and it may
   name real-sounding companies that don't exist, or real ones that don't make
   the part. Use it for the *type* of alternative, never the name.
7. **It agrees with you too easily.** Ask "what would make this ranking
   wrong?" A good analyst answers that question; make the AI do it too.

## Taking this to work

- Use only the AI tools your company has approved, and follow its data policy.
  Free consumer tools may keep or learn from what you paste.
- If you can't upload real data, **anonymise** it: replace supplier names with
  IDs and round spend. The method works the same.
- The [dashboard](https://jawdat-rana.github.io/learn-ai-with-usecases/dashboards/supplier-risk.html) lets you load your own CSV.
  The file is read on your computer and nothing is uploaded.
- Next step for a real team: agree the rubric with procurement and finance
  first. The scores are only as good as that conversation.
