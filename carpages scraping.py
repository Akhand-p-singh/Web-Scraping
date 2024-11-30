import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://www.carpages.ca/used-cars/search/?fueltype_id%5B0%5D=3&fueltype_id%5B1%5D=7'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')


df = pd.DataFrame({'Link': [''], 'Title':[''], 'Price': [''], 'Desc': [''] })


counter = 0
while counter < 10:
    posting = soup.find_all('div', class_ = 't-flex t-gap-6 t-items-start t-p-6')
    for post in posting:
        des = soup.find('h5', class_ ='hN t-text-gray-500').text
        title = soup.find('h4', class_ ='hN').text
        price = soup.find('span', class_ ='t-font-bold t-text-xl').text.strip()
        link = soup.find('div', class_ ='t-flex t-gap-6 t-items-start t-p-6').find('a').get('href')
        full_link = 'https://www.carpages.ca' + link
        df = df.append({'Link': full_link, 'Title':title, 'Price': price, 'Desc': des }, ignore_index = True)


    next_page = soup.find('a', class_ = 'nextprev').get('href')
    page = requests.get(next_page)
    soup = BeautifulSoup(page.text, 'lxml')
    counter +=1

    

color = soup.find('span', class_ = 't-text-sm t-font-bold').text
print(color)


title = soup.find('h4', class_ ='hN').text
print(title)


des = soup.find('h5', class_ ='hN t-text-gray-500').text
print(des)


price = soup.find('span', class_ ='t-font-bold t-text-xl').text.strip()
print(price)


link = soup.find('div', class_ ='t-flex t-gap-6 t-items-start t-p-6').find('a').get('href')
full_link = 'https://www.carpages.ca' + link
print(full_link)

