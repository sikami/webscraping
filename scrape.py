import selenium
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_condition as EC
from selenium.webdriver.support.wait import WebDriverWait

url = 'https://bluewater-express.com/'
def prepareDriver(url):
    #return a firefox  webdriver, due to geckodriver specified only for firefox
    options = Options()
    option.add_argument('-headless')
    driver= Chrome(executable_path='geckodriver', options=options)
    driver.get(url)
    wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.ID, 'ss')))
    return driver

    