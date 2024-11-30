from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

driver = webdriver.Chrome(r'C:\Users\Akhand Pratap Singh\Desktop\WebScraping\chromedriver-win64\chromedriver-win64\chromedriver.exe')

driver.get('https://www.nike.com/in/w/sale-3yaep')


# # This will give you height of that  page
last_height = driver.execute_script('return document.body.scrollHeight')

while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(2)
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height == last_height:
        break
    last_height = new_height

#becoz we using selenium we tried this you can also use that beautifulsoup things
soup = BeautifulSoup(driver.page_source, 'lxml')

product_card = soup.find_all('div', class_ = 'product-card__body')

#created dataframe

df = pd.DataFrame({'Link':[''], 'Name':[''], 'Description':[''], 'Price':[''], 'Discounted_Price':[''] })


for product in product_card:
    try:
        link = product.find('a', class_ = 'product-card__img-link-overlay').get('href')
        name = product.find('div', class_ = 'product-card__title').text
        desc = product.find('div', class_ = 'product-card__subtitle').text
        full_price = product.find('div', class_ = 'product-price in__styling is--striked-out css-0').text
        discounted_price = product.find('div', class_ = 'product-price is--current-price css-1ydfahe').text
    
        df = df.append({'Link':link, 'Name': name, 'Description':desc, 'Price': full_price, 'Discounted_Price': discounted_price}, ignore_index = True )
    except: 
        pass
    

df.to_csv(r'C:\Users\Akhand Pratap Singh\Desktop\WebScraping\Nike Project\nike_product_page_raw_data.csv')
