from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Chrome('Drivers/chromedriver.exe')
driver.implicitly_wait(10)


driver.get('http://testautomationpractice.blogspot.com/?')
speed_drop = driver.find_element_by_id("speed")
elem = Select(speed_drop)
elem.select_by_index(1)








'''driver.get('https://www.facebook.com/')

dropdownmenu = driver.find_element_by_id('day')
select_element = Select(dropdownmenu)
select_element.select_by_index('14')
time.sleep(2)


def click_dropdown_menu_by_id(driver, dropdown_id, option_text):
    dropdown_element = driver.find_element_by_id('dropdown_id')
    dropdown_element.click()
    option_element = driver.find_element_by_link_text('option_text')
    option_element.click()

click_dropdown_menu_by_id("webdriver.Chrome", "day", "14")'''