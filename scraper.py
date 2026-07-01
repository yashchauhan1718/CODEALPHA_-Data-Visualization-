import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'http://quotes.toscrape.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

quotes = []
for quote in soup.find_all('div', class_='quote'):
    text = quote.find('span', class_='text').text
    author = quote.find('small', class_='author').text
    quotes.append({'Quote': text, 'Author': author})

df = pd.DataFrame(quotes)
df.to_csv('all_quotes.csv', index=False)
print("Dataset 'all_quotes.csv' has been made!")