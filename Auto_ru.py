import requests

a = 1 #Переменная для перехода по страницам
while a <= 99: #Всего страниц на сайте
    #ббъявляем переменным глобально
    global License_plate, Availability, Category, Color_hex, Description, Custom_cleared, Owners_number, PTS, VIN, Vin_resolution
    global Year, Price_rub, Price_eur, Price_usd, Salon, Seller, Region, Timezone, Mileage, Tip_auto, Count_doors, Class_auto
    global Name_auto, trunk_volume_min, Marka_info, Model_info, Ik_summary

    URL = 'https://auto.ru/-/ajax/desktop/listing/' #URL на который будет отправлен запрос

    #Параметры запроса
    PARAMS = {
        'catalog_filter': [{"mark": "MERCEDES"}],
        'section': "all",
        'category': "cars",
        'sort': "fresh_relevance_1-desc",
        'page': a
    }

    #Заголовки страницы
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

    response = requests.post(URL, json=PARAMS, headers=HEADERS) #Делаем post запрос на url
    data = response.json()['offers'] #Переменная data хранит все полученные объявления

    img_url = []

    i = 0 #Переменная для перехода по объявлениям
    while i <= len(data) - 1: #len(data)-1 это количество пришедших объявлений
        # Доступность объявления
        try: Availability = 'Доступность: ' + str(data[i]['availability'])
        except: Availability = 'Not availability'

        #Категория автомобиля
        try: Category = 'Категория: ' + str(data[i]['Category'])
        except: Category = 'Not category'

        #Цвет автомобиля (возвращается в формате hex)
        try: Color_hex = 'Цвет: #' + str(data[i]['color_hex'])
        except: Color_hex = 'Not color'

        #Описание автомобиля
        try: Description = 'Описание: ' + str(data[i]['description'])
        except: Description = 'Not description'

        #Растаможен ли автомобиль (возвращает либо True, либо False)
        try: Custom_cleared = 'Таможня: ' + str(data[i]['documents']['custom_cleared'])
        except: Custom_cleared = 'Not custom cleared'

        #Лицензия на автомобиль
        try: License_plate = 'Лицензия: ' + str(data[i]['documents']['license_plate'])
        except: License_plate = 'Not license plate'

        #Количество владельцев автомобиля
        try: Owners_number = 'Количество владельцев автомобиля: ' + str(data[i]['documents']['owners_number'])
        except: Owners_number = 'Not owners number'

        #PTS автомобиля
        try: PTS = 'PTS: ' + str(data[i]['documents']['pts'])
        except: PTS = 'Not pts'

        #VIN автомобиля
        try: VIN = 'VIN' + str(data[i]['documents']['vin'])
        except: VIN = 'Not vin'

        try: Vin_resolution = 'Vin разрашение: ' + str(data[i]['documents']['vin_resolution'])
        except: Vin_resolution = 'Not Vin resolution'

        #Год выпуска автомобиля
        try: Year = 'Год: ' + str(data[i]['documents']['year'])
        except: Year = 'Not year'

        #Цена в рублях, в евроб и долларах
        try: Price_rub = 'Рубли: ' + str(data[i]['price_info']['RUR']) + '₽'
        except: Price_rub = 'Not price rub'

        try: Price_eur = 'Евро: ' + str(data[i]['price_info']['EUR']) + '€'
        except: Price_eur = 'Not price eur'

        try: Price_usd = 'Доллар: ' + str(data[i]['price_info']['USD']) + '$'
        except: Price_usd = 'Not price usd'

        #С салона ли машина, или нет
        try: Salon = 'С салона: ' + str(data[i]['salon']['is_official'])
        except: Salon = 'Not salon'

        #Координаты места нахождения автомобиля
        try: Seller = 'Координаты: ' + str(data[i]['seller']['location']['coord']['latitude']) + ':' + str(data[i]['seller']['location']['coord']['longitude'])
        except: Seller = 'Not seller'

        #Регион, в котором находится автомобиль
        try: Region = 'Регион: ' + str(data[i]['seller']['location']['region_info']['name'])
        except: Region = 'Not region'

        #Временная зона в котором находится автомобиль
        try: Timezone = 'Временная зона: ' + str(data[i]['seller']['location']['timezone_info']['abbr'])
        except: Timazone = 'Not timezone'

        #Пробег автомобиля
        try: Mileage = 'Пробег: ' + str(data[i]['state']['mileage'])
        except: Mileage = 'Not mileage'

        #Картинки автомобиля
        #Возвращается несколько фото, мы их добавляем в словарь img_url
        for img in data[i]['state']['image_urls']:
            img_url.append(img['sizes']['1200x900'])

        #Тип автомобиля
        try: Tip_auto = 'Тип автомобиля: ' + str(data[i]['vehicle_info']['configuration']['body_type'])
        except: Tip_auto = 'Not tip auto'

        #Количество дверей автомобиля
        try: Count_doors = 'Количество дверей: ' + str(data[i]['vehicle_info']['configuration']['doors_count'])
        except: Count_doors = 'Not count doors'

        #Класс автомобиля
        try: Class_auto = 'Класс автомобиля: ' + str(data[i]['vehicle_info']['configuration']['auto_class'])
        except: Class_auto = 'Not class auto'

        #Название автомобиля
        try: Name_auto = 'Название автомобиля: ' + str(data[i]['vehicle_info']['configuration']['human_name'])
        except: Name_auto = 'Not name auto'

        #Объем багажника автомобиля
        try: trunk_volume_min = 'Объём багажника: ' + str(data[i]['vehicle_info']['configuration']['trunk_volume_min'])
        except: trunk_volume_min = 'Not trunk volume min'

        #Марка автомобиля
        try: Marka_info = 'Марка автомобиля: ' + str(data[i]['vehicle_info']['mark_info']['name'])
        except: Marka_info = 'Not marka info'

        #Модель автомобиля
        try: Model_info = 'Модель автомобиля: ' + str(data[i]['vehicle_info']['model_info']['name'])
        except: Model_info = 'Not model info'

        #Информация об автомобиле
        try: Ik_summary = 'Информация: ' + str(data[i]['Ik_summary'])
        except: Ik_summary = 'Not ik summary'

        link_img = '' #Переменная для ссылок
        for link_img_0 in img_url: #Перебираем ссылки из словаря img_url, и записываем их в одну переменную текстом
            link_img += str(link_img_0) + '\n'

        #Переменная для разделения записей
        text_razdelitely1 = '======================================================================='
        text_razdelitely2 = '======================================================================='
        text_razdelitely3 = '=======================================================================\n'

        #Переменные в которую всё записываем
        text = License_plate + '\n' + Availability + '\n' + Category + '\n' + Color_hex + '\n' \
               + Description + '\n' + Custom_cleared + '\n' + Owners_number+ '\n' + PTS + '\n' + VIN + '\n' + Vin_resolution + '\n' +\
               Year + '\n' + Price_rub + '\n' + Price_eur + '\n' + Price_usd + '\n' + Salon + '\n' + Seller + '\n' + Region + '\n' + \
               Timezone + '\n' + Mileage + '\n' + Tip_auto + '\n' + Count_doors + '\n' + Class_auto + '\n' + Name_auto + '\n' + \
               trunk_volume_min + '\n' + Marka_info + '\n' + Model_info + '\n' + Ik_summary + '\n' + link_img + '\n' + text_razdelitely1  + '\n' + text_razdelitely2 + '\n' + text_razdelitely3

        #Записываем переменную text в файл
        with open('Save_auto.txt', 'a', encoding='UTF-8') as file: #Открываем файл Save_auto.txt (создаётся автоматически), на дозапись (ключ a)
            file.write(text) #Записываем
        i += 1 #Увеличиваем переменную перехода по объявлениям на 1
    print('Page: ' + str(a)) #Выводим сообщение, какая страница записалась
    a += 1 #Увеличиваем переменную страницы сайта на 1

print('Successfully') #Выводим сообщение об успешном выполнении