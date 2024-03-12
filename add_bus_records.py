import sqlite3
# Step 1: Connect to the SQLite database
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()
print("connect to database")
# Step 3: Define a function to insert bus records into the database
def add_bus_record(bus_name, source, dest, nos, rem, price, date, time):
    cursor.execute('''INSERT INTO myapp_bus (bus_name, source, dest, nos, rem, price, date, time)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', (bus_name, source, dest, nos, rem, price, date, time))
    conn.commit()
    print("Bus record added successfully.")
    a = "Bus record added successfully."
    return a
# Step 4: Add bus records
add_bus_record("BUS001", "mumbai", "hyd", "12", "10", "1800", "2024-03-13", "20:00")
add_bus_record("BUS001", "mumbai", "hyd", "15", "5", "2000", "2024-03-14", "22:00")

# Step 5: Close the database connection
conn.close()
