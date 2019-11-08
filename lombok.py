import selenium
import unittest
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

url = 'https://www.lombokfastboats.com/'

def getdriver(url):
    """
    Takes one argument, a URL, and returns a web driver object for that URL.
    """
    options = Options()
    # options.add_argument('-headless')
    driver = webdriver.Chrome(executable_path='geckodriver',options=options)
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

    

def fill_date(driver, date):
    departure = driver.find_element_by_id('departure_date')
    WebDriverWait(driver,2)
    departure.clear()
    departure.send_keys(date)

def oneway(driver):
    #fill choice with return or oneway
    pulang = driver.find_element_by_id('oneway').click()
    WebDriverWait(driver,3)

def click(driver):
    button = driver.find_element_by_class_name('search-button')
    button.click()
    WebDriverWait(driver,5)    


if __name__ == '__main__':
    driver = getdriver(url)
    fill_destination(driver,'Bali', 'Nusa Penida')
    fill_date(driver, '2019-11-30')
    WebDriverWait(driver,5)
    oneway(driver)
    WebDriverWait(driver,3)
    click(driver)
    WebDriverWait(driver,5)
    
    