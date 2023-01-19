import requests
from bs4 import BeautifulSoup as bs

url = ('https://cbr.ru/')
response = requests.get(url).text
soup = bs(response, 'html.parser')
doll = soup.find('div', class_="col-md-2 col-xs-9 _right mono-num")
print(f'Курс доллара на сегодняшний день = {doll.text}')

url_1 = ('https://world-weather.ru/pogoda/russia/makhachkala/')
response_1 = requests.get(url_1).text
soup_1 = bs(response_1, 'html.parser')
weat = soup_1.find('div', id="weather-now-number")
print(f'погода в Махачкале = {weat.text}')

print()

url_2 = ('https://www.rbc.ru/')
response_2 = requests.get(url_2).text
soup_2 = bs(response_2, 'html.parser')
news = soup_2.find('span', class_="main__big__title")
print(f'Главная новость на сегодня:  {news.text}')
