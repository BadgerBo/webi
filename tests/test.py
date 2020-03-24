import unittest
from selenium import webdriver


URL = 'http://olesyabarsukova.pythonanywhere.com/'


class TestWebi(unittest.TestCase):   

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_connection(self):
        self.driver.get(URL)
        self.assertIn('Olesya Barsukova', self.driver.title)

    def test_language_switch(self):
        self.driver.get(URL)
        lang_button = self.driver.find_element_by_xpath('//a/img')
        lang_button.click()
        self.assertIn('Олеся Барсукова', self.driver.title)

    def tearDown(self):
        self.driver.close()
       

if __name__ == '__main__':
    unittest.main()