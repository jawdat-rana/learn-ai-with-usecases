# Exercise 2: Run an agent team by hand (no code)

**Goal:** understand how a team of AI agents works by **being the
orchestrator yourself**. You'll open three chats, give each one a role, and
pass work between them. This is exactly what the code in
[exercise 3](exercise-3-agent-team-in-colab.md) automates.

**Scenario:** Module 2's Port Alpha closure, but this time the brief is
uncertain: the closure might be 2 to 5 weeks, and Port Beta might take only
50% of our volume.

## Set up three chats

Open three separate chats (they can be in different AI tools, which is even
better, because different models catch different mistakes). Paste one of
these at the start of each.

### Chat 1: Planner

```text
You lead a supply chain disruption war room. I'll give you a brief. Turn it
into an analysis plan: 3 to 5 scenarios to test, each with exact settings
for: closure weeks, week rerouted containers first arrive, Port Beta share
(%), air freight share (%). Include a base case and pessimistic cases. Say
what question each scenario answers. Don't invent results. Later I'll bring
you an approved report and ask for the final memo.
```

### Chat 2: Analyst

```text
You are a supply chain analyst. I'll give you a plan with scenarios. I will
run each scenario in a simulation and paste the results to you. Your job is
to compare them: which option is cheapest in each scenario, which is most
robust across all of them, and what the trade-offs are. Copy numbers exactly
and never estimate a number yourself.
```

### Chat 3: Reviewer

```text
You are a sceptical reviewer. I'll give you an analyst's report plus the raw
simulation results it is based on. Check: every number in the report
appears in the raw results; every planned scenario was run; the conclusion
follows from the numbers; assumptions are stated. Reply APPROVED, or REVISE
with a numbered list of specific fixes.
```

## Run the team

1. **Planner:** paste the brief:

   ```text
   Port Alpha has closed; expected 3 weeks, could be 2 to 5. Rerouted
   containers via Port Beta arrive from week 3 (maybe week 4) at up to 80% of
   volume (maybe only 50%). We can fly up to 50% of weekly volume for five
   air-eligible products. Tier A customers have penalty clauses. We need a
   recommendation that holds up if our assumptions are wrong.
   ```

2. **You are the tool:** for each scenario in the plan, set the sliders on
   your **war-room dashboard** (`dashboards/war-room.html` on your GitHub Pages
   site), click **Copy results for AI memo**, and paste the results into a
   notes file. Label each one with its scenario.
3. **Analyst:** paste the plan and all the results.
4. **Reviewer:** paste the analyst's report *and* the raw results.
5. If the Reviewer says REVISE, paste its feedback to the Analyst, then send
   the new report back to the Reviewer. **Stop after one revision.**
6. **Planner:** paste the approved report and ask for a 300-word steering
   committee memo.

## Debrief questions (write the answers in your journal)

- Did the Reviewer catch anything? Would you have caught it?
- Which option was most robust across scenarios, not just cheapest in the
  base case? (Hint: try "rerouting from week 4 at 50%" and look at option B.)
- Where did you, as orchestrator, add judgement the agents couldn't?
- What would you **never** let an agent do without your approval at work?

## What you just learned

A team of agents is: **roles** (instructions), **tools** (the simulation),
**hand-offs** (you copying between chats), a **check** against evidence (the
Reviewer reading raw results), and a **stop rule** (one revision). In
exercise 3, Python does the copying.
