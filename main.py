import requests
import selectorlib
import smtplib, ssl
import os
import time


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
    with open("data.txt",'a') as file:
        file.write(extractor + "\n")

def read(extracted):
    with open("data.txt",'r') as file:
        return file.read()

if __name__ == "__main__":
    print(scarpe(url))
    while True:
        scraped = scarpe(url)
        extracted = extract(scraped)
        print(extracted)
        content = read(extracted)
        if extracted != "No upcoming tours":
            if extracted not in content:
                store(extracted)
                send_email("Hey, we found a new event")
        print("This is extracted value :",extracted)
        time.sleep(2)