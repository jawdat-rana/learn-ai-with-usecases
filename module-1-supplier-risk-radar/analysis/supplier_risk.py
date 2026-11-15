# %% [markdown]
# # Supplier Risk Radar
#
# This code was written by an AI from the plain-English prompt in
# `module-1-supplier-risk-radar/prompts.md` (Step 3). A human then read the
# explanation, checked a few rows by hand and asked the AI for fixes.
#
# **You do not need to understand every line.** Run each cell in order
# (press Shift+Enter in Google Colab). If something breaks, copy the error
# message into your AI chat and ask: "What does this error mean and how do I fix it?"

# %%
# STEP 1: Load the supplier list.
# It tries a local copy first, then downloads the sample file from GitHub.
from pathlib import Path
import math
import pandas as pd

# If you copied this course to your own GitHub account and changed the data,
# replace "jawdat-rana" below with your own GitHub username.
DATA_URL = (
    "https://raw.githubusercontent.com/jawdat-rana/learn-ai-with-usecases/"
    "main/module-1-supplier-risk-radar/data/suppliers.csv"
)

def find_data_file():
    candidates = [Path("suppliers.csv"), Path("data/suppliers.csv")]
    try:  # works when you run the .py file on a computer
        candidates.insert(0, Path(__file__).resolve().parent.parent / "data" / "suppliers.csv")
    except NameError:  # Colab notebooks have no __file__, so skip it
        pass
    for path in candidates:
        if path.exists():
            return path
    return DATA_URL

suppliers = pd.read_csv(find_data_file())
print(f"Loaded {len(suppliers)} suppliers")
suppliers.head()

# %%
# STEP 2: Turn each column into a 1-5 score using a simple rubric.
# 1 = low risk, 5 = high risk. The rubric is written in plain English in
# README.md, so a non-coder can challenge it.

def round_half_up(x):
    return int(math.floor(x + 0.5))

def score_lead_time(days):
    if pd.isna(days):
        return 5  # missing data is treated as worst case, and flagged below
    if days <= 14: return 1
    if days <= 30: return 2
    if days <= 45: return 3
    if days <= 60: return 4
    return 5

def score_on_time(pct):
    if pct >= 95: return 1
    if pct >= 90: return 2
    if pct >= 85: return 3
    if pct >= 80: return 4
    return 5

def score_spend(usd):
    if usd >= 4_000_000: return 5
    if usd >= 2_000_000: return 4
    if usd >= 1_000_000: return 3
    if usd >= 500_000: return 2
    return 1

def score_concentration(share_pct):
    if share_pct >= 60: return 5
    if share_pct >= 40: return 4
    if share_pct >= 25: return 3
    if share_pct >= 10: return 2
    return 1

def score_substitutability(single_source, alternates):
    if single_source == "Y": return 5
    if alternates == 0: return 4
    if alternates == 1: return 3
    if alternates == 2: return 2
    return 1

# News flags: we pasted news-snippets.md into the AI and asked it which
# suppliers each story affects. A human checked every match (see README:
# the AI wrongly matched "Northwind Circuit Solutions" to Northwind Circuits).
NEWS_FLAGS = {
    "S06": "Plant consolidation, customers warned of allocation (news #2)",
    "S25": "Missed a bond payment (news #3)",
    "S07": "Workers voting on strike action (news #5)",
    "S14": "New export licensing rules for battery cells (news #7)",
    "S22": "New export licensing rules for battery cells (news #7)",
}

APPLY_NEWS = True  # change to False to see the risk without news

df = suppliers.copy()
df["s_region"] = df["region_risk_1to5"]
df["s_financial"] = 6 - df["financial_health_1to5"]
df["s_on_time"] = df["on_time_delivery_pct"].apply(score_on_time)
df["s_lead_time"] = df["lead_time_days"].apply(score_lead_time)
df["s_spend"] = df["annual_spend_usd"].apply(score_spend)
df["s_concentration"] = df["share_of_category_spend_pct"].apply(score_concentration)
df["s_substitutability"] = [
    score_substitutability(s, a) for s, a in zip(df["single_source"], df["qualified_alternates"])
]

likelihood_cols = ["s_region", "s_financial", "s_on_time", "s_lead_time"]
impact_cols = ["s_spend", "s_concentration", "s_substitutability"]
df["likelihood"] = df[likelihood_cols].mean(axis=1).apply(round_half_up)
df["impact"] = df[impact_cols].mean(axis=1).apply(round_half_up)

