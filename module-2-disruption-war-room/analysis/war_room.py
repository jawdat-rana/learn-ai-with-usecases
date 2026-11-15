# %% [markdown]
# # Disruption War-Room: "Port Alpha closes for 3 weeks"
#
# This code was written by an AI from the plain-English prompt in
# `module-2-disruption-war-room/prompts.md` (Step 4). It simulates stock week
# by week for every product, then compares four response options.
#
# **You do not need to understand every line.** Run the cells in order
# (Shift+Enter in Google Colab). Change the numbers in STEP 1 to ask "what if?".

# %%
# STEP 1: Settings you can change. Try 4 closure weeks, or a later reroute.
CLOSURE_START_WEEK = 1
CLOSURE_WEEKS = 3
BACKLOG_RELEASE_SHARE_PCT = 100  # extra cargo the port clears per week after reopening
HORIZON_WEEKS = 8

# %%
# STEP 2: Load the products and the response options.
from pathlib import Path
import pandas as pd

# If you copied the course and changed the data, put your GitHub username here.
BASE_URL = (
    "https://raw.githubusercontent.com/jawdat-rana/learn-ai-with-usecases/"
    "main/module-2-disruption-war-room/data/"
)

def load(name):
    candidates = [Path(name), Path("data") / name]
    try:  # running the .py file on a computer
        candidates.insert(0, Path(__file__).resolve().parent.parent / "data" / name)
    except NameError:  # Colab notebooks have no __file__
        pass
    for path in candidates:
        if path.exists():
            return pd.read_csv(path)
    return pd.read_csv(BASE_URL + name)

inventory = load("inventory.csv")
options = load("response_options.csv").fillna({"reroute_start_week": 0, "air_start_week": 0})
print(f"{len(inventory)} products, {len(options)} options")
options[["option_id", "option_name", "what_it_means"]]

# %%
# STEP 3: The simulation. One loop per product, one row per week.
# Assumptions (say these out loud in the war room!):
#  - Demand we cannot serve is lost, not back-ordered.
#  - Containers blocked at Port Alpha wait in a backlog. Reroute and air
#    freight take units out of that backlog, so nothing is counted twice.
#  - Air freight stops once rerouted containers start arriving.

def simulate(item, option, protect_tier_a):
    stock = item["on_hand_units"]
    backlog = 0
    inbound = item["weekly_inbound_units"]
    reroute_on = option["reroute_share_pct"] > 0
    air_on = option["air_share_pct"] > 0 and item["air_eligible"] == "Y"
    rows = []
    for week in range(1, HORIZON_WEEKS + 1):
        closed = CLOSURE_START_WEEK <= week < CLOSURE_START_WEEK + CLOSURE_WEEKS
        arrivals, extra_cost = 0, 0.0
        if item["ships_via"] != "Port Alpha":
            arrivals = inbound
        elif closed:
            backlog += inbound
        else:
            release = min(backlog, inbound * BACKLOG_RELEASE_SHARE_PCT / 100)
            backlog -= release
            arrivals = inbound + release
        if item["ships_via"] == "Port Alpha":
            rerouting = reroute_on and week >= option["reroute_start_week"]
            if rerouting:
                moved = min(backlog, inbound * option["reroute_share_pct"] / 100)
                backlog -= moved; arrivals += moved
                extra_cost += moved * option["reroute_cost_per_unit_usd"]
            if air_on and week >= option["air_start_week"] and not rerouting:
                flown = min(backlog, inbound * option["air_share_pct"] / 100)
                backlog -= flown; arrivals += flown
                extra_cost += flown * option["air_cost_per_unit_usd"]
        available = stock + arrivals
        demand = item["weekly_demand_units"]
        demand_a = demand * item["tier_a_share_pct"] / 100
        shipped = min(available, demand)
        shipped_a = min(available, demand_a) if protect_tier_a else shipped * item["tier_a_share_pct"] / 100
        stock = available - shipped
        rows.append({
            "sku": item["sku"], "week": week, "arrivals": arrivals, "closing_stock": stock,
            "demand": demand, "shipped": shipped, "short": demand - shipped,
            "demand_tier_a": demand_a, "shipped_tier_a": shipped_a,
            "lost_margin": (demand - shipped) * item["unit_margin_usd"], "extra_cost": extra_cost,
            "below_safety": stock < item["safety_stock_units"],
        })
    return rows

def run_option(option, protect_tier_a):
    rows = []
    for _, item in inventory.iterrows():
        rows += simulate(item, option, protect_tier_a)
    return pd.DataFrame(rows)

# %%
# STEP 4: Compare the options side by side.
summary = []
weekly_by_option = {}
for _, opt in options.iterrows():
    for protect in (False, True):
        w = run_option(opt, protect)
        if protect:
            weekly_by_option[opt["option_id"]] = w
        summary.append({
            "option": f"{opt['option_id']}. {opt['option_name']}",
            "allocation": "Protect tier A" if protect else "First come",
            "extra_freight_usd": round(w["extra_cost"].sum()),
            "units_short": round(w["short"].sum()),
            "lost_margin_usd": round(w["lost_margin"].sum()),
            "total_cost_usd": round(w["extra_cost"].sum() + w["lost_margin"].sum()),
            "fill_rate_pct": round(100 * w["shipped"].sum() / w["demand"].sum(), 1),
            "tier_a_fill_rate_pct": round(100 * w["shipped_tier_a"].sum() / w["demand_tier_a"].sum(), 1),
        })
summary = pd.DataFrame(summary)
summary

# %%
# STEP 5: Which products run out, and when? (Option A, do nothing)
w = weekly_by_option["A"]
stockouts = (w[w["short"] > 0].groupby("sku")
             .agg(first_short_week=("week", "min"), units_short=("short", "sum"),
                  lost_margin_usd=("lost_margin", "sum"))
             .sort_values("lost_margin_usd", ascending=False))
stockouts

# %%
# STEP 6: Chart total stock by week for each option.
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 4.5))
for opt_id, w in weekly_by_option.items():
    total = w.groupby("week")["closing_stock"].sum()
    name = options.loc[options["option_id"] == opt_id, "option_name"].iloc[0]
    ax.plot(total.index, total.values, marker="o", label=f"{opt_id}. {name}")
ax.axvspan(CLOSURE_START_WEEK - 0.5, CLOSURE_START_WEEK + CLOSURE_WEEKS - 0.5, color="grey", alpha=0.15, label="Port closed")
ax.set_xlabel("Week"); ax.set_ylabel("Units in stock (all products)")
ax.set_title("Stock by week under each option (synthetic data)")
ax.legend(fontsize=8)
plt.tight_layout()
out_dir = Path("output"); out_dir.mkdir(exist_ok=True)
plt.savefig(out_dir / "stock_by_option.png", dpi=150)
plt.show()

# %%
# STEP 7: Save the numbers so you can paste them into your AI chat for the
# decision memo (see prompts.md, Step 5).
summary.to_csv(out_dir / "option_comparison.csv", index=False)
print(summary.to_string(index=False))
