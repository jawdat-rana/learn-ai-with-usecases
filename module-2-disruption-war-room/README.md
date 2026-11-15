# Module 2: Disruption War-Room Copilot

> **The situation:** "Port Alpha has just closed for three weeks. Nine of our
> twelve products ship through it. The steering committee meets at 4pm and
> wants options, costs and a recommendation."

You will use a free AI chat tool as a small analyst team. It works out which
products run short and when, compares four response options on cost and
service, writes the decision memo, and drafts the RAID log, stakeholder
messages and a 30-day recovery plan. The simulation behind the numbers is a
Python program the AI writes for you, and you can play with an interactive
version on your own website.

**Time:** 90 minutes · **You need:** a free account on Claude, ChatGPT or Gemini
· **Data:** synthetic, safe to upload anywhere · **Best done after** [Module 1](../module-1-supplier-risk-radar/README.md)

| What you get at the end | Where it lives |
|---|---|
| Week-by-week stock forecast for 12 products | Python output, and [the live war-room dashboard](https://jawdat-rana.github.io/learn-ai-with-usecases/dashboards/war-room.html) |
| Side-by-side comparison of 4 response options | [output/option_comparison.csv](output/option_comparison.csv) (example) |
| A one-page decision memo | Your AI chat, then [your journal](../my-ai-journal.md) |
| RAID log, stakeholder messages and a 30-day recovery plan | Your AI chat |

---

## The files

| File | What it is |
|---|---|
| [scenarios.md](scenarios.md) | The scenario brief, plus two more scenarios to practise on |
| [data/inventory.csv](data/inventory.csv) | 12 products: stock, weekly demand, inbound volume, margin, share of tier A customers, whether they can fly |
| [data/response_options.csv](data/response_options.csv) | 4 options: do nothing, reroute via Port Beta, air freight, or both |
| [data/scenario.csv](data/scenario.csv) | The scenario settings in plain English |
| [prompts.md](prompts.md) | **Every prompt used, in order** |
| [analysis/war_room.py](analysis/war_room.py) | The simulation the AI wrote |
| [analysis/war_room.ipynb](analysis/war_room.ipynb) | The same code as a notebook. [Open it in Google Colab](https://colab.research.google.com/github/jawdat-rana/learn-ai-with-usecases/blob/main/module-2-disruption-war-room/analysis/war_room.ipynb) |
| [../dashboards/war-room.html](../dashboards/war-room.html) | The interactive what-if dashboard ([see it live](https://jawdat-rana.github.io/learn-ai-with-usecases/dashboards/war-room.html)) |

---

## The steps

The prompts are in [prompts.md](prompts.md). Use one chat for the whole module.

### Step 1: Set up your war-room team

**Prompt 1** asks the AI to play five roles: logistics lead, inventory
planner, customer service lead, finance analyst and a devil's advocate. Role
prompting gets you different angles on one problem instead of one generic
answer. Read [scenarios.md](scenarios.md) and paste Scenario 1 in.

### Step 2: Size the impact

Upload `inventory.csv` and use **Prompt 2**. The AI should work out which
products run out and in which week. **Insist that it uses code to calculate**,
not mental arithmetic. Ask it to list its assumptions before you look at the
numbers.

### Step 3: Have the AI build the simulation

**Prompt 3** is the prompt that produced
[war_room.py](analysis/war_room.py). It simulates every product week by week
under each option. Run it in your AI chat if it can run code, or in
[Google Colab](https://colab.research.google.com/github/jawdat-rana/learn-ai-with-usecases/blob/main/module-2-disruption-war-room/analysis/war_room.ipynb)
(**Runtime → Run all**). Then ask "what if": change `CLOSURE_WEEKS` to 4, or
ask the AI to change the code so rerouting starts in week 4.

### Step 4: Compare the options and push back

Use **Prompt 4** to get the trade-off table, then **Prompt 4b** to make each
role argue for a different option. A good war room disagrees before it
decides.

### Step 5: Write the decision memo

**Prompt 5** turns the numbers into a one-page memo for the steering
committee: recommendation, trade-offs, risks and what you'd need to believe
for a different option to win. The dashboard has a **Copy results for AI
memo** button that copies the current numbers and this prompt in one go.

### Step 6: RAID log, stakeholder messages, 30-day plan

**Prompts 6, 7 and 8** produce the project management artefacts you'd
normally spend an evening on. Treat them as a first draft: names, dates and
owners are yours to fill in.

### Step 7: Publish your what-if dashboard

**Prompt 9** is the prompt behind [war-room.html](../dashboards/war-room.html).
It's already on your GitHub Pages site. Move the sliders in the meeting and
the numbers update live.

---

## Check your answers

With the default settings (3-week closure, reroute from week 3 at 80% of
volume, air freight up to 50%, serve tier A first):

| Option | Extra freight | Units short | Lost margin | Total cost | Fill rate | Tier A fill |
|---|---:|---:|---:|---:|---:|---:|
| A. Do nothing | $0 | 4,850 | $139,750 | $139,750 | 95.5% | 95.3% |
| B. Reroute via Port Beta | $50,120 | 960 | $27,380 | **$77,500** | 99.1% | 99.8% |
| C. Air freight critical SKUs | $99,400 | 1,400 | $19,800 | $119,200 | 98.7% | 99.5% |
| D. Reroute plus air | $92,365 | 40 | $1,000 | $93,365 | 100.0% | 100.0% |

**The interesting part:** B is cheapest overall, but D protects almost every
sale for about $16k more. Which is right depends on things that aren't in
the data: how angry tier A customers get, contract penalties, and whether a
lost sale is really lost or just late. That's the conversation the war room
should have, and the AI can't settle it for you.

If you switch off "serve tier A first", total cost doesn't change but tier A
fill under "Do nothing" drops from 95.3% to 93.0%. Same stock, different
customers disappointed.

---

## Where AI is wrong (read this before using it at work)

1. **Hidden assumptions decide the answer.** Whether short demand is lost or
   back-ordered changes the cost of "do nothing" a lot. AIs pick one silently.
   Always ask: "List every assumption you made, and which one matters most."
2. **Double counting.** A common mistake in simulations like this is to count
   rerouted containers twice: once at Port Beta and again when Port Alpha
   reopens. The numbers look great and are wrong. Ask the AI to reconcile: "Do
   total units arriving match total units shipped by suppliers?"
3. **Made-up rates sound precise.** If you don't give it freight rates, it
   will invent "$4.20 per unit" with total confidence. Give it your numbers,
   or ask it to show results across a range.
4. **Role-play experts agree too politely.** Five "experts" written by one
   model often reach the same view. Make the devil's advocate argue for a
   specific different option and say what would have to be true.
5. **It forgets constraints.** Ask for "more rerouting" and it may assume
   Port Beta has unlimited space. Restate the limits when you change the
   question.
6. **It doesn't know today's news.** A free AI may not know what is actually
   happening at a real port today. Use it to reason about scenarios, and get
   live facts from your forwarder.
7. **The memo is more confident than the model.** Ask it to add a "what
   would change our mind" section. If it can't write one, the analysis isn't
   finished.

## Taking this to work

- Use only AI tools your company approves, and anonymise data (product codes,
  rounded volumes) if you have to use a public tool.
- Start with the **prompts**, not the code: a good scenario brief and role
  prompt is useful the first time you're in a real war room.
- Keep [war_room.py](analysis/war_room.py) as a template. Ask the AI to adapt
  it: "Change this so each product has its own supplier lead time" or "Add a
  second disrupted port".
