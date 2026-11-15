# 1. How AI chat tools work, in 10 minutes

You don't need the maths. You need a mental model good enough to know when to
trust the answer.

## The one-paragraph version

Tools like Claude, ChatGPT and Gemini are **large language models**. They were
trained on a huge amount of text and learned to predict what comes next. That
simple trick, at enormous scale, turns out to produce something that can
summarise, reason through a problem, write code and explain it. But it is
still *predicting plausible text*, which is why it can be fluent, confident
and wrong at the same time.

## Five things that change how you use it

| What's true | What it means for you |
|---|---|
| **It only knows what you tell it, plus its training.** It doesn't know your company, your suppliers or today's news unless you paste them in. | Context is everything. Give it the data, the goal and the constraints. |
| **It's better at language than arithmetic.** Adding up 30 numbers "in its head" can go wrong. | For anything numeric, ask it to **write and run code**. Code is exact; mental maths isn't. |
| **It sounds equally confident when it's right and when it's wrong.** | Confidence is not evidence. Check one or two numbers yourself, and ask for its assumptions. |
| **It tends to agree with you.** If you lead the witness, it follows. | Ask neutral questions, and explicitly ask it to disagree: "What's the strongest case against this?" |
| **It remembers the current chat, not last week's.** | Keep a piece of work in one chat. Save good prompts and results in your [journal](../my-ai-journal.md). |

## Chat tool vs code: why this course uses both

When you ask a question, the AI answers in words. When you ask it to
*calculate*, a good habit is to have it write a small program (in Python) and
run it. Some free AI tools can run the code for you in the chat. If yours
can't, you paste the code into **Google Colab**, a free website that runs
Python with one click. Either way **you never need to write code yourself**.
More on that in [lesson 3](03-you-dont-need-to-code.md).

## What never to paste into a public AI tool

- Personal data about real people (names, contact details, salaries, health)
- Confidential company data: real supplier prices, contracts, customer lists,
  unreleased plans, unless your company has approved that tool for it
- Passwords, access keys, or anything that would hurt if it appeared in a
  newspaper

Free consumer plans may keep your chats and some use them to improve their
models. Check each tool's privacy settings and your company's AI policy.
**That's why every exercise in this course uses synthetic (made-up) data.**

## Which free tool should I use?

Any of them. Free plans of Claude (claude.ai), ChatGPT (chatgpt.com) and Gemini
(gemini.google.com) all handle every exercise here. Free plans have daily
usage limits and features change often, so if one tool runs out, paste your
work into another and carry on. Trying the same prompt in two tools is also a
great way to see how differently they think.

**Next:** [2. Prompting for senior professionals](02-prompting-for-leaders.md)
