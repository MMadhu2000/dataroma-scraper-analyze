import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

url = 'https://www.dataroma.com/m/holdings.php?m=BRK'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) " +
                  "AppleWebKit/537.36 (KHTML, like Gecko) " +
                  "Chrome/120.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'lxml')

table = soup.find('table', {'id': 'grid'})
rows = table.find_all('tr')[1:]

data = []
for row in rows:
    cols = row.find_all('td')
    if len(cols) >= 10:
        stock = cols[1].text.strip()
        shares = cols[4].text.strip()
        price = cols[5].text.strip()
        value = cols[6].text.strip()
        recent_price = cols[8].text.strip()
        change_pct = cols[9].text.strip()
        data.append({
            "Stock": stock,
            "Shares": shares,
            "Reported Price": price,
            "Value": value,
            "Recent Price": recent_price,
            "Change %": change_pct
        })

with open("buffett_holdings.json", "w") as f:
    json.dump(data, f, indent=4)

print("✅ Data scraped and saved to buffett_holdings.json")
