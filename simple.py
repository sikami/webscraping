from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()
driver.get('https://bluewater-express.com/')
driver.find_element_by_css_selector('#return-option').click()
driver.find_element_by_name('destination_from').send_keys('11')
driver.find_element_by_name('destination_to').send_keys('10')
driver.find_element_by_name('depart_date').send_keys('02 November 2019')
driver.find_element_by_name('adult').send_keys('2')
driver.find_element_by_name('check_availability').submit()
WebDriverWait(driver, timeout=10).until(EC.presence_of_all_elements_located((By.CLASS_NAME,'flip-icon-result')))


