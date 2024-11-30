import requests
from bs4 import BeautifulSoup
import pandas as pd

# url = 'https://www.worldometers.info/world-population/'

# page = requests.get(url)
# page

# soup =BeautifulSoup(page.text, 'lxml')
# #print(soup)

# table = soup.find('table', class_ = 'table table-striped table-bordered table-hover table-condensed table-list')
# #print(table)

# table.find_all('th')

# headers = []

# for i in table.find_all('th'):
#     title = i.text
#     headers.append(title)

# #print(headers)

# df = pd.DataFrame(columns = headers)

# for j in table.find_all('tr')[1:]:
#     row_data = j.find_all('td')
#     row = [tr.text for tr in row_data]
#     length = len(df)
#     df.loc[length] = row


# print(row)
# df.to_csv('C:/Users/Akhand Pratap Singh/Desktop/file_name1.csv')


url = 'https://www.nfl.com/standings/league/2019/REG'

page1 = requests.get(url)

soup1 = BeautifulSoup(page1.text, 'lxml')
#print(soup1)


table = soup1.find_all('table', {'summary': 'Standings - Detailed View'})
#print(table)

heading = []

for k in soup1.find_all('th'):
    head = k.text.strip()
    heading.append(head)
#print(heading)
    
df1 = pd.DataFrame(columns = heading)
    
for k in soup1.find_all('tr')[1:]:
   table_cont =  k.find_all('td')
   content = [td.text.strip() for td in table_cont]
   leng = len(df1)
   df1.loc[leng] = content


df1.to_csv(r'C:\Users\Akhand Pratap Singh\Desktop\WebScraping\NFL Project\NFL_raw_data.csv')





