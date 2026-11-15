# Kit 2: Contract and SLA risk review

**Use it when:** a supplier, 3PL or service contract lands on your desk and
you want to know which clauses to worry about before legal and procurement
get involved.

**Try it with:** [samples/logistics-sla.md](samples/logistics-sla.md), a
fictional warehousing agreement with several deliberately one-sided clauses.

> This is a first-pass review to help you ask better questions. It isn't
> legal advice, and real contracts should go to your legal team. Don't paste
> real contracts into a public AI tool unless your company allows it.

## The prompt

```text
You are a senior supply chain contracts manager reviewing a contract on
behalf of the CUSTOMER. Review the text below and produce:

1. A risk table: clause number | what it says in plain English | why it's
   risky for us | severity (H/M/L) | what to ask for instead.
2. The 3 clauses I should raise first in negotiation, and why.
3. What's MISSING that I'd normally expect in this kind of contract (for
   example, business continuity, audit rights, step-in rights, KPIs measured
   independently).
4. Any clauses that interact badly with each other.

Quote the exact clause text for every point. If you aren't sure what a
clause means, say so rather than guessing.

[paste contract text]
```

## What good looks like (for the sample)

It should flag at least: **auto-renewal with 180 days' notice (3)**;
**unilateral price changes and surcharges "at any time" (5.2, 5.3)**; KPIs
on **"reasonable endeavours"** and **measured by the provider (7.1, 7.2)**;
**service credits as the sole remedy, capped at 5% (8)**; a **liability cap of
$5/kg (10.1)** that is tiny for electronics; **1.5% accepted shrinkage
(10.2)**; **force majeure that covers the provider's own strikes and IT
failures (12)**; **the provider owning our data (14)**; and a **6-month exit
fee even for the provider's breach (15)**. The bad interaction: sole remedy
(8) plus exit fee (15) means poor service is hard to escape.

## Where AI is wrong

- **It misses things in long contracts.** Accuracy drops on 50+ page
  documents. Review section by section, and ask "what did you NOT review?"
- **Jurisdiction matters.** What's enforceable differs by country. The AI
  often assumes US or UK law.
- **It can invent "market standard" figures.** Ask where the number comes
  from. Use your own benchmarks.
- **It reviews the words, not the relationship.** A tough clause may be fine
  with a strategic partner you've worked with for ten years.

## Make it yours

Add your company's contract playbook ("we never accept liability caps below
X") to the prompt, so the AI reviews against your rules, not generic ones.
