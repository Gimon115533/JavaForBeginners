import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Search(unittest.TestCase):
    def setUp(self):
        self.drv = webdriver.Chrome("chromedriver.exe")

    def test_search(self):
        self.drv.get("https://www.google.com/")
        assert 'Google' in self.drv.title
        elm = self.drv.find_element_by_name('q')
        elm.send_keys('selenide')
        elm.send_keys(Keys.RETURN)
        assert 'No results found' not in self.drv.page_source
        spisok = self.drv.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div[1]/div/div').text
        assert 'selenide.org' in spisok
        baton_more = self.drv.find_element_by_xpath('//*[@id="ow16"]')
        baton_more.click()
        img = self.drv.find_element_by_xpath('//*[@id="lb"]/div/a[1]')
        img.click()
        assert 'selenide' in self.drv.find_element_by_xpath('//*[@id="rg_s"]/div[1]/a[2]').text
        self.drv.find_element_by_xpath('//*[@id="hdtb-msb-vis"]/div[1]/a').click()
        assert 'selenide.org' in spisok

    def tearDown(self):
        self.drv.close()

if __name__ == '__main__':
    unittest.main()
