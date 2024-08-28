import sqlite3 

connect = sqlite3.connect('Measurements.db') #initialize sql database

cursor = connect.cursor()

create_voltage_measurements_table = """
CREATE TABLE IF NOT EXISTS voltage_measurements (
  date TEXT PRIMARY KEY,
  voltage FLOAT,
  unit TEXT
);
"""
cursor.execute(create_voltage_measurements_table)
connect.commit()
connect.close()
