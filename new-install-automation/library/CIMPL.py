import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

'''
Function Name: Cimpl install
Function Purpose: Updates cimpl inventory
Author: Nikola Gavric
'''

with open('CREDENTIALS.json', "r", encoding="utf-8") as f:
    data = json.load(f)

def cimpl(first_name, last_name, email, extension, acf2, budget, ritm, date):
    options = Options()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options = options)


    driver.get(data["CIMPL_URL"])

    #login
    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/form/div[2]/input"))).send_keys(data["CIMPL_EMAIL"]) #Email
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/form/div[5]/button'))).click() # Continue
        time.sleep(3)
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/form/div[4]/input"))).send_keys(data["CIMPL_PASSWORD"]) #Password
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/form/div[5]/button"))).click() # Sign In

        time.sleep(2)
        WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'loader__container___G8vlD')))

        driver.get(data["CIMPL_URL"])
        print('logged in')
    except:
        driver.close()
        return('failed to login')


    #go to inventory
    driver.get("https://apps.cimpl.com/Cimpl/Actions#/home/inventory")

    time.sleep(2)
    WebDriverWait(driver, 20).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'loader__container___G8vlD')))
    print('done')

    #search for extension
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/cimpl-landing/div/div[2]/div[2]/ng-transclude/div/inventory-page/div[1]/div[3]/div/div/div[2]/div/cimpl-collapsible-box/div/div[2]/ng-transclude/div[2]/div[1]/basic-search-input/div/div/div[1]/input"))).clear()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/cimpl-landing/div/div[2]/div[2]/ng-transclude/div/inventory-page/div[1]/div[3]/div/div/div[2]/div/cimpl-collapsible-box/div/div[2]/ng-transclude/div[2]/div[1]/basic-search-input/div/div/div[1]/input"))).send_keys(extension)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/cimpl-landing/div/div[2]/div[2]/ng-transclude/div/inventory-page/div[1]/div[3]/div/div/div[2]/div/cimpl-collapsible-box/div/div[2]/ng-transclude/div[2]/div[1]/basic-search-input/div/div/div[1]/input"))).send_keys(Keys.RETURN)

    
    WebDriverWait(driver, 20).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'loader__container___G8vlD')))
    print('done')

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/cimpl-landing/div/div[2]/div[2]/ng-transclude/div/inventory-page/div[1]/div[3]/div/div/div[5]/inventory-list/div/cimpl-grid/div/div[2]/div[2]/table/tbody/tr/td[6]/span"))).click()

    WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'loader__container___G8vlD')))
    print('done')

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/cimpl-landing/div/div[2]/div[2]/ng-transclude/div/inventory-details-page/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[2]/cimpl-button/button/div/span"))).click()

    WebDriverWait(driver, 20).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'loader__container___G8vlD')))
    print('done')

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/cimpl-landing/div/div[2]/div[2]/ng-transclude/div/inventory-details-page/div[1]/div[2]/div[1]/inventory-side-list/div/div[2]/menu-side-option/div/div[3]/div[1]/ng-transclude/div[2]/div[2]/cimpl-button/button/div/span"))).click()

    WebDriverWait(driver, 20).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'loader__container___G8vlD')))
    print('done')

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/cimpl-landing/div/div[2]/div[2]/ng-transclude/div/inventory-details-page/div[1]/div[2]/div[1]/inventory-side-list/div/div[3]/menu-side-option/div/div[3]/div[1]/ng-transclude/div[1]"))).click()

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/cimpl-landing/div/div[2]/div[2]/ng-transclude/div/inventory-details-page/div[1]/div[2]/div[2]/div[3]/div/inventory-details-hardware/div[1]/div/div/cimpl-button/button/div/span"))).click()

    WebDriverWait(driver, 20).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'loader__container___G8vlD')))
    print('done')

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/cimpl-landing/div/div[2]/div[2]/ng-transclude/div/inventory-details-page/div[1]/div[2]/div[2]/div[3]/div/inventory-details-hardware/div/div[2]/inventory-details-hardware-add/div[1]/cimpl-form/div/div[1]/div/ng-transclude/div[1]/div[2]/ng-transclude/cimpl-dropdown/div/div[1]/span"))).click()
    time.sleep(2)

    element = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/cimpl-landing/div/div[2]/div[2]/ng-transclude/div/inventory-details-page/div[1]/div[2]/div[2]/div[3]/div/inventory-details-hardware/div/div[2]/inventory-details-hardware-add/div[1]/cimpl-form/div/div[1]/div/ng-transclude/div[1]/div[2]/ng-transclude/cimpl-dropdown/div/div[1]/span")
    element.send_keys(Keys.DOWN)
    time.sleep(1)
    element.send_keys(Keys.DOWN)
    time.sleep(1)
    element.send_keys(Keys.RETURN)

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/cimpl-landing/div/div[2]/div[2]/ng-transclude/div/inventory-details-page/div[1]/div[2]/div[2]/div[3]/div/inventory-details-hardware/div/div[2]/inventory-details-hardware-add/div[1]/cimpl-form/div/div[1]/div/ng-transclude/div[2]/div[2]/ng-transclude/div[2]/label/span[1]/i"))).click()

    WebDriverWait(driver, 20).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'loader__container___G8vlD')))
    print('done')

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/cimpl-landing/div/div[2]/div[2]/ng-transclude/div/inventory-details-page/div[1]/div[2]/div[2]/div[3]/div/inventory-details-hardware/div/div[2]/inventory-details-hardware-add/div[1]/div[2]/inventory-details-hardware-warehouse-list/div/div[2]/cimpl-collapsible-box/div/div[2]/ng-transclude/filter-search/div/div[2]/div[1]/div[2]/div/div[2]/div[2]/div/cimpl-checkbox[2]/div/div[1]/label/span[1]/i"))).click()

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/cimpl-landing/div/div[2]/div[2]/ng-transclude/div/inventory-details-page/div[1]/div[2]/div[2]/div[3]/div/inventory-details-hardware/div/div[2]/inventory-details-hardware-add/div[1]/div[2]/inventory-details-hardware-warehouse-list/div/div[2]/cimpl-collapsible-box/div/div[2]/ng-transclude/filter-search/div/div[2]/div[1]/div[2]/div/div[2]/div[2]/div/cimpl-checkbox[7]/div/div[1]/label/span[1]/i"))).click()

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/cimpl-landing/div/div[2]/div[2]/ng-transclude/div/inventory-details-page/div[1]/div[2]/div[2]/div[3]/div/inventory-details-hardware/div/div[2]/inventory-details-hardware-add/div[1]/div[2]/inventory-details-hardware-warehouse-list/div/div[2]/cimpl-collapsible-box/div/div[2]/ng-transclude/filter-search/div/div[2]/div[2]/div/selected-filter-container/div/div[2]/div[1]/div[1]/div[2]/div[2]/cimpl-meta-field/div/div[2]/div/div[1]/div/div/input"))).send_keys('9630')
    time.sleep(2)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/cimpl-landing/div/div[2]/div[2]/ng-transclude/div/inventory-details-page/div[1]/div[2]/div[2]/div[3]/div/inventory-details-hardware/div/div[2]/inventory-details-hardware-add/div[1]/div[2]/inventory-details-hardware-warehouse-list/div/div[2]/cimpl-collapsible-box/div/div[2]/ng-transclude/filter-search/div/div[2]/div[2]/div/selected-filter-container/div/div[2]/div[1]/div[1]/div[2]/div[2]/cimpl-meta-field/div/div[2]/div/div[1]/div/div/input"))).send_keys(Keys.RETURN)

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/cimpl-landing/div/div[2]/div[2]/ng-transclude/div/inventory-details-page/div[1]/div[2]/div[2]/div[3]/div/inventory-details-hardware/div/div[2]/inventory-details-hardware-add/div[1]/div[2]/inventory-details-hardware-warehouse-list/div/div[2]/cimpl-collapsible-box/div/div[2]/ng-transclude/filter-search/div/div[2]/div[2]/div/selected-filter-container/div/div[2]/div[2]/div[1]/div[2]/div[2]/cimpl-meta-field/div/div[2]/div/div[1]/div/div/input"))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[26]/div/div[2]/ul/li[10]"))).click()

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/cimpl-landing/div/div[2]/div[2]/ng-transclude/div/inventory-details-page/div[1]/div[2]/div[2]/div[3]/div/inventory-details-hardware/div/div[2]/inventory-details-hardware-add/div[1]/div[2]/inventory-details-hardware-warehouse-list/div/div[2]/cimpl-collapsible-box/div/div[2]/ng-transclude/filter-search/div/div[3]/div[2]/cimpl-button/button/div/span"))).click()

    WebDriverWait(driver, 20).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'loader__container___G8vlD')))
    print('done')

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/cimpl-landing/div/div[2]/div[2]/ng-transclude/div/inventory-details-page/div[1]/div[2]/div[2]/div[3]/div/inventory-details-hardware/div/div[2]/inventory-details-hardware-add/div[1]/div[2]/inventory-details-hardware-warehouse-list/div/dynamic-column-grid/div/div[1]/div/div[1]/cimpl-grid/div/div[2]/div[2]/table/tbody/tr[1]"))).click()

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/cimpl-landing/div/div[2]/div[2]/ng-transclude/div/inventory-details-page/div[1]/div[2]/div[2]/div[3]/div/inventory-details-hardware/div/div[2]/inventory-details-hardware-add/div[2]/div/div[2]/cimpl-button/button/div/span"))).click()

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/cimpl-landing/div/div[2]/div[2]/ng-transclude/div/inventory-details-page/div[1]/div[2]/div[2]/div[3]/div/inventory-details-hardware/div[1]/div/div/cimpl-button/button/div/span"))).click()

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/cimpl-landing/div/div[2]/div[2]/ng-transclude/div/inventory-details-page/div[1]/div[2]/div[2]/div[3]/div/inventory-details-hardware/div/div[2]/inventory-details-hardware-add/div[1]/cimpl-form/div/div[1]/div/ng-transclude/div[1]/div[2]/ng-transclude/cimpl-dropdown/div/div[1]/span"))).click()
    time.sleep(2)

    element = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/cimpl-landing/div/div[2]/div[2]/ng-transclude/div/inventory-details-page/div[1]/div[2]/div[2]/div[3]/div/inventory-details-hardware/div/div[2]/inventory-details-hardware-add/div[1]/cimpl-form/div/div[1]/div/ng-transclude/div[1]/div[2]/ng-transclude/cimpl-dropdown/div/div[1]/span")
    element.send_keys(Keys.DOWN)
    time.sleep(1)
    element.send_keys(Keys.DOWN)
    time.sleep(1)
    element.send_keys(Keys.DOWN)
    time.sleep(1)
    element.send_keys(Keys.DOWN)
    time.sleep(1)
    element.send_keys(Keys.RETURN)

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/cimpl-landing/div/div[2]/div[2]/ng-transclude/div/inventory-details-page/div[1]/div[2]/div[2]/div[3]/div/inventory-details-hardware/div/div[2]/inventory-details-hardware-add/div[1]/cimpl-form/div/div[1]/div/ng-transclude/div[2]/div[2]/ng-transclude/div[1]/label/span[1]/i"))).click()

    WebDriverWait(driver, 20).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'loader__container___G8vlD')))
    print('done')

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/cimpl-landing/div/div[2]/div[2]/ng-transclude/div/inventory-details-page/div[1]/div[2]/div[2]/div[3]/div/inventory-details-hardware/div/div[2]/inventory-details-hardware-add/div[1]/div[2]/inventory-details-hardware-catalog-list/div/div[2]/cimpl-grid/div/div[2]/div[2]/table/tbody/tr[1]"))).click()

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/cimpl-landing/div/div[2]/div[2]/ng-transclude/div/inventory-details-page/div[1]/div[2]/div[2]/div[3]/div/inventory-details-hardware/div/div[2]/inventory-details-hardware-add/div[2]/div/div[2]/cimpl-button/button/div/span"))).click()

    WebDriverWait(driver, 20).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'loader__container___G8vlD')))
    print('done')


    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/cimpl-landing/div/div[2]/div[2]/ng-transclude/div/inventory-details-page/div[1]/div[2]/div[2]/div[3]/div/inventory-details-hardware/div[1]/div/div/cimpl-button/button/div/span"))).click()

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/cimpl-landing/div/div[2]/div[2]/ng-transclude/div/inventory-details-page/div[1]/div[2]/div[2]/div[3]/div/inventory-details-hardware/div/div[2]/inventory-details-hardware-add/div[1]/cimpl-form/div/div[1]/div/ng-transclude/div[1]/div[2]/ng-transclude/cimpl-dropdown/div/div[1]/span"))).click()
    time.sleep(2)

    element = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/cimpl-landing/div/div[2]/div[2]/ng-transclude/div/inventory-details-page/div[1]/div[2]/div[2]/div[3]/div/inventory-details-hardware/div/div[2]/inventory-details-hardware-add/div[1]/cimpl-form/div/div[1]/div/ng-transclude/div[1]/div[2]/ng-transclude/cimpl-dropdown/div/div[1]/span")
    element.send_keys(Keys.DOWN)
    time.sleep(1)
    element.send_keys(Keys.DOWN)
    time.sleep(1)
    element.send_keys(Keys.DOWN)
    time.sleep(1)
    element.send_keys(Keys.DOWN)
    time.sleep(1)
    element.send_keys(Keys.RETURN)

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/cimpl-landing/div/div[2]/div[2]/ng-transclude/div/inventory-details-page/div[1]/div[2]/div[2]/div[3]/div/inventory-details-hardware/div/div[2]/inventory-details-hardware-add/div[1]/cimpl-form/div/div[1]/div/ng-transclude/div[2]/div[2]/ng-transclude/div[1]/label/span[1]/i"))).click()

    WebDriverWait(driver, 20).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'loader__container___G8vlD')))
    print('done')

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/cimpl-landing/div/div[2]/div[2]/ng-transclude/div/inventory-details-page/div[1]/div[2]/div[2]/div[3]/div/inventory-details-hardware/div/div[2]/inventory-details-hardware-add/div[1]/div[2]/inventory-details-hardware-catalog-list/div/div[2]/cimpl-grid/div/div[2]/div[2]/table/tbody/tr[17]"))).click()

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/cimpl-landing/div/div[2]/div[2]/ng-transclude/div/inventory-details-page/div[1]/div[2]/div[2]/div[3]/div/inventory-details-hardware/div/div[2]/inventory-details-hardware-add/div[2]/div/div[2]/cimpl-button/button/div/span"))).click()

    WebDriverWait(driver, 20).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'loader__container___G8vlD')))
    print('done')

    #Contract
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/cimpl-landing/div/div[2]/div[2]/ng-transclude/div/inventory-details-page/div[1]/div[2]/div[1]/inventory-side-list/div/div[6]/menu-side-option/div/div[3]/div[1]/ng-transclude"))).click()

    WebDriverWait(driver, 20).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'loader__container___G8vlD')))
    print('done')

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/cimpl-landing/div/div[2]/div[2]/ng-transclude/div/inventory-details-page/div[1]/div[2]/div[2]/div[3]/div/inventory-details-contract/div[1]/div/cimpl-form/div/div[1]/div/ng-transclude/div[7]/div[2]/cimpl-datepicker/div/div[1]/span/span/input"))).send_keys(date, Keys.RETURN)

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/cimpl-landing/div/div[2]/div[2]/ng-transclude/div/inventory-details-page/div[1]/div[2]/div[2]/div[3]/div/inventory-details-contract/div[1]/div/cimpl-form/div/div[2]/div/span[2]/cimpl-button/button/div/span"))).click()

    WebDriverWait(driver, 20).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'loader__container___G8vlD')))
    print('done')

    #Assignment
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/cimpl-landing/div/div[2]/div[2]/ng-transclude/div/inventory-details-page/div[1]/div[2]/div[1]/inventory-side-list/div/div[9]/menu-side-option/div/div[3]/div[1]/ng-transclude"))).click()

    WebDriverWait(driver, 20).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'loader__container___G8vlD')))
    print('done')

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/cimpl-landing/div/div[2]/div[2]/ng-transclude/div/inventory-details-page/div[1]/div[2]/div[2]/div[3]/div/inventory-details-assignment/div/div[1]/div[2]/label/span[1]/i"))).click()

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/cimpl-landing/div/div[2]/div[2]/ng-transclude/div/inventory-details-page/div[1]/div[2]/div[2]/div[3]/div/inventory-details-assignment/div/div[2]/employee-modal-popup-selector/div/div/div[1]/div/div/cimpl-icon-button/div/div[1]/i"))).click()

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/cimpl-landing/div/div[2]/div[2]/ng-transclude/div/inventory-details-page/div[1]/div[2]/div[2]/div[3]/div/inventory-details-assignment/div/div[2]/employee-modal-popup-selector/div/div/cimpl-modal-popup/div/div/div/div/div[2]/ng-transclude/ng-transclude/employee-list/div/div[1]/cimpl-collapsible-box/div/div[2]/ng-transclude/div[2]/div[2]/div/input"))).send_keys(acf2)

    WebDriverWait(driver, 20).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'loader__container___G8vlD')))
    print('done')

    if driver.find_elements(By.XPATH, '/html/body/div[3]/div/div/cimpl-landing/div/div[2]/div[2]/ng-transclude/div/inventory-details-page/div[1]/div[2]/div[2]/div[3]/div/inventory-details-assignment/div/div[2]/employee-modal-popup-selector/div/div/cimpl-modal-popup/div/div/div/div/div[2]/ng-transclude/ng-transclude/employee-list/div/div[3]/cimpl-grid/div/div[2]/div[2]/table/tbody/tr'):
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/cimpl-landing/div/div[2]/div[2]/ng-transclude/div/inventory-details-page/div[1]/div[2]/div[2]/div[3]/div/inventory-details-assignment/div/div[2]/employee-modal-popup-selector/div/div/cimpl-modal-popup/div/div/div/div/div[2]/ng-transclude/ng-transclude/employee-list/div/div[3]/cimpl-grid/div/div[2]/div[2]/table/tbody/tr"))).click()
        time.sleep(2)
    else:
        print('ACF2 ID not found')
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/cimpl-landing/div/div[2]/div[2]/ng-transclude/div/inventory-details-page/div[1]/div[2]/div[2]/div[3]/div/inventory-details-assignment/div/div[2]/employee-modal-popup-selector/div/div/cimpl-modal-popup/div/div/div/div/div[1]/div[1]/span"))).click()

        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/cimpl-landing/div/div[2]/div[2]/ng-transclude/div/inventory-details-page/div[1]/div[2]/div[2]/div[3]/div/inventory-details-assignment/div/div[1]/div[3]/label/span[1]/i"))).click()

        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/cimpl-landing/div/div[2]/div[2]/ng-transclude/div/inventory-details-page/div[1]/div[2]/div[2]/div[3]/div/inventory-details-assignment/div/div[5]/cimpl-form/div/div[1]/div/ng-transclude/div[1]/div[2]/ng-transclude/department-modal-popup-selector/div/div/div[2]/div[2]/div[1]/cimpl-icon-button/div/div[1]/i"))).click()

        WebDriverWait(driver, 20).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'loader__container___G8vlD')))
        print('done')

        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/cimpl-landing/div/div[2]/div[2]/ng-transclude/div/inventory-details-page/div[1]/div[2]/div[2]/div[3]/div/inventory-details-assignment/div/div[5]/cimpl-form/div/div[1]/div/ng-transclude/div[1]/div[2]/ng-transclude/department-modal-popup-selector/div/div/cimpl-modal-popup/div/div/div/div/div[2]/ng-transclude/ng-transclude/department-list/div/cimpl-collapsible-box/div/div[2]/ng-transclude/div[2]/div[2]/div/input"))).send_keys(budget)

        WebDriverWait(driver, 20).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'loader__container___G8vlD')))
        print('done')

        time.sleep(2)

        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/cimpl-landing/div/div[2]/div[2]/ng-transclude/div/inventory-details-page/div[1]/div[2]/div[2]/div[3]/div/inventory-details-assignment/div/div[5]/cimpl-form/div/div[1]/div/ng-transclude/div[1]/div[2]/ng-transclude/department-modal-popup-selector/div/div/cimpl-modal-popup/div/div/div/div/div[2]/ng-transclude/ng-transclude/department-list/div/div[2]/div/cimpl-grid/div/div[2]/div[2]/table/tbody/tr"))).click()

        WebDriverWait(driver, 20).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'loader__container___G8vlD')))
        print('done')

        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/cimpl-landing/div/div[2]/div[2]/ng-transclude/div/inventory-details-page/div[1]/div[2]/div[1]/inventory-side-list/div/div[14]/menu-side-option/div/div[3]/div[1]/ng-transclude/div[1]"))).click()

        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/cimpl-landing/div/div[2]/div[2]/ng-transclude/div/inventory-details-page/div[1]/div[2]/div[2]/div[3]/div/inventory-details-additional-info/div/cimpl-form/div/div[1]/div/ng-transclude/div/span/div[2]/div[5]/div/div[2]/ng-transclude/div/div/div/div[2]/div/input"))).send_keys(f'{first_name} {last_name}')

        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/cimpl-landing/div/div[2]/div[2]/ng-transclude/div/inventory-details-page/div[1]/div[2]/div[2]/div[3]/div/inventory-details-additional-info/div/div/div[2]/cimpl-button/button/div/span"))).click()

    #Comments
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/cimpl-landing/div/div[2]/div[2]/ng-transclude/div/inventory-details-page/div[1]/div[2]/div[1]/inventory-side-list/div/div[15]/menu-side-option/div/div[3]/div[1]/ng-transclude/div[1]"))).click()

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/cimpl-landing/div/div[2]/div[2]/ng-transclude/div/inventory-details-page/div[1]/div[2]/div[2]/div[3]/div/inventory-details-comments/div/cimpl-textarea/div/textarea"))).send_keys(f'\n{date} - {ritm} - new user - {first_name} {last_name} {acf2}')

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/cimpl-landing/div/div[2]/div[2]/ng-transclude/div/inventory-details-page/div[1]/div[2]/div[2]/div[3]/div/inventory-details-comments/div/div[2]/cimpl-button/button/div/span"))).click()

    #Excecute
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/cimpl-landing/div/div[2]/div[2]/ng-transclude/div/inventory-details-page/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[4]/cimpl-button/button/div/span"))).click()

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/cimpl-landing/div/div[2]/div[2]/ng-transclude/div/inventory-details-page/div[2]/div[2]/div/div[2]/ng-transclude/div/workorder-wizard/div/div[3]/div[1]/div/label/span[1]/i"))).click()

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/cimpl-landing/div/div[2]/div[2]/ng-transclude/div/inventory-details-page/div[2]/div[2]/div/div[4]/div[2]/div[2]/cimpl-button/button/div/span"))).click()


    time.sleep(2)


def main():
            
    first_name = 'Tina'
    last_name = 'Bali-Rampal'
    email = 'tina.bali-rampal@sunlife.com'
    extension = '3419588'
    acf2 = 'TY12'
    budget = '182724'
    ritm = 'RITM1510179'
    date = '2023-10-11'

    try:
        cimpl(first_name, last_name, email, extension, acf2, budget, ritm, date)
        
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()