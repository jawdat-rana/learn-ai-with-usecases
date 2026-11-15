# Module 1 prompts: Supplier Risk Radar

Copy each prompt into your AI chat in order, in **the same chat**. Text in
`[square brackets]` is for you to change. These are the actual prompts used to
build the code and dashboard in this module.

Works in the free versions of Claude, ChatGPT and Gemini. Free plans have
daily limits, so if you hit one, wait a few hours or switch tools and paste
your earlier results back in.

---

## Prompt 1: Understand the data first

*Attach `data/suppliers.csv` before sending.*

```text
You are a senior supply chain analyst helping me, a project manager who does
not code.

I've attached a supplier list (synthetic data for training). Before any
analysis:
1. Explain each column in plain English, one line each.
2. Tell me how many suppliers, categories and regions there are.
3. Check the data quality: missing values, odd values, anything that doesn't
   add up (for example, category shares that don't sum sensibly).
4. List 3 questions about supplier risk this data CAN answer and 2 it CANNOT.

Keep it short and use tables where helpful.
```

**What good looks like:** it spots that S20 Torque Precision has no lead time,
and it says the data cannot tell you about things like quality defects or
contract terms.

---

## Prompt 2: Agree a scoring rubric

```text
I want to score each supplier's risk as LIKELIHOOD (1-5) x IMPACT (1-5),
giving 1-25.

Propose a simple rubric using only the columns in this file:
- which columns feed likelihood and which feed impact, and why
- the thresholds that turn each column into a 1-5 score
- how to treat missing data
- what counts as High, Medium and Low

Show it as two tables. Then tell me the 2 weakest assumptions in your rubric.
Don't calculate anything yet.
```

**Your job:** argue with it. Try: *"Why does lead time matter as much as
financial health?"* or *"Treat missing data as worst case and flag it, so
people fix the data."* Agree the final rubric before moving on. The one this
course used is in the [module README](README.md#the-rubric-in-plain-english).

---

## Prompt 3: Have the AI write the code

This is the prompt that produced [analysis/supplier_risk.py](analysis/supplier_risk.py).

```text
Write Python code (pandas and matplotlib) that applies the rubric we agreed
to the attached file. I will run it in Google Colab, and I can't code, so:

- Split it into short numbered steps with a plain-English comment above each.
- Load the CSV from this URL if no local file is found:
  https://raw.githubusercontent.com/[your-github-username]/learn-ai-with-usecases/main/module-1-supplier-risk-radar/data/suppliers.csv
- Step 1: load and preview the data.
- Step 2: score every supplier, calculate likelihood, impact, risk and tier,
  and flag rows with missing data.
- Step 3: for each category, show the biggest supplier's share and whether it
  is single source. Print total single-source spend.
- Step 4: draw a 5x5 heatmap (likelihood across, impact up) with supplier IDs
  in the cells and red/amber/green zones.
- Step 5: write a short markdown one-pager with the headline numbers and the
  High-risk suppliers, and save it to output/one_pager.md.

If you can run code, run it and show me the results. If not, tell me exactly
how to run it in Colab.
```

### Prompt 3b: Make it explain the code

```text
Explain this code to me as if I'm a new team member who has never
programmed. For each step: what it does, why it's needed, and one thing I
could change to ask a different question. No jargon, or explain it when you
use it.
```

### If something breaks

```text
I ran the code and got this error:
[paste the whole red error message]
What does it mean, in plain English, and what exactly should I change?
```

---

## Prompt 4: Turn news into data

*Paste the full text of `data/news-snippets.md` after this prompt.*

```text
Here are 8 news snippets. For each one, tell me:
- which supplier(s) in my file it affects, if any, with the supplier_id
- whether it raises risk, lowers it, or is unclear, and why in one sentence
- how confident you are (high/medium/low)

Be strict about names: only match a supplier if the name really is the same
company. Then give me a dictionary I can paste into the code, in the form
{"S06": "short reason", ...}, containing only the stories that raise risk.

[paste news snippets here]
```

**Check:** story 6 should *not* match Northwind Circuits (S01). Story 7 should
match all three battery suppliers (S06, S14, S22); check the code and decide
whether S06 needs a second flag. If the AI got any of this wrong, tell it so
and ask why it made the mistake.

---

## Prompt 5: Draft the mitigation plan

```text
Re-run the scores with the news flags (+1 likelihood, capped at 5).
For every High-risk supplier, propose a mitigation plan as a table:
risk | action | owner (role, not a name) | first step this month |
rough cost (low/medium/high) | how we'll know it's working.

Use a mix of actions: dual sourcing, safety stock, contract terms, closer
monitoring, design changes. Don't invent supplier names: describe the type
of alternative instead.
```

### Prompt 5b: Force a trade-off

```text
I only have budget for two of these actions this quarter. Which two, and
why? What risk am I knowingly accepting by not doing the rest?
```

---

## Prompt 6: Build the dashboard

This is the prompt behind [dashboards/supplier-risk.html](../dashboards/supplier-risk.html).

```text
Create a single HTML file (HTML, CSS and plain JavaScript, no frameworks, no
build step) for GitHub Pages that:
- loads ../module-1-supplier-risk-radar/data/suppliers.csv with fetch()
- applies exactly the same rubric as the Python code
- shows 4 headline tiles: suppliers, high-risk count and spend, single-source
  count and spend, rows with data gaps
- shows a 5x5 heatmap with supplier IDs; hovering shows the detail
- shows a bar for each category's biggest supplier share
- shows a sortable table of all suppliers
- has a checkbox to switch the news flags on or off
- lets me load my own CSV with the same columns, read only in the browser
- works on a phone and in dark mode
Add short comments in plain English so a non-coder can follow it.
```

If you can, open the result in the AI's preview window. Then add it to your
repository: on GitHub, open the `dashboards` folder, click **Add file →
Create new file**, name it, paste the code and commit.

---

## Prompt 7: The exec one-pager

```text
Write a one-page summary for our VP of Supply Chain:
- 3-line headline: what we found and what we recommend
- top risks in a short table
- the 2 actions we're funding this quarter and the risk we're accepting
- data gaps we must close before the next review
Plain business English, no jargon, under 300 words. Use only numbers that
came from the code output; don't recalculate anything yourself.
```

---

## Bonus: challenge the AI

```text
Play devil's advocate. Give me the 3 strongest reasons this risk ranking
could be wrong or misleading, and what extra data would fix each one.
```
