# Seattle Logistics and Supply Chain Pipeline: Operations and Safety Analysis

## Project Overview
Welcome to my supply chain data project! The goal of this analysis was to investigate operational bottlenecks and safety hazards for delivery routes in the Greater Seattle area. To do this, I built an end-to-end ETL (Extract, Transform, Load) pipeline to merge logistics records, historical weather data, and safety incident reports into a single, clean dataset. 

From there, I visualized the data to find actionable ways to improve delivery efficiency and reduce the financial impact of safety incidents.

**Tools Used:** Python (Pandas, Datetime), SQLite (for local data storage), Tableau, and VS Code.

## Data Source
The core logistics data used in this project was sourced from the **Logistics Operations Database** on Kaggle, created by Yogape Rodriguez. The dataset is a high-quality, realistic simulation of a Class 8 trucking company's daily operations spanning from 2022 to 2024. External historical weather data for the Seattle region was sourced independently and integrated into the pipeline for correlational analysis.

## Key Business Insights and Recommendations
You can view the full interactive Tableau dashboard here: [https://public.tableau.com/views/LogisticsProject_17844983969490/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link]

* **The 3:00 AM Operational Bottleneck:** The data shows that truck detention times (delays) spike significantly in the middle of the night, with trucks waiting an average of nearly 120 minutes around 3:00 AM. 
  * *Recommendation:* I recommend reviewing warehouse staffing levels and dock availability during the night shift to clear this bottleneck and reduce costs associated with idle trucks.
* **The True Cost of Incidents:** While minor accidents happen frequently, DOT Violations are actually the most expensive incident type on average, costing operations over $14,200 per occurrence. 
  * *Recommendation:* Reallocating a portion of the safety training budget specifically toward DOT compliance and equipment pre-checks could help mitigate these high-cost penalties.

## The ETL Pipeline
Here is a quick look at how I prepared the data for analysis:

1. **Extract and Filter:** I started with large-scale national datasets (routes, loads, and delivery events) and used Pandas to filter operations exclusively to Seattle-bound or Seattle-originating trips.
2. **Transform and Time-Align:** I converted the raw delivery timestamps into standard Pandas datetime objects and rounded them to the nearest hour. This step was crucial for performing an accurate join with the hourly weather data.
3. **Merge and Preserve Baseline:** I used a left join to append the safety incident reports to the master delivery table. This ensured that successful, incident-free deliveries were preserved as a baseline, allowing for accurate incident rate calculations later on.
4. **Load:** Finally, I used Pandas and SQLite3 to programmatically generate a local database file and store the final dataset for future querying.

## Technical Note on Weather Data 
Going into this project, my initial hypothesis was that adverse weather would be a primary driver of delivery delays and accidents in Seattle. However, after successfully integrating the historical weather data, the exploratory data analysis (EDA) revealed a null result. Because the Kaggle dataset is a simulation, the delivery events were not mathematically tied to actual historical weather patterns, resulting in no correlation.

Because the weather metrics did not highlight an actionable root cause, I intentionally excluded them from the final Tableau dashboard to keep the focus on the internal operational factors that management can actually control.

## Repository Structure
* `/data`: The raw `.csv` files used for the initial extraction. (Note: some larger files were excluded due to size limits).
* `/scripts`: My Python ETL scripts (`merge.py`, `merge_incidents.py`, `load_to_sql.py`).
* `/database`: The final SQLite database file.
* `/dashboard`: Screenshots of the final Tableau visualizations.
