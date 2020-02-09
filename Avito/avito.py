import requests
from bs4 import BeautifulSoup as bs

global price

data = []
URL = 'https://www.avito.ru/ryazan/avtomobili/s_probegom?radius=200&q=автомобили'
HEADERS = {
    'accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}

response = requests.get(URL, HEADERS)
soup = bs(response.content, 'html.parser')

div = soup.find_all('div', attrs={'class': 'snippet-horizontal item item_table clearfix js-catalog-item-enum item-with-contact js-item-extended'})
for divs in div:
    title = divs.find('a', attrs={'class': 'snippet-link'}).text
    href = divs.find('a', attrs={'class': 'snippet-link'})['href']
    try: price = divs.find('span', attrs={'class': 'price price_highlight'}).text
    except: price = divs.find('span', attrs={'class': 'price'}).text
    description = divs.find('div', attrs={'class': 'specific-params specific-params_block'}).text
    #time = divs.find('div', attrs={'class': 'js-item-date c-2'}).text
    print(href)
    #data.append({
    #    'Title': title,
    #    'Price': price,
    #    'Description': description,
    #    'Time': time
    #})
