from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('Drivers/chromedriver.exe')
driver.implicitly_wait(10)
driver.get('https://github.com/')
assert driver.current_url == 'https://github.com/'
sign_in = driver.find_element_by_link_text('Sign in')
sign_in.click()
username = driver.find_element_by_id('login_field')
username.send_keys('Ani719')
password = driver.find_element_by_xpath('//input[@name="password"]')
password.send_keys('Manukyan719')
sign_in_button = driver.find_element_by_xpath('//input[@name = "commit"]')
sign_in_button.click()

#driver.quit()