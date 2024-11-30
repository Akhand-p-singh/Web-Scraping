# import requests
# from bs4 import BeautifulSoup

# url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers'

# page = requests.get(url) 
# page.text

# soup = BeautifulSoup(page.text, 'lxml') # grabing html as a text(.text) where lxml put that html in proper format. otherwise html will be in single line 
# soup

# #Tags      (All tag will be in output)
# soup.header
# soup.div


# # Navigable Strings

# # 1st it will take HTML from soup variable which we created then 
# # it will extract the header then li tag and then p tag. See the 
# # Navigable or hierarchical approach then to get text use .text or .string

# tag = soup.header.li.p
# print(tag.string)

# # Attributes

# tag = soup.header.a
# print(tag.attrs)     # want some attributes of any tag use .attrs. Here we get attributes of <a> tag.

# ************************************************

import requests
from bs4 import BeautifulSoup

url = 'https://webscraper.io/test-sites/e-commerce/allinone/phones/touch'

page = requests.get(url)
page

soup = BeautifulSoup(page.text, 'lxml')
soup

# Find

soup.find('header')

#print(soup.find('div', {'class': 'container test-site'}))
 
#OR

soup.find('div', class_ ='container test-site')


#Note: For class attribute you can use class_ and for other you have to use dictinary technique like this one- {'class': 'container test-site'}



#Price

   #print(soup.find('h4', class_ = 'float-end price card-title pull-right').text)

#Note:  Difference b/w find And find_all is find will give you only 1st occurance while find_all will give all present tag/element


# find_all

#print(soup.find_all('h4', class_ = 'float-end price card-title pull-right'))

oo = soup.find_all('h4', class_ = 'float-end price card-title pull-right')

#for i in oo:
  ##  print(i.text)

#result_set = print(soup.find_all('p', class_ = 'description card-text').text)

#result_set = soup.find_all('p', class_='description card-text')


#for i in result_set:
 ##   print(i.text)

mobile_name  = soup.find_all('a', class_ = 'title')

#for i in mobile_name:
 ##   print(i.text)



# Find_all part - 2
    
# Calling 2 at a time. in a List    

#print(soup.find_all(['h4', 'p', 'a']))


# Importing Regular Expression

import re

#print(soup.find_all(string =  re.compile('Nok')))

#print(soup.find_all(class_ =  re.compile('pull')))

#print(soup.find_all('p', class_ =  re.compile('pull')))

#Note:  here we used Limit and Regex to get attribute which has name 'pull'

#print(soup.find_all('h4', class_ = re.compile('pull'), limit = 2))


# find_all - 3

#Note: Now we created empyt variable and stored value on those.

name_product = []
product_names = soup.find_all('a', class_ = 'title')
for i in product_names:
    name = i.text
    name_product.append(name)

#print(name_product)


price_product = []
product_price = soup.find_all('h4', class_ = 'float-end price card-title pull-right')
for i in product_price:
    price = i.text
    price_product.append(price)

#print(price_product)


# Now we will create dataframe

import pandas as pd

table101 = pd.DataFrame({'Product_Name': name_product,'Product_Price': price_product})

#print(table)




table101.to_csv('table101.csv', index = False)
#print('DataFrame is written to Excel File successfully.')


# Done and dusted  File Location:   "C:\Users\Akhand Pratap Singh\table101.csv"


# Extract data from Nested HTML tags

# Side Menu

#Note: Use [0] [1] otherwise you will get this error: Did you call find_all() when you meant to call find()?


# menu = soup.find_all('ul', class_ = 'nav', id = 'side-menu')[0]

# print(menu.find_all('a')[1].text)



# ***************** Assignment *****************


# price of the stock

# closing price of the stock

# 52 week range (lower, upper)

# analyst rating

# Stock Price

url = 'https://www.marketwatch.com/investing/stock/aapl?mod=search_symbol'

url2 = requests.get(url)

soup2 = BeautifulSoup(url2.text, 'html.parser')

stock = soup2.find_all('h2', class_ =  'intraday__price')[0]
#print(stock)
print(stock.find('bg-quote', class_ = 'value').text)


closing_price = soup2.find_all('td', class_ = 'table__cell u-semi')[0]
#print(closing_price.text)


lowest = soup2('span', class_ ='primary')[4]
print(lowest.text)

highest = soup2('span', class_ ='primary')[5]
print(highest.text)

no_of_rating = soup2('span', class_ ='count')[0]
print(no_of_rating.text)