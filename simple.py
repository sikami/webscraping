import unittest
import selenium
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
import csv

url = 'https://bluewater-express.com/'
def getdriver(url):
    options = Options()
    options.add_argument('-headless')
    driver = Firefox(executable_path='geckodriver', options=options)
    driver.get(url)
    wait = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.ID,'one-way-option')))
    return driver

def fillform(driver, port_from, port_to):
    
    search_field = driver.find_element_by_name('destination_from')
    Select(search_field).select_by_visible_text(port_from)
    search_field2 = driver.find_element_by_name('destination_to')
    Select(search_field2).select_by_visible_text(port_to)
    search_date = driver.find_element_by_name('depart_date').click()
    #wait implicit wait
    WebDriveWait(driver, timeout=4).until(EC.implicitly_Wait((4)))
    search_month = driver.find_element_by_xpath("//div//select[@class='ui-datepicker-month']")
    month = search_month.select_by_visible_text('November')
    time.sleep(2)
    search_year = driver.find_element_by_xpath("//div//select[@class='ui-datepicker-year']")
    year = search_year.select_by_visible_text('2019')
    time.sleep(2) 
    search_day = driver.find_element_by_xpath("//div//select[@class='ui-state-default']")
    day = search_day.select_by_visible_text('25')
    time.sleep(2)
    passenger = driver.find_element_by_class_name('adult prequired')
    Select(passenger).select_by_visible_text('2')
    driver.find_element_by_class_name('search-avaibility').click()
    wait = WebDriverWait(driver,timeout=10).until(EC.presence_of_element_located((By.CLASS_NAME, 'destination-name')))

if __name__ == '__main__':
    try:
        driver = getdriver(url)
        fillform(driver, 'Padang Bai', 'Gili Trawangan')
        
    finally:
        driver.quit()
# def scrape ():
#     route_list = list()

#     for route_title in driver.find_elements_by_class_name('routes'):
#         route_list.append(route_title)

#     return route_list

# if __name__ == '__main__':
#     try:
#         driver = getdriver(url)
#         fillform(driver,'Padang Bai', 'Gili Trawangan', '29 October 2019')
#         route_list = scrape(driver)
#         with open('scrapetest.csv', 'a') as csv_filetest:
#             writer = csv.writer(csv_filetest)
#             writer.writerrow([route_list])
#     finally:
#         driver.quit()
    