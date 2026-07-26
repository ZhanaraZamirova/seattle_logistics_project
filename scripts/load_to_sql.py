import pandas as pd
import sqlite3

# 1. Load the final CSV 
df = pd.read_csv('final_seattle_logistics_weather.csv')

# 2. Create a connection to the database
conn = sqlite3.connect('seattle_supply_chain.db')

# 3. Push the dataframe into a SQL table
df.to_sql('logistics_weather_impact', conn, if_exists='replace', index=False)

# 4. Write SQL query
query = "SELECT * FROM logistics_weather_impact;"

# 5. Ask Pandas to run the SQL query and print the result
test_result = pd.read_sql(query, conn)
print(test_result)

# 6. Close the connection in the end
conn.close()