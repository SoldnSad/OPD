from bs4 import BeautifulSoup # импортируем библиотеку BeautifulSoup
import requests # импортируем библиотеку requests

def parse():
    f = open('dromparslab1.txt', 'w')
    url = 'https://auto.drom.ru/region55/new/' # передаем необходимый URL адрес
    page = requests.get(url)                                                     # отправляем запрос методом Get на данный адрес и получаем ответ в переменную
    print(page.status_code)                                                        # смотрим ответ
    soup = BeautifulSoup(page.text, "html.parser") # передаем страницу в bs4

    block = soup.findAll('a', class_='css-4zflqt e1huvdhj1') # находим  контейнер с нужным классом
    for element in block:                                                            # проходим циклом по содержимому контейнера
        price = element.find('span', class_ ="css-46itwz e162wx9x0").text      # записываем в переменную содержание тега
        bull_title = element.find('div', class_ ="css-16kqa8y e3f4v4l2").text
        obshie = element.find('div', class_="css-1fe6w6s e162wx9x0").text
        price = price.replace('\xa0', ' ')
        price = ' | Цена - ' + price[:-1] + 'Руб | '
        bull_title = '| Модель - ' + bull_title
        obshie = obshie + ' |'
        f.write(bull_title)
        f.write(price)
        f.write(obshie)
        f.write('\n')
parse()



