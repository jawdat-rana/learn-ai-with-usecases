# %% [markdown]
# # A team of AI agents for the disruption war room
#
# Three agents work together on the Module 2 scenario (Port Alpha closes):
#
# | Agent | Job | Tools |
# |---|---|---|
# | **Planner** | Breaks the problem into scenarios to test, and writes the final memo | none |
# | **Analyst** | Runs the simulation for each scenario and reports results | `run_war_room_simulation` |
# | **Reviewer** | Checks every number against the simulation log, then approves or sends it back | the log |
#
# It uses Google's **Gemini API free tier** (no credit card). Without a key it
# runs in **practice mode** with stand-in answers, so you can see how the
# hand-offs work first. Written by AI from the prompt in
# `part-2-advanced/exercise-3-agent-team-in-colab.md`.
#
# Run each cell in order (Shift+Enter in Google Colab).

# %%
# STEP 1: Install the Gemini library (Colab only needs this once per session).
# The "!" line only works in Colab; on your own computer run: pip install google-genai pandas
try:
    from google import genai
    from google.genai import types
except ImportError:
    import subprocess, sys
    subprocess.run([sys.executable, "-m", "pip", "install", "-q", "google-genai"], check=False)
    try:
        from google import genai
        from google.genai import types
    except ImportError:
        genai = None

# %%
# STEP 2: Your API key. Never paste the key into the code or into GitHub.
# In Colab: click the key icon on the left (Secrets), add GEMINI_API_KEY,
# and switch on "Notebook access". No key = practice mode.
import os
API_KEY = os.environ.get("GEMINI_API_KEY")
try:
    from google.colab import userdata
    API_KEY = userdata.get("GEMINI_API_KEY")
except Exception:
    pass

# Use a current free "flash" model. If you get a "model not found" error,
# check the model list in Google AI Studio and change this name.
MODEL = "gemini-2.5-flash"
PRACTICE_MODE = not (API_KEY and genai)
client = None if PRACTICE_MODE else genai.Client(api_key=API_KEY)
print("Practice mode (no AI calls)" if PRACTICE_MODE else f"Live mode with {MODEL}")

# %%
# STEP 3: The tool. This is the same simulation as Module 2, wrapped as a
# function the Analyst agent is allowed to call. Every call is written to
# SIMULATION_LOG so the Reviewer can check the Analyst's numbers.
from pathlib import Path
import pandas as pd

BASE_URL = ("https://raw.githubusercontent.com/jawdat-rana/learn-ai-with-usecases/"
            "main/module-2-disruption-war-room/data/")

def load(name):
    candidates = [Path(name)]
    try:
        candidates.insert(0, Path(__file__).resolve().parents[2] / "module-2-disruption-war-room" / "data" / name)
    except NameError:
        pass
    for p in candidates:
        if p.exists():
            return pd.read_csv(p)
    return pd.read_csv(BASE_URL + name)

INVENTORY = load("inventory.csv")
OPTIONS = load("response_options.csv")
SIMULATION_LOG = []

def _simulate_option(opt, closure_weeks, reroute_start_week, port_beta_share_pct, air_share_pct, weeks=8):
    extra = short = lost = demand_total = shipped_total = 0.0
    for _, item in INVENTORY.iterrows():
        stock, backlog, inbound = item["on_hand_units"], 0.0, item["weekly_inbound_units"]
        via_port = item["ships_via"] == "Port Alpha"
        air_ok = opt["air_share_pct"] > 0 and item["air_eligible"] == "Y"
        for week in range(1, weeks + 1):
            arrivals = 0.0
            if not via_port:
                arrivals = inbound
            elif week <= closure_weeks:
                backlog += inbound
            else:
                release = min(backlog, inbound); backlog -= release; arrivals = inbound + release
            if via_port:
                rerouting = opt["reroute_share_pct"] > 0 and week >= reroute_start_week
                if rerouting:
                    m = min(backlog, inbound * port_beta_share_pct / 100); backlog -= m; arrivals += m
                    extra += m * opt["reroute_cost_per_unit_usd"]
                if air_ok and not rerouting:
                    f = min(backlog, inbound * air_share_pct / 100); backlog -= f; arrivals += f
                    extra += f * opt["air_cost_per_unit_usd"]
            available = stock + arrivals
            sent = min(available, item["weekly_demand_units"])
            stock = available - sent
            short += item["weekly_demand_units"] - sent
            lost += (item["weekly_demand_units"] - sent) * item["unit_margin_usd"]
            demand_total += item["weekly_demand_units"]; shipped_total += sent
    return extra, short, lost, 100 * shipped_total / demand_total

def run_war_room_simulation(closure_weeks: int, reroute_start_week: int,
                            port_beta_share_pct: int, air_share_pct: int) -> str:
    """Simulate the Port Alpha closure for 8 weeks and compare the four response options.

    Args:
        closure_weeks: How many weeks Port Alpha is closed (1-6).
        reroute_start_week: Week rerouted containers first arrive via Port Beta (1-6).
        port_beta_share_pct: Share of normal weekly volume Port Beta can take (0-100).
        air_share_pct: Share of weekly volume of air-eligible products we can fly (0-100).

    Returns:
        A table with extra freight cost, units short, lost margin, total cost and fill rate per option.
    """
    lines = ["option | extra_freight_usd | units_short | lost_margin_usd | total_cost_usd | fill_rate_pct"]
    for _, opt in OPTIONS.fillna(0).iterrows():
        e, s, l, f = _simulate_option(opt, closure_weeks, reroute_start_week, port_beta_share_pct, air_share_pct)
        lines.append(f"{opt['option_id']}. {opt['option_name']} | {e:,.0f} | {s:,.0f} | {l:,.0f} | {e + l:,.0f} | {f:.1f}")
    table = "\n".join(lines)
    SIMULATION_LOG.append({"settings": dict(closure_weeks=closure_weeks, reroute_start_week=reroute_start_week,
                                            port_beta_share_pct=port_beta_share_pct, air_share_pct=air_share_pct),
                           "result": table})
    return table

