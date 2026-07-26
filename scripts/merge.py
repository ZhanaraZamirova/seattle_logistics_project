import pandas as pd

#Step 1
routes = pd.read_csv("routes.csv") #Open routes.csv file
seattle_routes = routes.loc[(routes['destination_city'] == 'Seattle') | (routes['origin_city'] == 'Seattle')] 
#Filter rows where destination and origin city is Seattle 
print(seattle_routes.head()) #Print result 

#Step 2
route_ids = seattle_routes['route_id'].tolist() #Find and filter route ids from seattle_routes (Step 1)
print(route_ids) #Print result 

#Step 3
loads = pd.read_csv('loads.csv') #Open and read loads.csv
seattle_loads = loads.loc[loads['route_id'].isin(route_ids)] #Find and filter route ids that match with Seattle in loads.csv file
print(seattle_loads) #Print result 

#Step 4
load_ids = seattle_loads['load_id'].tolist() #Make a list of load ids from seattle_loads (Step 3)
events = pd.read_csv("delivery_events.csv")  #Open and read delivery_events.csv
seattle_events = events.loc[events['load_id'].isin(load_ids)] #Filter events by load ids. 
print(seattle_events.head())

#Step 5
#Filter the events and keep the ones that physically happened in Seattle
final_seattle_events = seattle_events.loc[seattle_events['location_city'] == 'Seattle']
print(final_seattle_events.head())

#Step 6
weather = pd.read_csv("weather2022-2024.csv", skiprows=3) #Load Weather Data (skip first 3 rows)

#Step 7
#Convert both time columns to official Pandas Datetime objects
weather['time'] = pd.to_datetime(weather['time'])
final_seattle_events['actual_datetime'] = pd.to_datetime(final_seattle_events['actual_datetime'])

#Step 8
#Round the delivery times to the nearest hour so they match the weather 
final_seattle_events['rounded_time'] = final_seattle_events['actual_datetime'].dt.round('h')


#Step 9
#Merging supply chain and weather together
final_dataset = pd.merge(final_seattle_events, weather, left_on='rounded_time', right_on='time', how='inner')
print(final_dataset.head())

#Step 10
#Export the final merged dataset to a CSV file
final_dataset.to_csv('final_seattle_logistics_weather.csv', index=False)