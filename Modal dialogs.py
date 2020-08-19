import  time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome("Drivers/chromedriver.exe")
driver.implicitly_wait(10)

'''
driver.get('https://www.facebook.com/?stype=lo&jlou=Afd9Z6r')
a = driver.find_element_by_css_selector('a[ajaxify="/reg/spotlight/"]').click()
name = driver.find_element_by_css_selector('input[name="firstname"]').send_keys("Ani")
lastname = driver.find_element_by_css_selector('input[name="lastname"]').send_keys('Manukyan')
phone = driver.find_element_by_css_selector('input[name="reg_email__"]').send_keys(+37494832465)
password = driver.find_element_by_css_selector('input[autocomplete="new-password"]').send_keys('ani')
day_dropdown = driver.find_element_by_id("day")
day = Select(day_dropdown)
day.select_by_index('14')
mounth_dropdown = driver.find_element_by_id('month')
month = Select(mounth_dropdown)
month.select_by_value('4')
year_dropdown = driver.find_element_by_css_selector('select#year')
year = Select(year_dropdown)
year.select_by_visible_text('1995')
gender = driver.find_element_by_css_selector('input[value="1"]')
gender.click()
print(gender.is_selected())
time.sleep(4)
sing_up = driver.find_element_by_css_selector('button[name="websubmit"]').click()
'''





driver.get("http://testautomationpractice.blogspot.com/?")

assert "Automation Testing Practice" in driver.title
pop_up = driver.find_element_by_xpath('//button[@onclick="myFunction()"]').click()
time.sleep(4)
alert = driver.switch_to_alert().accept()     #alert.accept()     #closes alert window with Ok button
#alert.dismiss()  #closes alert window with Cancel button