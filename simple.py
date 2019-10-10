import selenium
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def getdriver(url):
    options = Options()
    options.add_argument('-headless')
    driver = Firefox(executable_path='geckodriver', options=options)
    driver.get(url)
    wait = WebDriverWait(driver,5).until(EC.presence_of_element_located(by.ID,'one-way-option'))
    return driver

def fillform(driver, port_from, port_to, date):
    search_field = driver.find_element_by_name('destination_from')
    search_field.send_keys(port_from)
    search_field2 = driver.find_element_by_name('destination_to')
    search_field2.send_keys(port_to)
    search_date = driver.find_element_by_name('depart_date')
    search_date.send_keys(date)
    passenger = driver.find_element_by_class_name('adult prequired', value='2')

