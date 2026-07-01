import pandas as pd
import sqlite3

# CSV read
df = pd.read_csv("CSV_files/restaurants.csv")

# Create DB
conn = sqlite3.connect("restaurants.db")

# Save as table
df.to_sql(
    "restaurants",      # Table name
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("Database created successfully!")