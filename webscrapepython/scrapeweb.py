from csv import writer

import requests
from bs4 import BeautifulSoup

response = requests.get("https://books.toscrape.com/")
soup = BeautifulSoup(response.text, "html.parser")

links = soup.find("body").find_all("a")

with open("links.csv", "w") as csv_file:
    csv_writer = writer(csv_file)
    headers = ["========urls========"]
    csv_writer.writerow(headers)

    for link in links:
        # print(link.get("href"))
        uri = link.get("href")
        csv_writer.writerow([uri])
