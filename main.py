import requests
import selectorlib
import smtplib, ssl
import os
import time
import sqlite3

#Establish a connection and cursor
connection = sqlite3.connect("data.db")



url = "https://programmer100.pythonanywhere.com/tours/"

def scarpe(url):
    """Scrape the web page from URL"""
    response = requests.get(url)
    source = response.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)['tours']
    return value

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "shubham.gugaliya5496@gmail.com"
    password = "rxcl gqml hpzr uaby"

    receiver = "shubham.gugaliya5496@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

def store(extractor):
    row = extracted.split(",")
    row = [item.strip() for item in row]
    # Queries to write data
    cursor = connection.cursor()
    cursor.execute("INSERT INTO events VALUES (?,?,?)", row)
    connection.commit()

def read(extracted):
    row = extracted.split(",")
    row = [item.strip() for item in row]
    band,city,date = row
    # Queries to read all data
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM events WHERE band=? AND city = ? AND date = ?",(band,city,date))
    rows = cursor.fetchall()
    print(rows)
    return rows

if __name__ == "__main__":
    print(scarpe(url))
    while True:
        scraped = scarpe(url)
        extracted = extract(scraped)
        print(extracted)

        if extracted != "No upcoming tours":
            row = read(extracted)
            if not row:
                store(extracted)
                send_email("Hey, we found a new event")
        print("This is extracted value :",extracted)
        time.sleep(2)