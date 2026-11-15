# War-room scenarios (all fictional)

## Scenario 1: Port Alpha closes for three weeks (used in the module)

> **Monday 07:30.** Port Alpha has stopped all container handling after a
> crane collapse and a safety investigation. The port authority expects
> three weeks before normal operations. Ships are anchoring outside or
> diverting.
>
> Nine of our twelve products (SKU-101 to SKU-109) come in through Port Alpha
> every week. Three (SKU-110 to SKU-112) are made domestically and are not
> affected.
>
> Options on the table from logistics:
> - **Reroute** blocked containers through Port Beta. Their agent says first
>   arrivals in week 3, up to 80% of our normal weekly volume, at about $3.50
>   extra per unit.
> - **Air freight** up to half the weekly volume of the five air-eligible
>   products, from week 1, at about $14 extra per unit.
>
> Tier A customers (our top retailers) have penalty clauses for missed
> deliveries. Steering committee is at 16:00.

**Data:** [inventory.csv](data/inventory.csv), [response_options.csv](data/response_options.csv)

**Stakeholders (fictional roles for the RAID log and messages):**

| Who | Cares about |
|---|---|
| VP Supply Chain (decision maker) | Cost, service, reputation |
| Head of Sales | Tier A customers, penalty clauses |
| Finance Business Partner | Unbudgeted freight spend |
| Customer Service Lead | What to tell customers and when |
| 3PL / freight forwarder | Port Beta capacity, booking deadlines |
| Warehouse Manager | Receiving surge in weeks 4-6 |

---

## Scenario 2: A key supplier fails its audit (links to Module 1)

> Voltaria Cells (S06 in Module 1), our single-source battery supplier with
> 66% of battery spend, has failed a safety and labour audit at its main
> plant. Our policy says we must stop new orders until corrective actions
> are verified, normally 6 to 10 weeks. We have 5 weeks of battery stock.
> Helix Power (S14) and Ampere Storage (S22) make similar cells but neither
> is qualified for our two main products.

**Try:** use Prompts 1, 4b, 5, 6 and 8 from [prompts.md](prompts.md) with this
scenario instead. No code needed. Ask the AI to compare: (a) wait,
(b) fast-track qualification of S22, (c) an exception process with
on-site monitoring, (d) a design change. What are the ethical and
reputational sides, not just cost?

---

## Scenario 3: Demand spike (stretch)

> A competitor's recall sends extra demand our way: smart thermostat
> (SKU-101) and control hub (SKU-109) demand doubles for six weeks, starting
> in week 2, at the same time as the Port Alpha closure.

**Try:** ask the AI to change `war_room.py` so weekly demand can differ by
week, then re-run the four options. Which option wins now? This is how you
learn that you don't need to code: you describe the change in plain English
and check the result makes sense.
