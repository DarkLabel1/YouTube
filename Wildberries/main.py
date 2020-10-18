import requests
from bs4 import BeautifulSoup as bs
import csv
import json

tovarsSections = [
    "https://wbxcatalog.wildberries.ru/presets/women_clothes/catalog",
    "https://wbxcatalog.wildberries.ru/men_clothes/catalog",
    "https://wbxcatalog.wildberries.ru/children_things/catalog",
    "https://wbxcatalog.wildberries.ru/children/catalog",
    "https://wbxcatalog.wildberries.ru/accessories/catalog",
    "https://wbxcatalog.wildberries.ru/electronic/catalog",
    "https://wbxcatalog.wildberries.ru/appliances/catalog",
    "https://wbxcatalog.wildberries.ru/books/catalog",
    "https://wbxcatalog.wildberries.ru/sport/catalog",
    "https://wbxcatalog.wildberries.ru/beauty/catalog",
    "https://wbxcatalog.wildberries.ru/toys/catalog",
    "https://wbxcatalog.wildberries.ru/product/catalog",
    "https://wbxcatalog.wildberries.ru/zoo/catalog",
    "https://wbxcatalog.wildberries.ru/stationery/catalog",
    "https://wbxcatalog.wildberries.ru/shealth/catalog",
    "https://wbxcatalog.wildberries.ru/repair/catalog",
    "https://wbxcatalog.wildberries.ru/house/catalog",
    "https://wbxcatalog.wildberries.ru/autoproduct/catalog",
    "https://wbxcatalog.wildberries.ru/jewellery/catalog",
    "https://wbxcatalog.wildberries.ru/event_gift/catalog",
    "https://wbxcatalog.wildberries.ru/adult/catalog?page=1"
]
tovarsLink = []
tovarsContent = []

class Wildberries():

    def __init__(self):
        self.url = "https://www.wildberries.ru"
        self.headers = {
            "accept": "*/*",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
        }
        self.i_ch = 0

    # Принимает 1 переменную urlRequest (ссылка на страницу)
    def req_json(self, urlRequest, page=None):
        r = requests.get(urlRequest, headers=self.headers, params={"page": page}).json()
        return r

    def req(self, urlRequest):
        r = requests.get(urlRequest, headers=self.headers)
        s = bs(r.content, 'html.parser')
        return s

    def catalogTovars(self, catalogTovarsAll):
        for itemProducts in catalogTovarsAll['data']['products']:
            tovarsLink.append({
                "linkProducts": f"https://www.wildberries.ru/catalog/{str(itemProducts['id'])}/detail.aspx"
            })

    # Принимает 1 переменную resultSoup (результат запроса к странице)
    def tovarsContent(self, resultSoup):
        try: tovarsArticle = resultSoup.find("div", attrs={"class": "article"}).find("span").text
        except: tovarsArticle = "None"
        try: tovarsLink = f"https://www.wildberries.ru/catalog/{str(tovarsArticle)}/detail.aspx"
        except: tovarsLink = "None"
        try: tovarsName = resultSoup.find("div", attrs={"class": "brand-and-name"}).text.replace("/n", "").replace("\n", "")
        except: tovarsName = "None"
        try:
            imgLinkAll = resultSoup.find("div", attrs={"class": "card-left"}).find("div", attrs={"class": "photo-items"}).find_all("div", attrs={"class": "slider-item"})
            tovarsImg = ""
            for itemImg in imgLinkAll:
                tovarsImg += str(itemImg.find("a")["href"]) + " | "
        except: tovarsImg = "None"
        try: tovarsPrice = resultSoup.find("div", attrs={"class": "card-right"}).find("div", attrs={"class": "order-block"}).find("span", attrs={"class": "final-cost"}).text.replace("\n", "").replace(" ", "")
        except: tovarsPrice = "None"
        try: tovarsColor = resultSoup.find("div", attrs={"class": "card-right"}).find("div", attrs={"class": "color"}).find("span", attrs={"class": "color"}).text
        except: tovarsColor = "None"
        try:
            tovarsSizesAll = resultSoup.find("div", attrs={"class": "card-right"}).find("div", attrs={"class": "i-sizes-block-v1"}).find("div", attrs={"class": "size-list"}).find_all("label")
            tovarsSize = ""
            for itemSize in tovarsSizesAll:
                tovarsSize += str(itemSize["data-size-name"]) + " | "
        except: tovarsSize = "None"
        try: tovarsBrandLogo = resultSoup.find("div", attrs={"class": "for-brand-logo"}).find("a").find("img")["src"]
        except: tovarsBrandLogo = "None"
        try: tovarsBrandTitle = resultSoup.find("div", attrs={"class": "for-brand-logo"}).find("a").find("img")["alt"]
        except: tovarsBrandTitle = "None"
        try:
            tovarsInformationAll = resultSoup.find("div", attrs={"class": "card-left2"}).find("div", attrs={"class": "card-add-info"}).find("div", attrs={"class": "params"}).find("div", attrs={"class": "params"}).find_all("div", attrs={"class": "pp"})
            tovarsInformation = ""
            for itemInformation in tovarsInformationAll:
                tovarsInformation += itemInformation.find_all("span")[0].text + " : " + itemInformation.find_all("span")[1].text + " | "
        except: tovarsInformation = "None"

        tovarsContent.append({
            "tovarsName": tovarsName,
            "tovarsImg": tovarsImg,
            "tovarsPrice": tovarsPrice,
            "tovarsColor": tovarsColor,
            "tovarsSize": tovarsSize,
            "tovarsBrandLogo": tovarsBrandLogo,
            "tovarsBrandTitle": tovarsBrandTitle,
            "tovarsInformation": tovarsInformation
        })

        with open("marketWildberries.csv", 'a', encoding="UTF-8", newline="") as f:
            pen = csv.writer(f, delimiter='@')
            if self.i_ch == 0:
                pen.writerow(('Артикуль', 'Названия товара', 'Фото товара', 'Цена', 'Цвет', 'Размер', 'Логотип бренда', 'Название бренда', 'Информация', "Ссылка"))
                self.i_ch += 1
            pen.writerow((tovarsArticle, tovarsName, tovarsImg, tovarsPrice, tovarsColor, tovarsSize, tovarsBrandLogo, tovarsBrandTitle, tovarsInformation, tovarsLink))


if __name__ == "__main__":
    obj = Wildberries()
    page = 1
    for o in tovarsSections:
        while True:
            f = obj.req_json(o, page=page)
            if len(f['data']['products']) != 0:
                obj.catalogTovars(f)
                page += 1
                print(f"Страница №{str(page)} загружается.")
            else:
                print(f"Все страницы раздела ({o.split('/')[4]}) загруженны.")
                break
        for i in tovarsLink:
            obj.tovarsContent(obj.req(i["linkProducts"]))
            print(f"Товар ({i}) записан.")