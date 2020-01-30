import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Programizsearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(r"D:\Drivers\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def test_search_in_programiz(self):
        driver = self.driver
        driver.get("https://www.programiz.com/")
        self.assertIn("Programiz", driver.title)
        elem = driver.find_element_by_xpath("//input[@id = 'edit-keys-2']")
        elem.send_keys("Python string methods")
        elem.send_keys(Keys.RETURN)

        assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()



