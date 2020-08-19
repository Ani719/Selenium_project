from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome('Drivers/chromedriver.exe')
driver.implicitly_wait(10)
url = 'https://www.seleniumeasy.com/test/basic-checkbox-demo.html'
driver.get(url)

'''def set_check_box(checkbox_element, want_checked):
    if want_checked and not checkbox_element.is_selected():
        checkbox_element.click
    elif checkbox_element.is_selected() and not want_checked:
        checkbox_element.click()

set_check_box()

check = driver.find_element_by_id('isAgeSelected')
check.click()
print(check.is_selected())
print(check.is_enabled())
print(check.is_displayed())'''

checkboxes = driver.find_elements_by_xpath('//input[@type="checkbox"]')
for checkbox in checkboxes:
    if not checkbox.is_selected():
        checkbox.click()








