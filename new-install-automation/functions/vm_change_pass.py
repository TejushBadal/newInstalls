'''
Function Name: Voicemail password change
Function Purpose: Changes password for user voicemail
Author: Nikola Gavric
'''

def vm_change_pass(extension):
    s = Service("C:\\Users\\th73\\Documents\\chromedriver.exe")

    options = Options()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    #options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument("--incognito")
    options.add_argument("--start-maximized")


    driver = webdriver.Chrome(service = s, options = options)


    driver.get("https://voicemail.ca.sunlife/UCSSO/SignInUC.aspx?state=PVNTTyZjbGllbnRJZD1VQ1dDJnNjb3BlPVVDQUxMJnN0YXRlPVNTTyZyZWRpcmVjdF9Vcmk9aHR0cHMlMjUzYSUyNTJmJTI1MmZ2b2ljZW1haWwuY2Euc3VubGlmZSUyNTJmdWMlMjUyZndlYmNsaWVudCUyNTJmd2ViY2xpZW50LmFzcCZ0eXBlPUluSG91c2UmbG9nb3V0PSZvZmZsaW5lQWNjZXNzPSZjb21wbGV0aW9uPWh0dHBzJTI1M2ElMjUyZiUyNTJmdm9pY2VtYWlsLmNhLnN1bmxpZmUlMjUyZlVDU1NPJTI1MmYmcnN0YXRlPTQ2YjJhNzJkLTc1MzktNGM2NC1hNzI1LWJiNGZmNGNhOGFjZg==")

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "tMailbox"))).send_keys(extension)

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "tPassword"))).send_keys(f'{extension}a')

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/form/section/div/a"))).click()
    time.sleep(2)

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div/div/div[5]/div[2]"))).click()

    iframe = ui.WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "FrameMain")))

    driver.switch_to.frame(iframe)

    iframe = ui.WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "MainPage")))

    driver.switch_to.frame(iframe)


    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/form[1]/table/tbody/tr/td/div/table/tbody/tr/td/div[2]/table[1]/tbody/tr[8]/td[2]/input"))).clear()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/form[1]/table/tbody/tr/td/div/table/tbody/tr/td/div[2]/table[1]/tbody/tr[8]/td[2]/input"))).send_keys('1947501')
    time.sleep(1)
    
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/form[1]/table/tbody/tr/td/div/table/tbody/tr/td/div[2]/table[1]/tbody/tr[9]/td[2]/input"))).clear()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/form[1]/table/tbody/tr/td/div/table/tbody/tr/td/div[2]/table[1]/tbody/tr[9]/td[2]/input"))).send_keys('1947501')

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[2]/ul/li[1]/a"))).click()

    time.sleep(5)