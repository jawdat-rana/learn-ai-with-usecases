# %% [markdown]
# # Project plan stress test: critical path
# Written by AI from the prompt in prompt-kits/project-plan-stress-test.md.
# It finds the longest chain of dependent tasks (the critical path): any delay
# on these tasks delays go-live. Run each cell in order.

# %%
from pathlib import Path
import pandas as pd

DATA_URL = ("https://raw.githubusercontent.com/jawdat-rana/learn-ai-with-usecases/"
            "main/prompt-kits/samples/project-plan.csv")
candidates = [Path("project-plan.csv")]
try:
    candidates.insert(0, Path(__file__).resolve().parent / "project-plan.csv")
except NameError:
    pass
plan = pd.read_csv(next((p for p in candidates if p.exists()), DATA_URL)).fillna({"depends_on": ""})
plan["deps"] = plan["depends_on"].apply(lambda s: [d for d in s.split(";") if d])
plan = plan.set_index("task_id")

# %%
# STEP 1: Earliest start and finish for each task (in working days from day 0).
# Remaining work only: tasks marked Done take 0 more days.
remaining = plan["duration_days"].where(plan["status"] != "Done", 0)
finish = {}
def earliest_finish(t):
    if t not in finish:
        start = max((earliest_finish(d) for d in plan.at[t, "deps"]), default=0)
        finish[t] = start + remaining[t]
    return finish[t]
for t in plan.index:
    earliest_finish(t)
plan["remaining_days"] = remaining
plan["earliest_finish_day"] = pd.Series(finish)

# %%
# STEP 2: Walk back from the last task to find the critical path.
end = plan["earliest_finish_day"].idxmax()
path, t = [end], end
while plan.at[t, "deps"]:
    t = max(plan.at[t, "deps"], key=lambda d: finish[d])
    path.append(t)
path.reverse()
print(f"Go-live work finishes on day {finish[end]} from today")
print("Critical path:", " -> ".join(f"{p} {plan.at[p, 'task']}" for p in path))

# %%
# STEP 3: Slack: how many days each task can slip before it delays go-live.
latest_finish = {t: finish[end] for t in plan.index}
for t in sorted(plan.index, key=lambda x: -finish[x]):
    for d in plan.at[t, "deps"]:
        latest_finish[d] = min(latest_finish[d], latest_finish[t] - remaining[t])
plan["slack_days"] = pd.Series({t: latest_finish[t] - finish[t] for t in plan.index})
plan["flags"] = ""
plan.loc[plan["owner_role"] == "Unassigned", "flags"] += "No owner. "
plan.loc[plan["slack_days"] == 0, "flags"] += "Critical. "
plan[["task", "owner_role", "status", "remaining_days", "earliest_finish_day", "slack_days", "flags"]]
