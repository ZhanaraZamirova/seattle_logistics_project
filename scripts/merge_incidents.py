import pandas as pd

# 1. Load both CSV files
logistics_data = pd.read_csv('final_seattle_logistics_weather.csv')
safety_data = pd.read_csv('safety_incidents.csv')

# 2. Tie them together based on the matching 'trip_id'
final_dataset = pd.merge(logistics_data, safety_data, on='trip_id', how='left')

# 3. Save the final result to folder
final_dataset.to_csv('ultimate_portfolio_data.csv', index=False)