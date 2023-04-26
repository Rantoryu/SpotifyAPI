import sqlite3
import pandas as pd

connection = sqlite3.connect('tracks.sqlite')
df = pd.read_sql_query("SELECT * FROM tracks", connection)
print(df)
connection.commit()
connection.close()