'''
Function Name: Avaya System Manager install
Function Purpose: Create new user in Avaya System Manager
Author: Nikola Gavric
'''

def sm(name, surname, email, extension, location):
    comm_pass = '284592'

    s = Service("C:\\Users\\th73\\Documents\\chromedriver.exe")

    options = Options()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    #options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument("--incognito")
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(service = s, options = options)


    driver.get("https://10.65.6.41/network-login/")

    #Login
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "j_username"))).send_keys('') #ASF2 ID
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "j_password"))).send_keys('Spring21') #Password
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[3]/table/tbody/tr/td[2]/div/form/div[2]/input[3]"))).click()

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/main/div/div/div/div/div/div[2]/div/div/span/div/div/div[6]/div[2]/div/div/div[1]/span/a[2]"))).click()
    #WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/main/div/div/div/div/div/div[2]/div/div/span/div/div/div[6]/div[2]/div/div/div[1]"))).click()


    iframe = ui.WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.TAG_NAME, "iframe")))

    driver.switch_to.frame(iframe)

    button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div[1]/div/div/div[2]/div/a[3]/button")))
    time.sleep(2)
    button.click()

    #**Basic Info**
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "surname"))).send_keys(surname)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "givenName"))).send_keys(name)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "loginName"))).send_keys(email)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "displayNameAscii"))).send_keys(f'{name} {surname}')
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "displayName"))).send_keys(f'{name} {surname}')
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "userPassword"))).send_keys('Sunlife123')
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "confirm"))).send_keys('Sunlife123')
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div/div[2]/div/form/div[3]/div[15]/div/div[2]/div/div/div/div"))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div/ul/li[25]"))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div/div[2]/div/form/div[3]/div[16]/div/div[2]/div/div/div/div"))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div/div/ul/li[12]"))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[1]/div/button[3]"))).click()
    time.sleep(2)

    #Communication Profile Password
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div[1]/div/ul/li/div/a"))).click()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "commPassword"))).send_keys(comm_pass)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "confirm"))).send_keys(comm_pass)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div[2]/div/div[1]/div[3]/button[2]"))).click()


    #comm address 1
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//html/body/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/button[2]"))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div/div[2]/div/div[1]/div[2]/form/div[1]/div/div/div[2]/div/div/div/div"))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div/div/div/ul/li[1]"))).click()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "handle"))).send_keys(extension)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div/div[2]/div/div[1]/div[2]/form/div[2]/div[1]/div[2]/div/div/div[3]/div/div/div/div/div/div"))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "html/body/div[7]/div/div/div/ul/li[15]"))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div/div[2]/div/div[1]/div[3]/button[2]"))).click()
    time.sleep(2)

    #comm address 2
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//html/body/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/button[2]"))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div/div[2]/div/div[1]/div[2]/form/div[1]/div/div/div[2]/div/div/div/div"))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div/div/div/ul/li[1]"))).click()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "handle"))).send_keys(f'+1001{extension}')
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div/div[2]/div/div[1]/div[2]/form/div[2]/div[1]/div[2]/div/div/div[3]/div/div/div/div/div/div"))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "html/body/div[7]/div/div/div/ul/li[15]"))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div/div[2]/div/div[1]/div[3]/button[2]"))).click()
    time.sleep(2)

    #comm address 3
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//html/body/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/button[2]"))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div/div[2]/div/div[1]/div[2]/form/div[1]/div/div/div[2]/div/div/div/div"))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div/div/div/ul/li[2]"))).click()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "handle"))).send_keys(f'+{extension}')
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div/div[2]/div/div[1]/div[2]/form/div[2]/div[1]/div[2]/div/div/div[3]/div/div/div/div/div/div"))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "html/body/div[7]/div/div/div/ul/li[15]"))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div/div[2]/div/div[1]/div[3]/button[2]"))).click()
    time.sleep(2)

    #**session Manager profile**
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div[1]/div/ul/li/ul/li/ul/li[2]/ul/li[1]/span/span"))).click()
    #primary session manager
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "primarySM_input"))).send_keys('Waterloo SM')
    #secondary session manager
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "secondarySM_input"))).send_keys(f'Toronto SM')
    #Max. Simultaneous Devices
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div/form/div/div[9]/div/div/div[2]/div/div/div/div/div"))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/div/div/div/ul/li[3]"))).click()
    #Origination Sequence
    dropdown = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div/form/div/div[15]/div/div/div[2]/div/div/div")))
    dropdown.click()
    time.sleep(2)
    dropdown.send_keys(Keys.DOWN, Keys.DOWN, Keys.RETURN)
    #Termination Sequence
    dropdown = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div/form/div/div[17]/div/div/div[2]/div/div/div")))
    dropdown.click()
    time.sleep(2)
    dropdown.send_keys(Keys.DOWN, Keys.DOWN, Keys.RETURN)
    #Home Location
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "homeLocation_input"))).send_keys(location)


    #**CM endpoint profile**
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div[1]/div/ul/li/ul/li/ul/li[2]/ul/li[2]/span/span"))).click()

    #System
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div/form/div/div[1]/div/div/div[2]/div/div/div/div/div"))).click()
    time.sleep(2)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div/div/div/ul/li[3]"))).click()
    #Template
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div/form/div/div[9]/div/div/div[2]/div/div[1]/div/div/ul/li/div/span[1]/input"))).click()
    time.sleep(2)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div/div/div/ul/li[2]"))).click()
    #Security Code
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "securityCode"))).send_keys(extension)
    #Extension
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "extension_input"))).send_keys(extension)
    #Preferred Handle
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div/form/div/div[19]/div/div/div[2]/div/div/div/div/div"))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/div/div/div/ul/li[2]"))).click()
    #Edit pencil
    time.sleep(3)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div/form/div/div[7]/div/div/div[2]/div/div/div/div/ul/li/div/span[1]/span/span/span[2]/i"))).click()
    time.sleep(3)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[8]/div/div[2]/div/div[1]/button/span"))).click()
    time.sleep(2)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div/form/div/div[7]/div/div/div[2]/div/div/div/div/ul/li/div/span[1]/span/span/span[2]/i"))).click()

    #Manually enter tn and click save and commit

    time.sleep(45)