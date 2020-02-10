import requests
from bs4 import BeautifulSoup as bs
import csv


url = input('Веведите ссылку на то что надо парсить: ')
page = 1
while page <= 100:
    URL = url + '?page=' + str(page)
    HEADERS = {
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
    }
    PRODUCTS = []

    response = requests.get(URL, headers=HEADERS)
    data = bs(response.content, 'html.parser')

    div = data.find_all('div', attrs={'class': 'dtList i-dtList j-card-item'})
    for divs in div:
        href = divs.find('a', attrs={'class': 'ref_goods_n_p'})['href']
        response_2 = requests.get(href, headers=HEADERS)
        data_tovar = bs(response_2.content, 'html.parser')
        div_tovar = data_tovar.find_all('div', attrs={'class': 'product-content-v1'})
        for divs_tovar in div_tovar:
            title = divs_tovar.find('span', attrs={'class': 'brand'}).text + divs_tovar.find('span', attrs={'class': 'name'}).text
            price = divs_tovar.find('span', attrs={'class': 'final-cost'}).text.split('\n')
            color = divs_tovar.find('span', attrs={'class': 'color'}).text
            PRODUCTS.append({
                'title': title,
                'price': price[1],
                'color': color,
                'href': href
            })

    with open('F:\\Pycharm Projects\\YouTube\\Wildberries\\Save.csv', 'a', encoding='UTF-8', newline='') as file:
        pen = csv.writer(file, delimiter=';')
        i = 0
        if i == 0:
            pen.writerow(('Названия', 'Цена', 'Цвет', 'Ссылка'))
            i += 1
        for PRODUCT in PRODUCTS:
            pen.writerow((PRODUCT['title'], PRODUCT['price'], PRODUCT['color'], PRODUCT['href']))
    print('Successfully page: ' + str(page))
    page += 1
print('Successfully')