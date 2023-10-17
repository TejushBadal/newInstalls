#from ansible.module_utils.basic import AnsibleModule
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

'''
Function Name: Voicemail install
Function Purpose: Creates user voicemail
Author: Nikola Gavric
'''

#TODO
#Need to fix where personal operator is commented

with open('CREDENTIALS.json', "r", encoding="utf-8") as f:
    data = json.load(f)

def vm(first_name, last_name, email, extension, acf2):

    options = Options()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--start-maximized")
    options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(options = options)


    driver.get(data['VM_URL'])

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username"))).send_keys(data['VM_USERNAME']) #username
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password"))).send_keys(data['VM_PASSWORD']) #password

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/form/button[1]"))).click()


    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/div/div/div[2]/div/div[2]/table/tbody/tr[1]/td[1]/a"))).click()
    time.sleep(3)

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/div/div/div[2]/div/div[2]/form/div/div[2]/ul/li[3]/a"))).click()
    time.sleep(2)

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/div/div/div[2]/div/div[2]/form/div/div[2]/div/div[3]/div/div/div[2]/div/div[1]/div[1]/div/div/a/button"))).click()

    #**General Options**

    #Mailbox Number
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div/div/div/div[2]/div/div[2]/form/div/div[2]/div/div[3]/div/div/div[2]/fieldset/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div[1]/div[2]/form/div/div/input[1]"))).send_keys(extension)

    #First Name
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div/div/div/div[2]/div/div[2]/form/div/div[2]/div/div[3]/div/div/div[2]/fieldset/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div[1]/div[2]/form/div/div/input[2]"))).send_keys(first_name)

    #Last Name
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div/div/div/div[2]/div/div[2]/form/div/div[2]/div/div[3]/div/div/div[2]/fieldset/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div[1]/div[2]/form/div/div/input[3]"))).send_keys(last_name)

    #Department
    dropdown = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/div/div/div[2]/div/div[2]/form/div/div[2]/div/div[3]/div/div/div[2]/fieldset/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div[1]/div[2]/form/div/div/select[2]")))

    dropdown.click()
    time.sleep(1)
    dropdown.send_keys(Keys.DOWN, Keys.DOWN, Keys.DOWN, Keys.DOWN, Keys.DOWN, Keys.DOWN, Keys.DOWN, Keys.DOWN, Keys.RETURN)

    #Department
    dropdown = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/div/div/div[2]/div/div[2]/form/div/div[2]/div/div[3]/div/div/div[2]/fieldset/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div[1]/div[2]/form/div/div/select[3]")))

    dropdown.click()
    time.sleep(1)
    dropdown.send_keys(Keys.DOWN, Keys.RETURN)

    #Voicemail Password
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div/div/div/div[2]/div/div[2]/form/div/div[2]/div/div[3]/div/div/div[2]/fieldset/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div[1]/div[2]/form/div/div/input[5]"))).send_keys('194750')

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div/div/div/div[2]/div/div[2]/form/div/div[2]/div/div[3]/div/div/div[2]/fieldset/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div[1]/div[2]/form/div/div/input[6]"))).send_keys('194750')

    #Application User Settings
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div/div/div/div[2]/div/div[2]/form/div/div[2]/div/div[3]/div/div/div[2]/fieldset/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div[1]/div[2]/form/div/div/input[7]"))).send_keys(extension)

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div/div/div/div[2]/div/div[2]/form/div/div[2]/div/div[3]/div/div/div[2]/fieldset/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div[1]/div[2]/form/div/div/input[8]"))).send_keys(f'{extension}a')

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div/div/div/div[2]/div/div[2]/form/div/div[2]/div/div[3]/div/div/div[2]/fieldset/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div[1]/div[2]/form/div/div/input[9]"))).send_keys(f'{extension}a')

    time.sleep(5)
    #Click Save
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/div/div/div[2]/div/div[2]/form/div/div[2]/div/div[3]/div/div/div[2]/fieldset/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div[2]/button[1]"))).click()
    time.sleep(5)

    #**Advanced**
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/div/div/div[2]/div/div[2]/form/div/div[2]/div/div[3]/div/div/div[2]/fieldset/div/div/div/div[2]/div/div[1]/div/div[1]/ul/li[2]/a"))).click()

    #Personal Operator
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div/div/div/div[2]/div/div[2]/form/div/div[2]/div/div[3]/div/div/div[2]/fieldset/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div[1]/div[2]/div/div/input[1]"))).send_keys(extension, Keys.RETURN)
    time.sleep(10)
    text = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/div/div/div[2]/div/div[2]/form/div/div[2]/div/div[3]/div/div/div[2]/fieldset/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div[1]/div[2]/div/div/ul/li"))).text
    
    if text == f'{extension} {first_name} {last_name}':
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/div/div/div[2]/div/div[2]/form/div/div[2]/div/div[3]/div/div/div[2]/fieldset/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div[1]/div[2]/div/div/ul/li"))).click()
    else:
        time.sleep(10)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/div/div/div[2]/div/div[2]/form/div/div[2]/div/div[3]/div/div/div[2]/fieldset/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div[1]/div[2]/div/div/ul/li"))).click()

    #Account Name
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div/div/div/div[2]/div/div[2]/form/div/div[2]/div/div[3]/div/div/div[2]/fieldset/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div[1]/div[2]/div/div/input[3]"))).send_keys(f'ml\{acf2}')

    #Desktop Capability
    elem = driver.find_element(By.TAG_NAME, "html")
    elem.send_keys(Keys.END)
    time.sleep(2)

    dropdown = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/div/div/div[2]/div/div[2]/form/div/div[2]/div/div[3]/div/div/div[2]/fieldset/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div[1]/div[2]/div/div/div[5]/select")))

    dropdown.click()
    dropdown.send_keys(Keys.UP, Keys.UP, Keys.UP, Keys.UP, Keys.RETURN)

    #Click Save
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/div/div/div[2]/div/div[2]/form/div/div[2]/div/div[3]/div/div/div[2]/fieldset/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div[2]/button[1]"))).click()
    time.sleep(3)

    #**Mailbox Options**
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/div/div/div[2]/div/div[2]/form/div/div[2]/div/div[3]/div/div/div[2]/fieldset/div/div/div/div[2]/div/div[1]/div/div[1]/ul/li[3]/a"))).click()

    #Fax Detection
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/div/div/div[2]/div/div[2]/form/div/div[2]/div/div[3]/div/div/div[2]/fieldset/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div[1]/div[2]/div/div/div[5]/input"))).click()

    #Message Playback Order
    dropdown = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/div/div/div[2]/div/div[2]/form/div/div[2]/div/div[3]/div/div/div[2]/fieldset/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div[1]/div[2]/div/div/select[3]")))

    dropdown.click()
    dropdown.send_keys(Keys.UP, Keys.RETURN)

    #Click Save
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/div/div/div[2]/div/div[2]/form/div/div[2]/div/div[3]/div/div/div[2]/fieldset/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div[2]/button[1]"))).click()
    time.sleep(3)

    #**Addresses**
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/div/div/div[2]/div/div[2]/form/div/div[2]/div/div[3]/div/div/div[2]/fieldset/div/div/div/div[2]/div/div[1]/div/div[1]/ul/li[11]/a"))).click()

    #Edit reply to
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/div/div/div[2]/div/div[2]/form/div/div[2]/div/div[3]/div/div/div[2]/fieldset/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/table/tbody/tr[3]/td[4]/a[1]"))).click()

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/user-address/div[2]/div/div/div[5]/div/input"))).clear()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/user-address/div[2]/div/div/div[5]/div/input"))).send_keys(email)

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/user-address/div[3]/button[1]"))).click()

    #New Address
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/div/div/div[2]/div/div[2]/form/div/div[2]/div/div[3]/div/div/div[2]/fieldset/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div[1]/div/button"))).click()

    dropdown = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/user-address/div[2]/div/div/div[2]/div/select")))
    dropdown.click()
    dropdown.send_keys(Keys.DOWN, Keys.DOWN, Keys.DOWN, Keys.DOWN, Keys.RETURN)

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/user-address/div[2]/div/div/div[5]/div/input"))).send_keys(email)

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/user-address/div[2]/div/div/div[7]/div[2]/div[1]/input"))).click()

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/user-address/div[3]/button[1]"))).click()

    time.sleep(3)


'''
def main():
    module = AnsibleModule(
        argument_spec=dict(
            first_name=dict(type='str', required=True),
            last_name=dict(type='str', required=True),
            email=dict(type='str', required=True),
            extension=dict(type='str', required=True),
            acf2=dict(type='str', required=True),
        ),
        supports_check_mode=True
    )

    
    first_name = module.params['first_name']
    last_name = module.params['last_name']
    email = module.params['email']
    extension = module.params['extension']
    acf2 = module.params['acf2']

    try:
        result = vm(first_name, last_name, email, extension, acf2)
        module.exit_json(changed=True, msg='Succesfully Created Voicemail', result=result)
    except Exception as e:
        module.fail_json(msg=str(e))

if __name__ == '__main__':
    main()'''


response = vm('automation', 'test', 'automation.test@sunlife.com', '3319716', 'zz99')
print(response)