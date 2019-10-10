import selenium
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import csv

url = 'https://bluewater-express.com/'
def getdriver(url):
    options = Options()
    options.add_argument('-headless')
    driver = Firefox(executable_path='geckodriver', options=options)
    driver.get(url)
    wait = WebDriverWait(driver,5).until(EC.presence_of_element_located(By.ID,'one-way-option'))
    return driver

def fillform(driver, port_from, port_to, date):
    search_field = driver.find_element_by_name('destination_from')
    search_field.send_keys(port_from)
    search_field2 = driver.find_element_by_name('destination_to')
    search_field2.send_keys(port_to)
    search_date = driver.find_element_by_name('depart_date')
    search_date.send_keys(date)
    passenger = driver.find_element_by_class_name('adult prequired', value='2')
    driver.find_element_by_class_name('search-avaibility').click()
    wait = WebDriverWait(driver,timeout=10).until(EC.presence_of_element_located((by.CLASS_NAME, 'destination-name')))

def scrape ():
    route_list = list()

    for route_title in driver.find_elements_by_class_name('routes'):
        route_list.append(route_title)

    return route_list

if __name__ == '__main__':
    try:
        driver = getdriver(url)
        fillform(driver,'Padang Bai', 'Gili Trawangan', '29 October 2019')
        route_list = scrape(driver)
        with open('scrapetest.csv', 'a') as csv_filetest:
            writer = csv.writer(csv_filetest)
            writer.writerrow([route_list])
    finally:
        driver.quit()
    