import selenium
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
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

#pseudo code:
#1. build machine to connect with host
#2. Select departure route
#3. select date
#4. search
#5. print date & time 
#6. if words = oops.., continue

#find element by name = "destination_from"
#find element by name = "destination_to"

def fill_form(driver, search_argument):
    driver.find_element_by_class_name('one-way-option').click()
    print('success click one way')
    driver.find_element_by_name('destination_from')
    #value 11 =PB, 12 = SRG, 13=LMB, 8=GA, 10=GT,   9=TK. worth separate it using class
    print('sucess click destination from')
    select.select_by_value('12') #worth to be input
    print('success selecting destination value')
    driver.find_element_by_name('destination_to')
    print('success selecting destination to')
    #worth separate it into class
    select.select_by_value('10') #worth to be input
    print('success selecting destination value')
    #make a class perhaps so that its easily customisable
    driver.find_element_by_name('depart_date')
    print('success choosing depart date')
    search_field_depart_date = driver.find_element_by_name('depart_date').click()
    #wait until date is available
    wait = WebDriverWait(driver, timeout=3).until(
        EC.presence_of_elements_located((By.CLASS_NAME, 'ui-datepicker-calendar')))
    
    #select datepicker
    # calendar = driver.find_element_by_name('ui-datepicker-calendar')    
    #find some date picker and fill in, worth to have a for loop or dependency injection?, class='ui-datepicker-month, class='ui-datepicker-year', class='ui-datepicker-calendar' <td class=" " data-handler="selectDay" data-event="click" data-month="7" data-year="2019"><a class="ui-state-default" href="#">5</a></td>
    #select.input[name=depart_date, value= '20 November 2019']
    calendar = driver.find_element_by_name('ui-datepicker-calendar')
    search_field_adult = driver.find_element_by_id('select2-adult-4a-container')
    select.select_by_title('2')
    #look for search button and click it
    search_field_button = driver.find_element_by_class_name('search-avaibility').click()

fill_form()   
    
    