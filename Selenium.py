import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from xml.dom import minidom

class Programizsearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\Program Files\Drivers\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def test_search_in_programiz(self):
        myfile = minidom.parse('Locators.xml')
        locators = myfile.getElementsByTagName('locator')
        baseurl = locators[0].firstChild.data
        Search_field = locators[2].firstChild.data
        Search_result = locators[3].firstChild.data
        Go = locators[3].firstChild.data
        driver = self.driver
        driver.get(baseurl)
        assert "Programiz" in driver.title
        elem = self.driver.find_element_by_xpath(Search_field)
        elem.send_keys("Python string methods")
        button = self.driver.find_element_by_class_name(Go)
        button.click()
        assert "No results found." not in driver.page_source
        list = self.driver.find_elements_by_class_name(Search_result)
        print(str(len(list)))

        for element in list:
            print(element.get_attribute(".text"))


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()