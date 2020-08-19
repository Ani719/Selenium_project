from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome('Drivers/chromedriver.exe')
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://www.geeksforgeeks.org/")

element = driver.find_element_by_link_text("Courses")

# create action chain object
action = ActionChains(driver)

# click and hold  the item
action.context_click(on_element=element)

# perform the operation
action.perform()
