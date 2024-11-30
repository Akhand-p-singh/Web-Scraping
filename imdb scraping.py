
# 1.  set google as your starting page and type in top 100 movies of all time in the box.
# 2.  press enter and then click on the the link corresponding  to imdb
# 3.  create a wait time  for the entire page to load
# 4.  scroll a!! the way down to where the jaws appear 
# 5.  take screen shot of the actual page, and get the image of the jaws(movie name) poster


from selenium import webdriver

# importing keys (send_keys, Enter and all)
from selenium.webdriver.common.keys import Keys          

# to use of time eg. time.sleep(2)
import time                                              

# chrome driver location
driver = webdriver.Chrome(r'C:\Users\Akhand Pratap Singh\Desktop\WebScraping\chromedriver-win64\chromedriver-win64\chromedriver.exe')   

 # website to open
driver.get('https://www.google.com')                                       

# xpath of search bar of google where we put keywords to search
box = driver.find_element('xpath', '//*[@id="APjFqb"]')                      
 
# keywords 
box.send_keys('top 100 movies of all time')                                

# After mentioning keywords pressing Enter  through library
box.send_keys(Keys.ENTER)                                                

# Finding particular result in this case IMDB. and click on that result
imdb_page = driver.find_element('xpath', '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/span/a/h3').click()           


# this will give you total height of page
#driver.execute_script('window.scrollTo(0, document.body.scrollHeight)') 


driver.execute_script('window.scrollTo(0,11200)')

# Click_more is not working don't know why
#click_more = driver.find_element('xpath', '//*[@id="__next"]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[2]/div[2]/div/span').click()
driver.save_screenshot(r'C:\Users\Akhand Pratap Singh\Desktop\WebScraping\cccc.png')


#Movie Screenshot
ss = driver.find_element('xpath', '//*[@id="__next"]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[2]/ul/li[50]').screenshot(r'C:\Users\Akhand Pratap Singh\Desktop\WebScraping\movie.png')

# Movie poster screenshot
ss1 = driver.find_element('xpath', '//*[@id="__next"]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[2]/ul/li[50]/div[1]/div/div/div[1]/div[1]/div/a/div').screenshot(r'C:\Users\Akhand Pratap Singh\Desktop\WebScraping\movie_poster.png')
time.sleep(10)  