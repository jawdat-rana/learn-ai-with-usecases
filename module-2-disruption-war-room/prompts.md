# Module 2 prompts: Disruption War-Room Copilot

Use these in order, in **one chat**. Text in `[square brackets]` is for you to
change. These are the prompts used to build the code and dashboard here.

---

## Prompt 1: Set up the war-room team

```text
You are my disruption war-room team. Play these five roles and label each
contribution with the role name:
- Logistics Lead: routes, carriers, port capacity, lead times
- Inventory Planner: stock cover, which products run out and when
- Customer Service Lead: which customers are hit and what we tell them
- Finance Analyst: cost of each option, margin at risk
- Devil's Advocate: challenges the others, looks for what we're missing

I'm the project manager running the war room. I can't code, so when we need
numbers, write and run code (or give me code to run in Google Colab) rather
than doing arithmetic in your head.

Here is the situation:
[paste Scenario 1 from scenarios.md]

First, each role: give me your top 2 questions before we look at any data.
```

---

## Prompt 2: Size the impact

*Attach `data/inventory.csv`.*

```text
Here is our product data (synthetic). Inventory Planner: for the products
that ship via Port Alpha, work out week by week which products run out and
when, if we do nothing. Assume:
- the port is closed weeks 1-3; nothing arrives through it in those weeks
- blocked containers wait in a backlog; after reopening the port releases
  one extra normal week of cargo per week on top of normal flow
- demand we can't meet is lost, not back-ordered
Use code. Before the results, list every assumption you made. Then show a
table: product, first week short, units short, margin lost.
```

---

## Prompt 3: Build the simulation (this produced `war_room.py`)

*Attach `data/response_options.csv` as well.*

```text
Write Python (pandas and matplotlib) that simulates this, for me to run in
Google Colab. I can't code, so use short numbered steps with plain-English
comments, and put the settings I might change (closure weeks, horizon) at
the top.

Model:
- 8 weeks, one row per product per week
- products shipping via Port Alpha: normal weekly inbound is blocked during
  the closure and added to a backlog; after reopening, normal inbound
  arrives plus up to one extra week of backlog per week
- domestic products are not affected
- each option in response_options.csv can take units OUT of the backlog:
  reroute from its start week at up to X% of weekly inbound, air freight
  (air-eligible products only) from its start week at up to Y%, with the
  extra cost per unit given. Air freight stops once rerouting starts.
  Never count a unit twice.
- demand not met is lost; margin lost = units short x unit margin
- allocation: either first come first served, or serve tier A demand first
  (tier_a_share_pct says how much of demand is tier A)

Output a comparison table per option and allocation rule: extra freight,
units short, lost margin, total cost, fill rate, tier A fill rate. Also a
table of which products run short under "do nothing", and a line chart of
total stock by week for each option with the closure shaded. Save the table
to output/option_comparison.csv.

Load the CSV files from
https://raw.githubusercontent.com/[your-github-username]/learn-ai-with-usecases/main/module-2-disruption-war-room/data/
if they're not found locally.
```

### Prompt 3b: Check the model

```text
Check your own simulation: for one product under option D, show me a
week-by-week table of backlog, arrivals by route, stock and shortfall.
Do total units arriving over 8 weeks plus the remaining backlog equal 8
weeks of normal inbound? If not, find the bug.
```

### Prompt 3c: Ask "what if" in plain English

```text
Change the code so [the port is closed for 4 weeks / rerouting starts in
week 4 / Port Beta can only take 50%]. Re-run it and tell me what changed
in the recommendation and why.
```

---

## Prompt 4: Compare the options

```text
Here are the simulation results:
[paste the comparison table]

Finance Analyst: rank the options on total cost.
Customer Service Lead: rank them on tier A service.
Logistics Lead: which is hardest to actually execute, and why?
Then summarise the trade-off in 3 sentences.
```

### Prompt 4b: Make them disagree

```text
Devil's Advocate: argue for the option that is NOT the cheapest. What would
have to be true (penalties, customer churn, back-orders instead of lost
sales) for it to be the better choice? Put rough numbers on the break-even.
```

---

## Prompt 5: Decision memo

```text
Write a one-page decision memo for the steering committee:
1. Recommendation in one sentence
2. Options compared (short table, using only the numbers above)
3. Why this option: cost, service, execution risk
4. What we're accepting by not choosing the others
5. What would change our mind, and when we'll review
6. Decisions needed today, with owner roles
Under 350 words, plain business English. Don't recalculate anything.
```

---

## Prompt 6: RAID log

```text
Create a RAID log (Risks, Assumptions, Issues, Dependencies) for executing
the recommended option. Table columns: type | description | impact
(H/M/L) | owner role | due date (week number) | mitigation or next step.
At least 4 entries of each type. Include the assumptions from our model.
Use the stakeholder list from the scenario.
```

## Prompt 7: Stakeholder messages

```text
Draft three short messages:
1. To tier A customers: what's happening, what we're doing, what they can
   expect, without promising dates we can't keep (under 120 words)
2. To the warehouse manager: the receiving surge in weeks 4-6 (under 100 words)
3. To finance: unbudgeted freight spend and why (under 100 words)
```

## Prompt 8: 30-day recovery plan

```text
Turn the recommendation into a 30-day recovery plan, week by week:
actions, owner role, decision points, and the metric we'll track each week.
Add a "trigger to escalate" for each week: what result would make us switch
options.
```

---

## Prompt 9: Build the what-if dashboard (this produced `war-room.html`)

```text
Create a single HTML file (HTML, CSS and plain JavaScript, no frameworks, no
build step) for GitHub Pages that runs exactly the same simulation in the
browser:
- loads ../module-2-disruption-war-room/data/inventory.csv and
  response_options.csv with fetch()
- sliders: closure weeks (1-6), week rerouted containers first arrive (1-6),
  Port Beta share (20-100%), air freight share (10-100%)
- a checkbox for "serve tier A first"
- headline tiles, the options comparison table with the lowest total cost in
  bold, a line chart of total stock by week with the closure shaded and a
  hover tooltip, and a per-product shortfall table with a tab per option
- a button that copies the results and a memo prompt to the clipboard
- works on a phone and in dark mode
Comment it in plain English. The numbers must match the Python version for
the default settings; tell me how to check that.
```
