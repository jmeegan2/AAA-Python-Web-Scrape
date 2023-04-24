import requests
import requests
from bs4 import BeautifulSoup

url = "https://gasprices.aaa.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

response = requests.get(url, headers=headers)
html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")

print(html_content)
price_div = soup.find("div", class_="mobi-average-price mobi-average-price--red")
price = price_div.find("p", class_="price-text price-text--red").text.strip()
date = price_div.find("p").text.strip()

print(price)
print(date)