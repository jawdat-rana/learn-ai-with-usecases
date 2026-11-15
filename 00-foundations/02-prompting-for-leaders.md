# 2. Prompting for senior professionals

You already know how to brief a capable new analyst. A good prompt is the same
thing written down.

## The briefing pattern: R-C-T-F-C

| Part | Question it answers | Example |
|---|---|---|
| **Role** | Who should the AI be? | "You are a senior supply chain analyst." |
| **Context** | What's the situation and what do you know? | "We're a consumer electronics company. 9 of 12 products ship via one port, which has just closed." |
| **Task** | What exactly do you want? | "Rank the response options by total cost and tier A service." |
| **Format** | What should the answer look like? | "A table, then three sentences. Under 200 words." |
| **Checks** | How will we know it's right? | "List your assumptions first. Use code for any calculation." |

## Before and after

**Weak:**

```text
What are the risks with our suppliers?
```

You'll get a generic list that could apply to any company.

**Strong:**

```text
You are a senior procurement risk analyst. Attached is our supplier list
(30 suppliers, synthetic data) with spend, category share, region, lead
time, on-time delivery and financial health.

Identify the 5 suppliers whose failure would hurt us most in the next 6
months. Score each on likelihood and impact (1-5), explain the score in one
line, and suggest one mitigation.

Format: a table, then a 3-sentence summary for a VP.
Checks: use code for any calculations, tell me how you handled missing
data, and name the weakest assumption in your scoring.
```

## Moves that separate good users from great ones

1. **Ask it to ask you questions first.** "Before you start, ask me up to 5
   questions that would improve your answer."
2. **Make it show its working.** "List your assumptions before the answer."
3. **Ask for options, not an answer.** "Give me three approaches with
   trade-offs" beats "what should I do?"
4. **Make it argue with itself.** "Now play devil's advocate against your own
   recommendation."
5. **Iterate like you would with a person.** "Shorter." "Less jargon." "Make
   the second option more aggressive." The first draft is never the last.
6. **Calculate with code.** "Write and run Python to calculate this" removes
   most arithmetic errors.
7. **Give it an example of what good looks like.** Paste a memo you liked and
   say "same structure and tone".
8. **Keep one chat per piece of work** so it remembers the context.

## Try it now (5 minutes)

Take a real (non-confidential) problem from your week, such as preparing for a
supplier review, and write a prompt using R-C-T-F-C. Then run it in two
different AI tools and compare. Log what you learned in your
[journal](../my-ai-journal.md).

**Next:** [3. You don't need to code](03-you-dont-need-to-code.md)
