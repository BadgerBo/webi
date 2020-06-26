import unittest
from selenium import webdriver


class TestWebi(unittest.TestCase): 

    def setUp(self):
        self.url = 'http://olesyabarsukova.pythonanywhere.com/'
        self.wd = webdriver.Chrome()
        self.wd.get(self.url)

    def test_navigation(self):
        nav_sections = ['experience', 'education', 'skills', 'portfolio', 'contacts']
        for section in nav_sections:
            self.wd.find_element_by_xpath('//nav//td[' + str(nav_sections.index(section) + 1) + ']').click()
            current_ulr = self.wd.current_url[45: -1]
            self.assertEqual(section, current_ulr)
        self.wd.find_element_by_xpath('//header/a').click()
        self.assertEqual('home', self.wd.current_url[45: -1])

    def test_language_switch(self):
        title = self.wd.title
        lang_button = self.wd.find_element_by_xpath('//a/img')
        lang = lang_button.get_attribute('src')[-6: -4]
        if lang == 'ru':
            new_title = 'Олеся Барсукова'
        elif lang == 'en':
            new_title = 'Олеся Барсукова'
        lang_button.click()
        self.assertIn(new_title, self.wd.title)

    def tearDown(self):
        self.wd.quit()
       

if __name__ == '__main__':
    unittest.main()