from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('Drivers/chromedriver.exe')
driver.implicitly_wait(10)
driver.maximize_window()
url = 'https://www.guru99.com/click-on-image-in-selenium.html'
driver.get(url)

image = driver.find_element_by_css_selector('img[alt="Guru99"]').click()
testing = driver.find_element_by_css_selector('a[title="Software Testing"]').click()