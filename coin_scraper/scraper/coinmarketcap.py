import requests
from bs4 import BeautifulSoup

class CoinMarketCap:
    def scrape(self, coin):
        url = f"https://coinmarketcap.com/currencies/{coin}/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        price = soup.find('div', class_='priceValue___11gHJ').text
        price_change = soup.find('span', class_='sc-15yy2pl-0 feeyND').text


        
        data = {
            'price': price,
            'price_change': price_change,
        }
        return data
