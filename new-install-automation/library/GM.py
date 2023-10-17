from ansible.module_utils.basic import AnsibleModule
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


'''
Function Name: Voicemail password change
Function Purpose: Changes password for user voicemail
Author: Nikola Gavric
'''

with open('CREDENTIALS.json', "r", encoding="utf-8") as f:
    data = json.load(f)


def vm_pass(extension):

    options = Options()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    #options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument("--incognito")
    options.add_argument("--start-maximized")


    driver = webdriver.Chrome(options = options)


    driver.get(data["VM_PASS_URL"])

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "tMailbox"))).send_keys(extension)

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "tPassword"))).send_keys(f'{extension}a')

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/form/section/div/a"))).click()
    time.sleep(2)

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div/div/div[5]/div[2]"))).click()

    iframe = driver.WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "FrameMain")))

    driver.switch_to.frame(iframe)

    iframe = driver.WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "MainPage")))

    driver.switch_to.frame(iframe)


    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/form[1]/table/tbody/tr/td/div/table/tbody/tr/td/div[2]/table[1]/tbody/tr[8]/td[2]/input"))).clear()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/form[1]/table/tbody/tr/td/div/table/tbody/tr/td/div[2]/table[1]/tbody/tr[8]/td[2]/input"))).send_keys('1947501')
    time.sleep(1)
    
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/form[1]/table/tbody/tr/td/div/table/tbody/tr/td/div[2]/table[1]/tbody/tr[9]/td[2]/input"))).clear()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/form[1]/table/tbody/tr/td/div/table/tbody/tr/td/div[2]/table[1]/tbody/tr[9]/td[2]/input"))).send_keys('1947501')

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[2]/ul/li[1]/a"))).click()

    time.sleep(5)


def main():
    extension = ""
    
    try:
        result = vm_pass(extension)
    except Exception as e:

if __name__ == '__main__':
    main()