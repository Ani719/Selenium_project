
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonSearch(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome(r"D:\Drivers\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()


    def test_search_in_python(self):
        driver = self.driver
        driver.get("https://www.python.org/")
        self.assertIn('Python', driver.title)
        element = driver.find_element_by_css_selector("input.search-field")
        element.send_keys("downloads")
        element.send_keys(Keys.RETURN)

        assert "No results found." not in driver.page_source


    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
     unittest.main()
