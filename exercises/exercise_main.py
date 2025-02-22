import requests
import selectorlib
from datetime import datetime
import time

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
    with open("exer_data.txt",'a') as file:
        file.write(extractor + "\n")

def read(extracted):
    with open("exer_data.txt",'r') as file:
        return file.read()

if __name__ == "__main__":
    while True:
        scraped = scarpe(url)
        extracted = extract(scraped)
        store(f"{formatted},{extracted['tours']}")
        time.sleep(2)
