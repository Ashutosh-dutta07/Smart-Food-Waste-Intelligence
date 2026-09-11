import psycopg2
import pandas as pd

# PostgreSQL connection
conn = psycopg2.connect(
    host="127.0.0.1",
    database="food_waste_db",
    user="postgres",
    password="Aa@shu2026",
    port="5433"
)

df = pd.read_csv("food_wastage_data.csv")

cur = conn.cursor()

# Create table
cur.execute("""
CREATE TABLE IF NOT EXISTS food_waste (
    type_of_food VARCHAR(100),
    number_of_guests INTEGER,
    event_type VARCHAR(100),
    quantity_of_food INTEGER,
    storage_conditions VARCHAR(100),
    purchase_history VARCHAR(100),
    seasonality VARCHAR(100),
    preparation_method VARCHAR(100),
    geographical_location VARCHAR(100),
    pricing VARCHAR(100),
    wastage_food_amount INTEGER
)
""")

# Insert data
for _, row in df.iterrows():

    cur.execute("""
        INSERT INTO food_waste (
            type_of_food,
            number_of_guests,
            event_type,
            quantity_of_food,
            storage_conditions,
            purchase_history,
            seasonality,
            preparation_method,
            geographical_location,
            pricing,
            wastage_food_amount
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, tuple(row))

conn.commit()

print("Data imported successfully!")
print("Total rows imported:", len(df))

cur.close()
conn.close()