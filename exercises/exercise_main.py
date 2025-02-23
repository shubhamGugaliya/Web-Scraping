import requests
import selectorlib
from datetime import datetime
import time
import sqlite3

#Establish a connection and cursor
connection = sqlite3.connect("exercise_data.db")


url = "https://programmer100.pythonanywhere.com/"

now = datetime.now()
formatted = now.strftime("%Y-%m-%d %H:%M:%S")


def scarpe(url):
    """Scrape the web page from URL"""
    response = requests.get(url)
    source = response.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("rexercise_extract.yaml")
    value = extractor.extract(source)
    return value

def store(extractor):
    row = [formatted,extractor['tours']]
    # Queries to write data
    cursor = connection.cursor()
    cursor.execute("INSERT INTO events VALUES (?,?)", row)
    connection.commit()

# def read(extracted):
#     row = extracted.split(",")
#     row = [item.strip() for item in row]
#     band,city,date = row
#     # Queries to read all data
#     cursor = connection.cursor()
#     cursor.execute("SELECT * FROM events WHERE band=? AND city = ? AND date = ?",(band,city,date))
#     rows = cursor.fetchall()
#     print(rows)
#     return rows

if __name__ == "__main__":
    while True:
        scraped = scarpe(url)
        extracted = extract(scraped)
        print(extracted)
        store(extracted)
        time.sleep(2)
