import requests
import os
import time


a = 1
while a <= 99:
    global License_plate, Availability, Category, Color_hex, Description, Custom_cleared, Owners_number, PTS, VIN, Vin_resolution
    global Year, Price_rub, Price_eur, Price_usd, Salon, Seller, Region, Timezone, Mileage, Tip_auto, Count_doors, Class_auto
    global Name_auto, trunk_volume_min, Marka_info, Model_info, Ik_summary
    URL = 'https://auto.ru/-/ajax/desktop/listing/'

    PARAMS = {
         'catalog_filter' : [{"mark": "MERCEDES"}],
         'section': "all",
         'category': "cars",
         'sort': "fresh_relevance_1-desc",
         'page': a
        }
    HEADERS = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        'Connection': 'keep-alive',
        'Content-Length': '137',
        'content-type': 'application/json',
        'Cookie': '_csrf_token=1c0ed592ec162073ac34d79ce511f0e50d195f763abd8c24; autoru_sid=a%3Ag5e3b198b299o5jhpv6nlk0ro4daqbpf.fa3630dbc880ea80147c661111fb3270%7C1580931467355.604800.8HnYnADZ6dSuzP1gctE0Fw.cd59AHgDSjoJxSYHCHfDUoj-f2orbR5pKj6U0ddu1G4; autoruuid=g5e3b198b299o5jhpv6nlk0ro4daqbpf.fa3630dbc880ea80147c661111fb3270; suid=48a075680eac323f3f9ad5304157467a.bc50c5bde34519f174ccdba0bd791787; from_lifetime=1580933172327; from=yandex; X-Vertis-DC=myt; crookie=bp+bI7U7P7sm6q0mpUwAgWZrbzx3jePMKp8OPHqMwu9FdPseXCTs3bUqyAjp1fRRTDJ9Z5RZEdQLKToDLIpc7dWxb90=; cmtchd=MTU4MDkzMTQ3MjU0NQ==; yandexuid=1758388111580931457; bltsr=1; navigation_promo_seen-recalls=true',
        'Host': 'auto.ru',
        'origin': 'https://auto.ru',
        'Referer': 'https://auto.ru/ryazan/cars/mercedes/all/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0',
        'x-client-app-version': '202002.03.092255',
        'x-client-date': '1580933207763',
        'x-csrf-token': '1c0ed592ec162073ac34d79ce511f0e50d195f763abd8c24',
        'x-page-request-id': '60142cd4f0c0edf51f96fd0134c6f02a',
        'x-requested-with': 'fetch'
    }

    response = requests.post(URL, json=PARAMS, headers=HEADERS)
    data = response.json()['offers']

    img_url = []

    i = 0
    while i <= len(data) - 1:
        try: Availability = 'Доступность: ' + str(data[i]['availability'])
        except: License_plate = 'Not availability'

        try: Category = 'Категория: ' + str(data[i]['category'])
        except: Category = 'Not category'

        try: Color_hex = 'Цвет: ' + str(data[i]['color_hex'])
        except: Color_hex = 'Not color'

        try: Description = 'Описание: ' + str(data[i]['description'])
        except: Description = 'Not description'

        try: Custom_cleared = 'Таможня: ' + str(data[i]['documents']['custom_cleared'])
        except: Custom_cleared = 'Not custom cleared'

        try: License_plate = 'Лицензия: ' + str(data[i]['documents']['license_plate'])
        except: License_plate = 'Not license plate '

        try: Owners_number = 'Количество владельцев: ' + str(data[i]['documents']['owners_number'])
        except: Owners_number = 'The number of owners is not specified'

        try: PTS = 'PTS: ' + str(data[i]['documents']['pts'])
        except: PTS = 'Not PTS'

        try: VIN = 'VIN: ' + str(data[i]['documents']['vin'])
        except: VIN = 'Not VIN'

        try: Vin_resolution = 'Vin разрешение: ' + str(data[i]['documents']['vin_resolution'])
        except: Vin_resolution = 'Not vin resolution '

        try: Year = 'Год: ' + str(data[i]['documents']['year'])
        except: Year = 'Not year'

        try: Price_rub = 'Рубли: ' + str(data[i]['price_info']['RUR']) + '₽'
        except: Price_rub = 'Not price rub'

        try: Price_eur = 'Евро: ' + str(data[i]['price_info']['EUR']) + '€'
        except: Price_eur = 'Not price eur'

        try: Price_usd = 'Доллар: ' + str(data[i]['price_info']['USD']) + '$'
        except: Price_usd = 'Not price usd'

        try: Salon = 'С салона: ' + str(data[i]['salon']['is_official'])
        except: Salon = 'Not salon'

        try: Seller = 'Координаты: ' + str(data[i]['seller']['location']['coord']['latitude']) + ':' + str(data[i]['seller']['location']['coord']['longitude'])
        except: Seller = 'Not seller'

        try: Region = 'Регион: ' + str(data[i]['seller']['location']['region_info']['name'])
        except: Region = 'Not region'

        try: Timezone = 'Временная зона: ' + str(data[i]['seller']['location']['timezone_info']['abbr'])
        except: Timezone = 'Not timezone'

        try: Mileage = 'Пробег: ' + str(data[i]['state']['mileage'])
        except: Mileage = 'Not mileage'

        for img in data[i]['state']['image_urls']:
            img_url.append(img['sizes']['1200x900'])

        try: Tip_auto = 'Тип автомобиля: ' + str(data[i]['vehicle_info']['configuration']['body_type'])
        except: Tip_auto = 'Not tip auto'

        try: Count_doors = 'Колличество дверей: ' + str(data[i]['vehicle_info']['configuration']['doors_count'])
        except: Count_doors = 'Not count doors'

        try: Class_auto = 'Класс автомобиля: ' + str(data[i]['vehicle_info']['configuration']['auto_class'])
        except: Class_auto = 'Not class auto'

        try: Name_auto = 'Имя автомобиля: ' + str(data[i]['vehicle_info']['configuration']['human_name'])
        except: Name_auto = 'Not name auto'

        try: trunk_volume_min = 'Объем багажника: ' + str(data[i]['vehicle_info']['configuration']['trunk_volume_min'])
        except: trunk_volume_min = 'Not trunk volume min'

        try: Marka_info = 'Марка автомобиля: ' + str(data[i]['vehicle_info']['mark_info']['name'])
        except: Marka_info = 'Not marka info'

        try: Model_info = 'Модель автомобиля: ' + str(data[i]['vehicle_info']['model_info']['name'])
        except: Model_info = 'Not model info'

        try: Ik_summary = 'Информация: ' + str(data[i]['lk_summary'])
        except: Ik_summary = 'Not ik summary'

        link_img = ''
        for link_img_0 in img_url:
            link_img += str(link_img_0) + '\n'


        text_razdelitely1 = '================================================================================================================================='
        text_razdelitely2 = '================================================================================================================================='
        text_razdelitely3 = '=================================================================================================================================\n'
        text = str(License_plate) + '\n' + str(Availability) + '\n' + str(Category) + '\n' + str(Color_hex) + '\n' + str(Description) + '\n' + str(Custom_cleared) + '\n' + str(Owners_number) + '\n' + str(PTS) + '\n' + str(VIN) + '\n' + str(Vin_resolution) + '\n' + str(Year) + '\n' + str(Price_rub) + '\n' + str(Price_eur) + '\n' + str(Price_usd) + '\n' + str(Salon) + '\n' + str(Seller) + '\n' + str(Region) + '\n' + str(Timezone) + '\n' + str(Mileage) + '\n' + str(Tip_auto) + '\n' + str(Count_doors) + '\n' + str(Class_auto) + '\n' + str(Name_auto) + '\n' + str(trunk_volume_min) + '\n' + str(Marka_info) + '\n' + str(Model_info) + '\n' + str(Ik_summary) + '\n' + text_razdelitely1 + '\n' + text_razdelitely2 + '\n' + text_razdelitely3

        with open('Save_auto1.txt', 'a', encoding='UTF-8') as file:
            file.write(text)
        i += 1
    print('Page: ' + str(a))
    a += 1

print('Successfully')