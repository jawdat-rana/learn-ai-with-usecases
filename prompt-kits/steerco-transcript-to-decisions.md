# Kit 1: Steering committee transcript → decisions, owners and risks

**Use it when:** you have a meeting transcript (Teams, Zoom or Meet can make
one) or messy notes, and you need clear minutes, actions and risks out
within the hour.

**Try it with:** [samples/steerco-transcript.txt](samples/steerco-transcript.txt),
a fictional warehouse-system upgrade steering committee.

## The prompt

```text
You are an experienced PMO lead. Below is a steering committee transcript.
Produce:

1. DECISIONS: only things that were actually decided. Quote the line that
   shows the decision. If something sounds decided but isn't, list it under
   "Unclear decisions" instead.
2. ACTIONS: action | owner | due date | source quote. If no owner or date
   was clearly agreed, write "NOT AGREED". Never guess an owner.
3. RISKS AND ISSUES: description | impact (H/M/L) | raised by | is it in
   our risk log yet? (say "unknown" if you can't tell)
4. CONFLICTS: places where people gave different dates, numbers or views.
5. QUESTIONS TO CLOSE: the 3-5 things I should chase before the next
   meeting.
6. A 5-line summary I can send to the sponsor.

Be strict: if it isn't in the transcript, don't include it.

[paste transcript]
```

## What good looks like (for the sample)

- **Decisions:** keep the 3rd as target date; go/no-go call on the 27th by
  Priya with Tom's operations sign-off.
- **Actions with no clear owner:** revised budget forecast (Sam said "I can
  send something", no date); temp staff at Northgate ("probably", no owner or
  date); finding the hardware owner for printer firmware.
- **Conflicts:** fix date "20th, maybe the 24th"; go-live on the 3rd needs
  fix on the 24th plus 5 working days of regression, which is very tight.
- **Hidden risk:** label printer firmware isn't on the defect list and has no
  owner. Night shift training is behind.

## Where AI is wrong

- **It invents owners and dates** to make the table look complete. The
  "NOT AGREED" rule above is your defence. Check every owner against the
  transcript.
- **It turns opinions into decisions.** "I'd rather slip a week" is a view,
  not a decision.
- **Speech-to-text errors** become facts: names, numbers and dates are the
  most often misheard. Check them.
- **It misses what wasn't said.** It can't know that a risk was raised last
  month and ignored. Your judgement adds the history.

## Make it yours

Add your organisation's RAID or minutes template to the prompt: "Use exactly
this format: [paste]". Turn it into a skill in [Part 2](../part-2-advanced/exercise-1-build-a-skill.md).
