# Kit 4: Project plan stress test

**Use it when:** before a go/no-go, a steering committee or a re-plan, and
you want to know where the plan will really break.

**Try it with:** [samples/project-plan.csv](samples/project-plan.csv), a
fictional warehouse-system go-live plan (it goes well with the
[steerco transcript](samples/steerco-transcript.txt) from Kit 1).

**The code the AI wrote:** [samples/critical_path.py](samples/critical_path.py) ·
[run it in Google Colab](https://colab.research.google.com/github/jawdat-rana/learn-ai-with-usecases/blob/main/prompt-kits/samples/critical_path.ipynb)

## The prompt

*Attach the project plan CSV (or export your plan from MS Project, Smartsheet
or Excel as CSV).*

```text
You are a senior programme manager doing a pre-go-live stress test.
Attached is the plan: task, owner, duration in working days, dependencies
(separated by ;) and status.

1. Using code, calculate the critical path from today, counting only
   remaining work (Done = 0 days), and the slack for every other task.
2. Flag: tasks with no owner, tasks with no dependencies that probably
   should have some, and tasks with very little slack.
3. Stress test: what happens to the end date if the 3 riskiest tasks each
   slip by 50%? Show it as a table.
4. List the 5 questions I should ask at the next steering committee.

Write the Python so I can re-run it in Google Colab, with plain-English
comments. Then explain the critical path to me in 3 sentences.
```

### Follow-up: combine with the meeting

```text
Here is the transcript of the last steering committee [paste from Kit 1].
Compare it with the plan. What did people say that the plan doesn't
reflect yet? Update the plan table accordingly.
```

## What good looks like (for the sample)

- **Critical path:** pick-list defect fix (T3) → regression testing (T4) →
  final data migration (T10) → go/no-go (T11) → go-live (T12). 21 working
  days of remaining work, including the go-live week.
- **No owner:** label printer firmware (T5). It has 12 days of slack, which
  can feel comfortable but is risky because nobody is doing it.
- **Missing dependency:** go-live (T12) should probably depend on the
  printer firmware (T5), not just the go/no-go.
- **Stress test:** any slip in T3 or T4 moves go-live day for day.
  Temp staff recruitment (T8) has only 4 days of slack.

## Where AI is wrong

- **"In progress" is counted at full duration** unless you give % complete.
  Tell it how much is left.
- **Calendars:** it usually ignores weekends, holidays and shift patterns
  unless asked.
- **Dependencies you didn't write down don't exist for the AI.** The most
  valuable output is often the question "should T12 depend on T5?" Only you
  can answer it.
- **It can't tell a padded estimate from an honest one.** Ask the task
  owners, not the AI, how confident they are.