print(run_war_room_simulation(3, 3, 80, 50))
SIMULATION_LOG.clear()

# %%
# STEP 4: The agents. An agent here is just: instructions + (optional) tools.
# Read the instructions: this is where the real design work is, and it's in English.
BRIEF = """Port Alpha has closed after a crane collapse; expected closure 3 weeks
(could be 2 to 5). Nine of our twelve products ship through it. Port Beta's
agent says rerouted containers arrive from week 3 (maybe week 4) at up to 80% of
volume (maybe only 50%). We can fly up to 50% of weekly volume for five
air-eligible products. Tier A customers have penalty clauses. The steering
committee wants a recommendation that holds up if our assumptions are wrong."""

AGENTS = {
    "Planner": dict(tools=[], instructions="""You lead a supply chain disruption war room.
Turn the brief into an analysis plan: list 3 to 5 scenarios to test, each with exact
settings for closure_weeks, reroute_start_week, port_beta_share_pct and air_share_pct,
and say what question each scenario answers. Include a base case and pessimistic cases.
Be concise. Do not invent results."""),
    "Analyst": dict(tools=[run_war_room_simulation], instructions="""You are a supply chain analyst.
For EVERY scenario in the plan, call run_war_room_simulation with its settings.
Report results as a compact table per scenario, copying numbers exactly from the tool.
Then say which option is cheapest in each scenario and which option is most robust
across scenarios. Never estimate a number yourself; if you didn't run it, say so."""),
    "Reviewer": dict(tools=[], instructions="""You are a sceptical reviewer.
You get the analyst's report and the SIMULATION LOG of what was actually run.
Check: (1) every number in the report appears in the log, (2) every planned scenario
was run, (3) the conclusion follows from the numbers, (4) key assumptions are stated.
Reply with APPROVED on the first line if it passes, or REVISE on the first line
followed by a numbered list of specific fixes."""),
}

def ask(agent, message):
    """Send a message to one agent and return its reply."""
    spec = AGENTS[agent]
    if PRACTICE_MODE:
        return practice_reply(agent, message)
    config = types.GenerateContentConfig(system_instruction=spec["instructions"],
                                         tools=spec["tools"] or None, temperature=0.2)
    return client.models.generate_content(model=MODEL, contents=message, config=config).text

def practice_reply(agent, message):
    """Stand-in answers so you can see the hand-offs without an API key."""
    if agent == "Planner" and "final memo" not in message:
        return ("PLAN (practice mode)\n1. Base case: closure_weeks=3, reroute_start_week=3, port_beta_share_pct=80, air_share_pct=50\n"
                "2. Longer closure: closure_weeks=5, others as base\n"
                "3. Weak Port Beta: closure_weeks=3, reroute_start_week=4, port_beta_share_pct=50, air_share_pct=50")
    if agent == "Analyst":
        runs = [(3, 3, 80, 50), (5, 3, 80, 50), (3, 4, 50, 50)]
        return "REPORT (practice mode: tool results are real, wording is canned)\n\n" + "\n\n".join(
            f"Scenario {i}: {r}\n" + run_war_room_simulation(*r) for i, r in enumerate(runs, 1))
    if agent == "Reviewer":
        return "APPROVED (practice mode: a real reviewer would check each number against the log)"
    return "MEMO (practice mode): with a real API key the Planner writes the decision memo here."

def show(title, text):
    print("\n" + "=" * 80 + f"\n{title}\n" + "=" * 80 + f"\n{text}")

# %%
# STEP 5: Run the team. Planner -> Analyst -> Reviewer (-> one revision) -> Planner.
plan = ask("Planner", f"BRIEF:\n{BRIEF}")
show("PLANNER: analysis plan", plan)

report = ask("Analyst", f"BRIEF:\n{BRIEF}\n\nPLAN:\n{plan}")
show("ANALYST: results", report)

def log_text():
    return "\n\n".join(f"Run {i}: {r['settings']}\n{r['result']}" for i, r in enumerate(SIMULATION_LOG, 1))

review = ask("Reviewer", f"PLAN:\n{plan}\n\nANALYST REPORT:\n{report}\n\nSIMULATION LOG:\n{log_text()}")
show("REVIEWER: verdict", review)

if review.strip().upper().startswith("REVISE"):
    report = ask("Analyst", f"BRIEF:\n{BRIEF}\n\nPLAN:\n{plan}\n\nYOUR LAST REPORT:\n{report}\n\n"
                            f"REVIEWER FEEDBACK:\n{review}\n\nFix every point and send the full revised report.")
    show("ANALYST: revised results", report)
    review = ask("Reviewer", f"PLAN:\n{plan}\n\nANALYST REPORT:\n{report}\n\nSIMULATION LOG:\n{log_text()}")
    show("REVIEWER: second verdict", review)

memo = ask("Planner", f"Write the final memo for the steering committee (under 300 words): "
                      f"recommendation, why it is robust across scenarios, trade-offs, what would change "
                      f"our mind. Use only numbers from the approved report.\n\nREPORT:\n{report}\n\n"
                      f"REVIEWER VERDICT:\n{review}")
show("PLANNER: final memo", memo)

# %%
# STEP 6: Look under the hood. How many simulations did the team actually run?
print(f"The Analyst called the simulation {len(SIMULATION_LOG)} times:")
for r in SIMULATION_LOG:
    print(" ", r["settings"])
