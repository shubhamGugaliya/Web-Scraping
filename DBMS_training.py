import sqlite3

#Establish a connection and cursor
connection = sqlite3.connect("data.db")
cursor = connection.cursor()

#Tye of Queries for all data represented by *
cursor.execute("SELECT * FROM events WHERE date='2088-10-15'")
rows= cursor.fetchall()
print(rows)

#cursor.execute("DELETE FROM events WHERE band='tiger")


#Tye of Queries for certain columns in data represented by their name
cursor.execute("SELECT band,date FROM events WHERE date='2088-10-15'")
rows= cursor.fetchall()
print(rows)


#Insert New rows
new_rows = [('Cats', 'Cats City', '2088-10-17'), ('Dog', 'Dogs City', '2088-10-17')]
cursor.executemany("INSERT INTO events VALUES (?,?,?)",new_rows)
connection.commit()

#print all the data
cursor.execute("SELECT * FROM events")
rows= cursor.fetchall()
print(rows)