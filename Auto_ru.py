import requests

URL = 'https://auto.ru/-/ajax/desktop/listing/'

PARAMS = {
     'catalog_filter': [{"mark": "MERCEDES"}],
     'section': "all",
     'category': "cars",
     'sort': "fresh_relevance_1-desc"
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
    'Origin': 'https://auto.ru',
    'Referer': 'https://auto.ru/ryazan/cars/mercedes/all/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0',
    'x-client-app-version': '202002.03.092255',
    'x-client-date': '1580933207763',
    'x-csrf-token': '1c0ed592ec162073ac34d79ce511f0e50d195f763abd8c24',
    'x-page-request-id': '60142cd4f0c0edf51f96fd0134c6f02a',
    'x-requested-with': 'fetch'

}

requests = requests.post(URL, json=PARAMS, headers=HEADERS).json()['offers']

img_url = ''
for req in requests:
    Availability = req['availability']
    Category = req['category']
    Color_hex = str(req['color_hex'])
    Description = str(req['description'])
    Custom_cleared = str(req['documents']['custom_cleared'])
    License_plate = str(req['documents']['license_plate'])
    Owners_number = str(req['documents']['owners_number'])
    PTS = str(req['documents']['pts'])
    VIN = str(req['documents']['vin'])
    Vin_resolution = str(req['documents']['vin_resolution'])
    Year = str(req['documents']['year'])
    Price_rub = str(req['price_info']['RUR'])
    Price_eur = str(req['price_info']['EUR'])
    Price_usd = str(req['price_info']['USD'])
    Salon = req['salon']['is_official']
    Seller = 'Адресс: ' + str(req['seller']['location']) + '\nКоординаты: ' + str(req['seller']['location']['coord']['latitude']) + ':' + str(req['seller']['location']['coord']['longitude'])
    Region = req['seller']['location']['region_info']['name']
    Timezone = req['seller']['location']['timezone_info']['abbr']
    Mileage = req['state']['mileage']
    #for img in req['state']['image_urls']:
    #    img_url += req['state']['image_urls']['sizes']['1200x900'] + '\n'
    Vehicle_info = 'Тип: ' + str(req['vehicle_info']['configuration']['body_type']) + '\nКол-во дверей: ' + str(req['vehicle_info']['configuration']['doors_count']) + '\nКласс автомобиля: ' + req['vehicle_info']['configuration']['auto_class'] + '\nНазвание: ' + req['vehicle_info']['configuration']['human_name'] + '\nОбъем багажника: ' + req['vehicle_info']['configuration']['trunk_volume_min'] + '\nМарка: ' + req['vehicle_info']['mark_info']['name'] + '\nМлдель: ' + req['vehicle_info']['model_info']['name']
    Ik_summary = str(req['lk_summary'])

    print(Availability + '\n' + Category + '\n' + Color_hex + '\n' + Description + '\n' + Custom_cleared + '\n' + License_plate + '\n' + Owners_number + '\n' + PTS + '\n' + VIN + '\n' + Vin_resolution + '\n'
          + Year + '\n' + Price_rub + '\n' + Price_eur + '\n' + Price_usd + '\n' + Salon + '\n' + Seller + '\n' + Region + '\n' + Timezone + '\n' + Mileage + '\n' + img_url + '\n' + Vehicle_info + '\n'
          + Ik_summary)