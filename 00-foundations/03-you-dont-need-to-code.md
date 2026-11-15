# 3. You don't need to code (but you'll use code)

This is the most important idea in the course.

> **You think of the use case. The AI writes the code, explains it and helps
> you fix it. Your job is to judge whether the answer makes sense.**

Throughout the course you'll see two languages:

- **Python** for analysis: scoring suppliers, simulating stock, checking a
  forecast. You run it in Google Colab or let the AI run it.
- **HTML and JavaScript** for web pages: the interactive dashboards on your
  own GitHub Pages website.

You don't need to learn either. Every piece of code in this repository sits
next to **the plain-English prompt that produced it**, so you can see that the
skill is describing the problem well, not typing code.

## The loop

```text
 1. Describe what you want     →  "Score each supplier 1-25 using this rubric..."
 2. AI writes the code         →  you don't read every line
 3. Run it                     →  in the AI chat, or Colab: Runtime → Run all
 4. Ask it to explain          →  "Explain this like I'm new to the team"
 5. Check the result           →  does one row match what you'd expect by hand?
 6. Ask for changes in English →  "Now also flag suppliers with no alternates"
```

## How to run Python without installing anything

**Option A: let the AI run it.** Many AI tools, including some free plans, can
run Python in the chat. You'll see a step like "Analyzing" or "Running code".
Attach the CSV and ask it to run the code.

**Option B: Google Colab** (free, needs any Google account).

1. Open a module's notebook link, for example
   [Supplier risk notebook in Colab](https://colab.research.google.com/github/jawdat-rana/learn-ai-with-usecases/blob/main/module-1-supplier-risk-radar/analysis/supplier_risk.ipynb).
2. Click **Runtime → Run all**. If Colab warns that the notebook is from
   GitHub, click **Run anyway**: the code only reads the sample data.
3. Scroll down to see tables and charts appear.
4. To run code an AI gave you: **File → New notebook**, paste the code into
   the grey box, and press the ▶ button.

## When it breaks (it will, and that's fine)

Copy the **whole** red error message into the AI and say:

```text
I ran your code and got this error. Explain in plain English what went
wrong and give me the corrected full code.
[paste error]
```

Nine times out of ten that's all it takes. If the same error comes back
twice, ask: "Let's try a simpler approach: what's the smallest version of
this that works?"

## How to check code you can't read

You don't need to read code to check it. You need to check **results**.

- **Spot check:** pick one row and work it out by hand or in Excel. Does it
  match?
- **Sense check:** do the totals look like the right order of magnitude?
- **Edge check:** what happens to the row with missing data?
- **Second opinion:** paste the code into a *different* AI tool and ask
  "What could be wrong with this code? Does it do what this description
  says?"
- **Two versions agree:** in this course, the Python and the JavaScript
  dashboard implement the same logic and produce the same numbers. That's a
  strong check.

## How to publish a web page without coding

1. Ask the AI for "a single HTML file with no frameworks for GitHub Pages".
2. If the AI shows a preview, check it works there.
3. In your GitHub repository, go to the `dashboards` folder, click
   **Add file → Create new file**, name it (for example `my-page.html`),
   paste the code and click **Commit changes**.
4. A minute later it's live at
   `https://YOUR-USERNAME.github.io/learn-ai-with-usecases/dashboards/my-page.html`.

**Next:** [Module 1: Supplier Risk Radar](../module-1-supplier-risk-radar/README.md)