df["news"] = df["supplier_id"].map(NEWS_FLAGS).fillna("")
if APPLY_NEWS:
    df.loc[df["news"] != "", "likelihood"] = (df["likelihood"] + 1).clip(upper=5)

df["risk_score"] = df["likelihood"] * df["impact"]  # 1 to 25
df["risk_tier"] = pd.cut(df["risk_score"], bins=[0, 7, 14, 25], labels=["Low", "Medium", "High"])
df["data_gaps"] = df["lead_time_days"].isna().map({True: "Lead time missing", False: ""})

ranked = df.sort_values(["risk_score", "annual_spend_usd"], ascending=False)
ranked[["supplier_id", "supplier_name", "category", "likelihood", "impact",
        "risk_score", "risk_tier", "news", "data_gaps"]].head(10)

# %%
# STEP 3: Concentration check. Which categories depend on one supplier?
by_category = (
    df.sort_values("share_of_category_spend_pct", ascending=False)
      .groupby("category")
      .first()[["supplier_name", "share_of_category_spend_pct", "single_source"]]
      .rename(columns={"supplier_name": "largest_supplier", "share_of_category_spend_pct": "largest_share_pct"})
      .sort_values("largest_share_pct", ascending=False)
)
single_source_spend = df.loc[df["single_source"] == "Y", "annual_spend_usd"].sum()
total_spend = df["annual_spend_usd"].sum()
print(f"Single-source spend: ${single_source_spend:,.0f} "
      f"({single_source_spend / total_spend:.0%} of total spend)")
by_category

# %%
# STEP 4: Draw the risk heatmap (likelihood across, impact up).
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 6))
for l in range(1, 6):
    for i in range(1, 6):
        score = l * i
        colour = "#f4c7c3" if score >= 15 else "#fde7b0" if score >= 8 else "#d5ecd4"
        ax.add_patch(plt.Rectangle((l - 0.5, i - 0.5), 1, 1, color=colour, ec="white", lw=2))
        ids = df.loc[(df["likelihood"] == l) & (df["impact"] == i), "supplier_id"].tolist()
        if ids:
            ax.text(l, i, "\n".join(", ".join(ids[k:k + 3]) for k in range(0, len(ids), 3)),
                    ha="center", va="center", fontsize=8)
ax.set_xlim(0.5, 5.5); ax.set_ylim(0.5, 5.5)
ax.set_xticks(range(1, 6)); ax.set_yticks(range(1, 6))
ax.set_xlabel("Likelihood (region, finances, delivery, lead time)")
ax.set_ylabel("Impact (spend, concentration, substitutability)")
ax.set_title("Supplier risk heatmap (synthetic data)")
plt.tight_layout()
out_dir = Path("output"); out_dir.mkdir(exist_ok=True)
plt.savefig(out_dir / "risk_heatmap.png", dpi=150)
plt.show()

# %%
# STEP 5: Write a short exec one-pager. Paste this into your AI chat and ask it
# to polish the wording, but keep the numbers as they are.
high = ranked[ranked["risk_tier"] == "High"]
lines = [
    "# Supplier risk one-pager (synthetic data)",
    "",
    f"- Suppliers reviewed: {len(df)}; total annual spend ${total_spend / 1e6:.1f}M",
    f"- High-risk suppliers: {len(high)}, covering ${high['annual_spend_usd'].sum() / 1e6:.1f}M of spend",
    f"- Single-source spend: ${single_source_spend / 1e6:.1f}M ({single_source_spend / total_spend:.0%})",
    "",
    "## Top risks",
]
for _, r in high.iterrows():
    note = f" News: {r['news']}." if r["news"] else ""
    lines.append(f"- **{r['supplier_name']}** ({r['category']}, {r['region']}): "
                 f"score {r['risk_score']}/25, {r['share_of_category_spend_pct']}% of category spend, "
                 f"single source: {r['single_source']}.{note}")
gaps = df[df["data_gaps"] != ""]
if len(gaps):
    lines += ["", "## Data gaps to fix before trusting this"]
    lines += [f"- {r['supplier_name']}: {r['data_gaps']}" for _, r in gaps.iterrows()]
one_pager = "\n".join(lines)
(out_dir / "one_pager.md").write_text(one_pager)
print(one_pager)
