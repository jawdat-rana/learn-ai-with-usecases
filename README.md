# Learn AI with use cases: AI for supply chain leaders

A free, hands-on course for **senior project managers and supply chain
professionals who don't code**. You'll use free AI tools on realistic
(synthetic) supply chain problems and leave with work you could show your
leadership team.

> **The big idea:** you don't need to know how to program. You think of the
> use case and describe it well. The AI writes the code, explains it and fixes
> it. Your job is the part AI can't do: judging whether the answer is right.

**Website:** [jawdat-rana.github.io/learn-ai-with-usecases](https://jawdat-rana.github.io/learn-ai-with-usecases/)
(your own copy gets its own address)

---

## How it works

1. **Copy the course** into your own free GitHub account and switch on your
   own website. → [START-HERE.md](START-HERE.md) (15 minutes, no installing)
2. **Learn the foundations** in three short lessons.
3. **Do the two flagship projects** with a free AI tool (Claude, ChatGPT or
   Gemini). Every step has a copy-paste prompt.
4. **Run the code without coding:** in the AI chat, or in Google Colab with
   one click.
5. **Publish** interactive dashboards on your own GitHub Pages site.
6. **Keep a journal** of what worked and where the AI was wrong.

No paid subscriptions needed. All data is synthetic, so it's safe to upload
anywhere.

## The course

### Foundations (30 minutes)

1. [How AI chat tools work, in 10 minutes](00-foundations/01-how-ai-works.md):
   what they're good and bad at, and what never to paste in
2. [Prompting for senior professionals](00-foundations/02-prompting-for-leaders.md):
   the Role, Context, Task, Format, Checks pattern
3. [You don't need to code (but you'll use code)](00-foundations/03-you-dont-need-to-code.md):
   how to get AI to write, run, explain and fix code for you

### Flagship projects

| | Project | You'll produce | AI skills you'll learn |
|---|---|---|---|
| 1 | [**Supplier Risk Radar**](module-1-supplier-risk-radar/README.md) | Risk scores for 30 suppliers, a heatmap, a mitigation plan, an exec one-pager | Analysing a data file, scoring with a rubric, turning news into data, checking the AI's maths |
| 2 | [**Disruption War-Room Copilot**](module-2-disruption-war-room/README.md) | A what-if simulation of a port closure, an options comparison, a decision memo, RAID log and 30-day plan | Role prompting, scenario analysis, traceable assumptions, pushing back on the AI |

Each project has:

- `prompts.md`: every prompt, including **the prompts that generated the code**
- `analysis/*.py` and `*.ipynb`: the Python the AI wrote, runnable in Google Colab
- an interactive dashboard (HTML and JavaScript) on your GitHub Pages site
- a **"Where AI is wrong"** section, because senior people need to trust AI carefully, not blindly

### Prompt kits (reuse every week)

| Kit | For |
|---|---|
| [Steering committee transcript → decisions, owners, risks](prompt-kits/steerco-transcript-to-decisions.md) | Any meeting with a transcript or messy notes |
| [Contract and SLA risk review](prompt-kits/contract-sla-review.md) | Supplier, 3PL and service contracts |
| [Demand forecast sanity check](prompt-kits/demand-forecast-sanity-check.md) | Before S&OP, or when a forecast feels off |
| [Project plan stress test](prompt-kits/project-plan-stress-test.md) | Critical path and dependency risks before a go/no-go |

### Part 2 (advanced): skills, agents and AI teams

[Part 2](part-2-advanced/README.md) is a bonus for when you've finished the
above: package your method as a reusable **skill**, run an **agent team** by
hand, then build a real Planner → Analyst → Reviewer team of agents in Google
Colab with a free API key.

### Keep going

- [The 10 challenges](challenges.md): tick them off as you go
- [My AI journal](my-ai-journal.md): edit it in your browser after each session

---

## What's in the repository

```text
START-HERE.md                 Set up GitHub, your copy and your website
00-foundations/               Three short lessons
module-1-supplier-risk-radar/ Flagship project 1: data, prompts, Python, example output
module-2-disruption-war-room/ Flagship project 2: data, scenarios, prompts, Python
prompt-kits/                  Four reusable prompts with synthetic samples
part-2-advanced/              Skills, agents and AI teams (bonus)
dashboards/                   Interactive HTML/JavaScript dashboards for GitHub Pages
index.html, assets/           The course website
challenges.md, my-ai-journal.md
```

## A word on data and safety

- Everything here is **synthetic**. Company and product names are made up.
- Your copy of the course is **public**. Never commit company data to it.
- At work, use only AI tools your company has approved, and follow its data
  policy. Free consumer AI tools may keep what you paste.
- AI output is a draft. You're accountable for what you send.

---

## For the course owner

To let friends copy the course with **Use this template**, open this
repository's **Settings → General** and tick **Template repository**. To
publish the original course website, go to **Settings → Pages** and deploy
from the `main` branch, `/ (root)` folder.
