from geopy.geocoders import Nominatim #Подключаем библиотеку
geolocator = Nominatim(user_agent="Tester") #Указываем название приложения (так нужно, да)
adress = 'Россия, ' + str(input('Введите адрес: ')) #Получаем интересующий нас адрес
location = geolocator.geocode(adress) #Создаем переменную, которая состоит из нужного нам адреса
if location is not None:
    print(location) #Выводим результат: адрес в полном виде
    print(location.latitude, location.longitude) #И теперь выводим GPS-координаты нужного нам адреса
else:
    print('Нужны правильные данные')

#Нижний Тагил, ул.Коминтерна 69-16