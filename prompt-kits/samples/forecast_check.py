# %% [markdown]
# # Demand forecast sanity check
# Written by AI from the prompt in prompt-kits/demand-forecast-sanity-check.md.
# It builds a simple "same month last year, adjusted for growth" baseline and
# flags planner forecasts that are more than 20% away from it. Run each cell
# in order (Shift+Enter in Google Colab).

# %%
# STEP 1: Load the sales history and the planner's forecast.
from pathlib import Path
import pandas as pd

DATA_URL = ("https://raw.githubusercontent.com/jawdat-rana/learn-ai-with-usecases/"
            "main/prompt-kits/samples/monthly-sales.csv")
candidates = [Path("monthly-sales.csv")]
try:
    candidates.insert(0, Path(__file__).resolve().parent / "monthly-sales.csv")
except NameError:
    pass
source = next((p for p in candidates if p.exists()), DATA_URL)
sales = pd.read_csv(source)
actual = sales[sales["type"] == "actual"].copy()
forecast = sales[sales["type"] == "planner_forecast"].copy()
print(f"{len(actual)} months of actuals, {len(forecast)} forecast months")

# %%
# STEP 2: Spot unusual months in the history (for example a one-off promotion).
# A month is flagged if it is more than 50% above the median of its neighbours.
actual = actual.sort_values(["product", "month"])
actual["neighbour_median"] = (actual.groupby("product")["units"]
                              .transform(lambda s: s.rolling(5, center=True, min_periods=3).median()))
actual["outlier"] = actual["units"] > 1.5 * actual["neighbour_median"]
print("Unusual months in the history:")
print(actual.loc[actual["outlier"], ["month", "product", "units", "neighbour_median"]].to_string(index=False))

# %%
# STEP 3: Build the baseline: same month last year x growth over the last 12 months.
# Outliers are replaced by their neighbour median so a one-off promo doesn't inflate it.
actual["clean_units"] = actual["units"].where(~actual["outlier"], actual["neighbour_median"])
rows = []
for product, hist in actual.groupby("product"):
    hist = hist.set_index("month")["clean_units"]
    last12, prev12 = hist.iloc[-12:].sum(), hist.iloc[-24:-12].sum()
    growth = last12 / prev12
    for _, f in forecast[forecast["product"] == product].iterrows():
        same_month_last_year = f"{int(f['month'][:4]) - 1}{f['month'][4:]}"
        baseline = hist[same_month_last_year] * growth
        gap = f["units"] / baseline - 1
        rows.append({"product": product, "month": f["month"], "planner_forecast": f["units"],
                     "baseline": round(baseline), "gap_pct": round(100 * gap, 1),
                     "flag": "CHECK" if abs(gap) > 0.20 else ""})
check = pd.DataFrame(rows)
print(f"Growth used: last 12 months vs the 12 before")
check

# %%
# STEP 4: Chart history, baseline and planner forecast for each product.
import matplotlib.pyplot as plt

fig, axes = plt.subplots(len(check["product"].unique()), 1, figsize=(9, 6), sharex=False)
for ax, (product, hist) in zip(axes, actual.groupby("product")):
    ax.plot(hist["month"], hist["units"], color="#2a78d6", lw=2, label="Actual")
    out = hist[hist["outlier"]]
    ax.scatter(out["month"], out["units"], color="#d03b3b", zorder=3, label="Unusual month")
    c = check[check["product"] == product]
    ax.plot(c["month"], c["baseline"], color="#52514e", lw=2, ls="--", label="Baseline")
    ax.plot(c["month"], c["planner_forecast"], color="#eb6834", lw=2, label="Planner forecast")
    ax.set_title(product, fontsize=10); ax.tick_params(axis="x", labelrotation=90, labelsize=7)
    ax.legend(fontsize=7, loc="upper left")
plt.tight_layout(); plt.show()
