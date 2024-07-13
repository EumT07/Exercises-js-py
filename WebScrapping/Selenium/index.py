#pip install selenium
#pip install python-dotenv

import os
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from dotenv import load_dotenv
import time

load_dotenv()

#Using Chrome
driver = webdriver.Chrome()
driver.get("https://languagedoctors.bamboohr.com/login.php?r=%2Fhome")

driver.implicitly_wait(5)

#Email
useremail = os.getenv("user")
email = driver.find_element(By.ID, 'lemail')
email.send_keys(useremail)
#Password
userPass = os.getenv("pass")
password = driver.find_element(By.ID, 'password')
password.send_keys(userPass)
#Button
login = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
login.click()

#Get info
ads_info = driver.find_element(By.CLASS_NAME, "MuiBox-root")

if(ads_info):
    confirm_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "css-fngne8"))).click()

    #stop or start
    stop = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "css-fngne8"))).click()

cookies = driver.get_cookies()
print(cookies)
time.sleep(1000)

