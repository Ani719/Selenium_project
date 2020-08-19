import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('Drivers/chromedriver.exe')
driver.implicitly_wait(10)
driver.maximize_window()
url = 'https://www.guru99.com/'
driver.get(url)

assert driver.current_url == 'https://www.guru99.com/'
links = driver.find_elements_by_tag_name('a')
for link in links:
    response = requests.head(link.get_attribute('href'))
    print(link.text, link.get_attribute('href'), response)


driver.close()
'''print(link.text + " " + link.get_attribute("href"))
#print(len(links))'''



