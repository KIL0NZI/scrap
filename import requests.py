import requests
from bs4 import BeautifulSoup
import csv

headers = {
    'User-Agent': '*'
}

url = 'https://www.quickmart.co.ke/fresh'
response = requests.get(url, headers)

soup = BeautifulSoup(response.text, 'html.parser')

titles = soup.find_all('a', class_='products-title')
prices = soup.find_all('span', class_='products-price-new')

with open('naivas_products.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Product Name', 'Price'])

for title, price in zip(titles, prices):
    print(f"{title.text.strip()}: {price.text.strip()}")