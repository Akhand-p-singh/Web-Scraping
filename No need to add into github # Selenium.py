# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# driver =  webdriver.Chrome(r"C:\Users\Akhand Pratap Singh\Desktop\WebScraping\chromedriver-win64\chromedriver-win64\chromedriver.exe")

# driver.get('https://www.google.com')


# box = driver.find_element('xpath', '//*[@id="APjFqb"]')
# box.send_keys('poco x3')
# box.send_keys(Keys.ENTER)


# # This is used to click on button, In this case we click on 'Google search' button on google.com [ .click()]

# button = driver.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]').click()   # search bar click
# button2 = driver.find_element('xpath', '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/span/a/h3').click()              # result click flipkart website

# # New

# webpage = driver.find_element('xpath', '/html/body/div[3]/div/div[12]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/span/a/h3').click()





# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Chrome(r"C:\Users\Akhand Pratap Singh\Desktop\WebScraping\chromedriver-win64\chromedriver-win64\chromedriver.exe")

# driver.get('https://www.google.com')

# box = driver.find_element(By.NAME, 'q')
# box.send_keys('poco x3')
# box.send_keys(Keys.ENTER)

# # Wait for the search results to load
# try:
#     search_results = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, 'search'))
#     )

#     # Click on the first search result link
#     first_result = driver.find_element('xpath', '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/span/a/h3')
#     first_result.click()

# except Exception as e:
#     print(f"An error occurred: {e}")

# finally:
#     driver.quit()









# ****************** Screenshot *********************

# driver.save_screenshot('C:\Web Scraping course\screenshot.png')
# driver.find_element_by_xpath('//*[@id="grid-body"]/div/div[1]/div[1]/a/div[1]/div[2]/div/div[1]/span').screenshot('file location where you want to store with file name') 

# *************** Self Scrolling *******************

   # this will give you height of that page.  #3733 is the height when tested

# driver.execute_script('return document.body.scrollHeight')

   # this will scroll till the height of 6000, where 0 is the starting number.
# driver.execute_script('window.scrollTo(0,6000)')


# now scroll till the end with the use of while loop

# while True
# driver.execute_script('window.scrollTo(0, document.body.scrollHeight)') 



# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome(r"C:\Users\Akhand Pratap Singh\Desktop\WebScraping\chromedriver-win64\chromedriver-win64\chromedriver.exe")

# driver.get('https://www.google.com')

# box = driver.find_element('xpath', '//*[@id="APjFqb"]')
# box.send_keys('poco x3')

# box.send_keys(Keys.ENTER)

# # Wait for user input before closing the browser
# input("Press Enter to close the browser...")


# # Close the browser
# driver.quit()






# ************************************ Telegram **************************************

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service

# options = Options()
# options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"
# driver = webdriver.Chrome(
#     options=options,
#     service=Service(
#         r"C:\Users\Akhand Pratap Singh\Desktop\WebScraping\chromedriver-win64\chromedriver-win64\chromedriver.exe"
#     ),
# )
# driver.get("https://www.goat.com/sneakers")
# title = driver.find_element("xpath", '//*[@id="grid-body"]/div/div[1]/div[1]/a/div[1]/div[2]/div/div[1]/span').text
# print(title)
# print("Chrome Browser Invoked")

