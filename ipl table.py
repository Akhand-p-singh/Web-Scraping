import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.airbnb.co.in/s/Middle-East/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2024-02-01&monthly_length=3&adults=2&source=structured_search_input_header&search_type=filter_change&price_filter_input_type=0&price_filter_num_nights=5&channel=EXPLORE&date_picker_type=calendar&zoom=3&zoom_level=3&checkin=2024-01-10&checkout=2024-01-17'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')
soup

# while True:

postings = soup.find_all('div', class_ = 'dir dir-ltr')
for post in postings:
    #link = post.find('meta', {'itemprop': 'url'})     
        # name = post.find('meta', {'itemprop':'name'})
        # name2 = post.find('a',class_ = '_1pfo10')
    rating = soup.find('div', class_ = 'r1lutz1s atm_c8_o7aogt atm_c8_l52nlx__oggzyc dir dir-ltr')
    print(rating)
    
#rating.to_csv('C:/Users/Akhand Pratap Singh/Desktop/chimcham11.csv')    
    

# for post in posting:
#     #link = post.find('a', {'rel':"noopener noreferrer nofollow"})
#     link = post.find_all('a', class_ = 'rfexzly atm_9s_1ulexfb atm_7l_1j28jx2 atm_e2_1osqo2v dir dir-ltr')    
#     print(link)
    

    # next_page = soup.find('a', {'aria-label':'Next'}).get('href')
    # next_page_full = 'https://www.airbnb.co.in' +next_page
    # print(next_page_full)

    # url = next_page_full
    # page = requests.get(url)
    # soup = BeautifulSoup(page.text, 'lxml')
    
