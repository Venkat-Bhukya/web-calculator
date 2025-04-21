import requests
from bs4 import BeautifulSoup
import csv
import json

def scrape_website(url, element, attrs={}, output_format='csv'):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    items = soup.find_all(element, attrs=attrs)

    results = [{"text": item.get_text(strip=True), "link": item.get("href")} for item in items]

    if output_format == 'csv':
        with open("output.csv", "w", newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=["text", "link"])
            writer.writeheader()
            writer.writerows(results)
    else:
        with open("output.json", "w", encoding='utf-8') as f:
            json.dump(results, f, indent=2)

    return results