import selenium
import unittest
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

url = 'https://www.lombokfastboats.com/'

class tester_selenium(unittest.TestCase):
        
    def getdriver(url):
        """
        Takes one argument, a URL, and returns a web driver object for that URL.
        """
        options = Options()
        options.add_argument('-headless')
        driver = Firefox(executable_path='geckodriver', options=options)
        driver.get(url)
        wait = WebDriverWait(driver,3)
        return driver
        
        
    def fill_destination(driver, from_, to_):
        dari = driver.find_element_by_id('departure_region_id')
        Select(dari).select_by_visible_text(from_)
        WebDriverWait(driver,2)
        ke = driver.find_element_by_id('arrival_region_id')
        Select(ke).select_by_visible_text(to_)
        WebDriverWait(driver,2)
        assert 'No results found.' not in driver.page_source

    def fill_date(driver, date):
        departure = driver.find_element_by_id('departure_date')
        WebDriverWait(driver,2)
        departure.send_keys(date)    


    if __name__ == '__main__':
        unittest.main()