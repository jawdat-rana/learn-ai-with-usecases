# Kit 3: Demand forecast sanity check

**Use it when:** before S&OP, or when a forecast "feels off" and you want a
quick, independent check without waiting for the planning team.

**Try it with:** [samples/monthly-sales.csv](samples/monthly-sales.csv), with
3 years of monthly sales for two products plus a planner's 6-month forecast.
There's a one-off promotion in the history and one forecast month that
doesn't look right.

**The code the AI wrote:** [samples/forecast_check.py](samples/forecast_check.py) ·
[run it in Google Colab](https://colab.research.google.com/github/jawdat-rana/learn-ai-with-usecases/blob/main/prompt-kits/samples/forecast_check.ipynb)

## The prompt

*Attach the sales CSV.*

```text
You are a demand planning analyst. I'm not a statistician and I can't code.
Attached are monthly actual sales and a planner's forecast.

1. Describe the history in plain English: trend, seasonality, anything
   unusual. Use code to calculate, and show a chart.
2. Flag any months in the history that look like one-offs (promotions,
   stock-outs, data errors) and explain how you'd treat them.
3. Build a simple, explainable baseline: same month last year, adjusted for
   growth over the last 12 months, with one-off months cleaned out.
4. Compare the planner's forecast with the baseline month by month. Flag any
   gap above 20% and suggest what question I should ask the planner.

Write the Python so I could re-run it in Google Colab, with plain-English
comments, and explain the method in 5 lines a VP would understand.
```

## What good looks like (for the sample)

- **July 2024 for the smart plug** is flagged as a one-off (about 15,900 units
  against about 8,500 around it) and cleaned out of the baseline.
- **March 2026 for the smart thermostat** is flagged: the planner forecast is
  about 43% above the baseline. The right question is "what do you know that
  the history doesn't?": a promotion, a new customer, or a typo.
- Everything else is within a few percent of the baseline.

## Where AI is wrong

- **A simple baseline isn't a better forecast.** It's a sense check. The
  planner may know about a launch or a lost customer. Use the gaps to start
  a conversation, not to overrule anyone.
- **AIs love complex models.** If it suggests something sophisticated,
  ask: "Would a simpler method be almost as good, and easier to explain?"
- **Over-cleaning.** Remove too many "outliers" and you remove real demand.
  Ask it to show what it removed.
- **Calendar effects.** Easter, Ramadan, Chinese New Year and trading days
  move between months. A free AI won't account for them unless you tell it.
