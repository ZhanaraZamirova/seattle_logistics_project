# Seattle Logistics & Supply Chain Analysis

This is an independent project I built to look into delivery delays and safety incidents for trucking routes in and around Seattle. I wanted practice building a real ETL pipeline end to end, not just working with data that's already clean and ready to go.

**Tools:** Python (Pandas, Datetime), SQLite, Tableau, VS Code

## Data source

The core logistics data came from the "Logistics Operations Database" on Kaggle (created by Yogape Rodriguez) — it's a simulated dataset modeled on a real Class 8 trucking company's operations from 2022–2024. I sourced historical Seattle-area weather data separately and merged it in myself.

## What I found

Dashboard:https://public.tableau.com/app/profile/zhanara.zamirova/viz/LogisticsProject_17844983969490/Dashboard1

- **Truck detention times spike overnight.** Delays jump to almost 120 minutes on average around 3 AM. My guess is this points to a staffing or dock-availability gap during the night shift, though it'd be worth someone actually checking on the ground before assuming that.
- **DOT violations are the most expensive incident type**, averaging over $14,200 per occurrence — higher than accidents or equipment damage. Shifting more of the safety training budget toward DOT compliance specifically might do more than spreading it evenly across incident types.

## How the pipeline works

1. Filtered national logistics data down to Seattle-only routes.
2. Converted delivery timestamps to datetime objects and rounded them to the nearest hour so they'd line up with the hourly weather data.
3. Used a left join to attach safety incidents to the full delivery table — this mattered because most deliveries don't have an incident, and an inner join here would've silently dropped every clean trip.
4. Loaded the final dataset into SQLite so I could query it with SQL, not just filter it in Pandas.

## A note on the weather data

Going in, I actually expected weather to be a real factor in delays. It wasn't. Since the Kaggle dataset is simulated, delivery events weren't actually tied to real historical weather patterns, so there was nothing to find. I left weather out of the final dashboard since it wasn't pointing to anything actionable — but it's also a big part of why I think this project would look different with real-world data instead of a simulated dataset.

## Repo structure

- `/data` — raw CSVs (some larger files excluded for size)
- `/scripts` — `merge.py`, `merge_incidents.py`, `load_to_sql.py`
- `/database` — final SQLite database
- `/dashboard` — Tableau screenshots
