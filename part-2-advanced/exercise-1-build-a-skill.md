# Exercise 1: Build a skill

**Goal:** turn the supplier risk method from Module 1 into a reusable
**skill**, so that you (or a colleague) get a consistent review every time,
with no re-explaining.

## What a skill is

A skill is a folder with a `SKILL.md` file: a short description of **when**
to use it, followed by **how** to do the task. Skills are an open format:
Claude can load them automatically, and you can paste the same text into any
other AI tool. Two finished examples are in this repository:

- [skills/supplier-risk-review/SKILL.md](skills/supplier-risk-review/SKILL.md)
- [skills/steerco-minutes/SKILL.md](skills/steerco-minutes/SKILL.md)

Open one now. Notice it's plain English. The **description** at the top
matters most, because it's how the AI decides when to use the skill.

## Step 1: Let the AI interview you (15 min)

```text
I want to write a reusable "skill": a set of instructions an AI follows
every time I ask for a [supplier risk review]. Interview me, one question
at a time, about how I do this task: inputs, steps, rules, output format,
common mistakes and what "good" looks like. Ask at most 10 questions.
Then write it as a SKILL.md file with this structure:

---
name: short-name-with-dashes
description: what it does and WHEN to use it, in 1-2 sentences
---
# Title
## Steps
## Rules
```

Use [the supplier risk example](skills/supplier-risk-review/SKILL.md) as a
model if you get stuck, or pick a task from your own job (a weekly S&OP
pack, a supplier QBR, a carrier tender review).

## Step 2: Save it in your repository (5 min)

In your GitHub copy, open `part-2-advanced/skills`, click **Add file →
Create new file**, and type `my-skill-name/SKILL.md` as the name (the slash
makes the folder). Paste, then **Commit changes**.

## Step 3: Use it (pick what your free plan allows)

Plans and features change often, so use whichever of these your account
offers:

- **Any AI tool, always works:** start a new chat, paste the whole SKILL.md
  and write: "Follow these instructions for the rest of this chat." Then
  attach your data.
- **Claude:** if your plan shows **Skills** under Settings → Capabilities,
  zip the skill folder and upload it there. Claude then uses it
  automatically whenever your request matches the description.
- **Gemini:** create a **Gem** and paste the skill as its instructions.
- **ChatGPT:** if your plan lets you create a project or custom GPT, paste
  the skill into its instructions.

## Step 4: Test it like a product (15 min)

A skill is only good if it works on inputs you didn't design it for.

1. Run it on `module-1-supplier-risk-radar/data/suppliers.csv`. Do you get
   the same 4 high-risk suppliers as Module 1?
2. Ask the AI to make **a messier version** of the file: rename columns,
   add blanks, include a supplier twice. Run the skill again. Did it notice?
3. Run it in a **different AI tool**. Same answer?
4. Fix the SKILL.md where it went wrong, and commit the new version. GitHub
   keeps the history, so you can see how your skill improved.

## Where AI is wrong

- **Vague descriptions mean the skill is ignored** (or used at the wrong
  time). "Helps with suppliers" is too vague. Say what input and what
  request should trigger it.
- **Long skills get partly ignored.** Keep the core steps short. Put rarely
  needed detail at the end.
- **A skill makes errors consistent, too.** If your rubric is wrong, it will
  be applied wrong every time. Review it with a colleague.
