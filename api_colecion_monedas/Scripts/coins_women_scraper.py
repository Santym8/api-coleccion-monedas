import json
from bs4 import BeautifulSoup
import requests

def download_img(img_url, img_name):
    url_save = f'img/American Women Quarters/{img_name}.jpg'
    req = requests.get(img_url)
    response = req.content
    file = open(url_save, "wb")
    file.write(response)
    file.close()
    return  f'img/American Women Quarters/{img_name}.jpg'

url = 'https://www.usmint.gov/learn/kids/about-the-mint/american-women-quarters'

page_response = requests.get(url, timeout=5)
page_content = BeautifulSoup(page_response.content, "html.parser")

coins = []
divs = page_content.find_all('div',class_= "feature-group group-type-2")
count = 1
for div in divs:
    internal_divs = div.find_all('div')
    year = internal_divs[0].text  
    coint_containers = internal_divs[1].find_all('div')
    for coin_container in coint_containers:
       name = coin_container.find('div', class_='mint-feature-caption')
       if name != None:
        img =  coin_container.find('img')['src']
        coin = {
            'id_collection': 3,
            'coin_number':count,
            'name':name.text,
            'year':year,
            'image':download_img(img, f'{count}.{name.text}'),
            }
        count +=1
        coins.append(coin)

with open('Scripts/json/women.json', 'w') as outfile:
    json.dump(coins, outfile)


