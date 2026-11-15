# Part 2 (advanced): skills, agents and AI teams

Part 1 used AI as a very capable assistant: you ask, it answers, you check.
Part 2 is about making AI **repeatable** and **autonomous**:

| Idea | In plain English | Supply chain example |
|---|---|---|
| **Skill** | A reusable instruction pack. You write your best way of doing a task once, and the AI follows it every time. | Your supplier risk rubric, so every review is scored the same way. |
| **Agent** | An AI with a job, instructions and **tools** it can use on its own (for example, running a simulation) in a loop until the job is done. | An analyst that runs the war-room simulation for each scenario by itself. |
| **Team of agents** | Several agents with different roles that hand work to each other, including one whose job is to check the others. | Planner → Analyst → Reviewer for a disruption. |

**Do Part 1 first.** Part 2 reuses the Module 1 rubric and the Module 2
simulation.

## The exercises

| # | Exercise | Code? | Time |
|---|---|---|---|
| 1 | [Build a skill](exercise-1-build-a-skill.md): package your supplier risk method so any AI applies it the same way | No | 45 min |
| 2 | [Run an agent team by hand](exercise-2-agent-team-no-code.md): three chat windows act as Planner, Analyst and Reviewer, and you pass work between them | No | 60 min |
| 3 | [Build a real agent team in Colab](exercise-3-agent-team-in-colab.md): Python agents that call the war-room simulation as a tool, using Google's free Gemini API | AI-written Python | 60-90 min |

All three work without a paid subscription.

## Where agents go wrong (more than chat does)

- **Errors compound.** One agent's small mistake becomes the next agent's
  "fact". That's why exercise 2 and 3 have a Reviewer that checks numbers
  against the **evidence** (the simulation log), not against the other
  agent's words.
- **Agents agree with each other.** Agents built on the same model share the
  same blind spots. Give the Reviewer a different job, different
  information, or even a different AI tool.
- **Loops and limits.** An agent that keeps "trying again" can burn through
  your free daily limit. Always cap the number of rounds (exercise 3 allows
  one revision).
- **Tools do real things.** Here the tool is a harmless simulation. At work,
  an agent that can send emails or place orders needs a human approval step.
- **Instructions hidden in documents.** If an agent reads an email or web
  page saying "ignore your instructions and…", it may obey. Never give an
  agent tools that act on the outside world plus documents from people you
  don't trust.
- **Keys are secrets.** An API key is like a password. Never paste it into
  code you commit to GitHub. Use Colab's Secrets panel.
