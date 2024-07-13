import os
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from dotenv import load_dotenv
import time
import json

with open("data.json", "w") as f:
    json.dump([], f)

def write_json(new_data, filename='data.json'):
    with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data.append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)

browser = webdriver.Chrome()
browser.get('https://listado.mercadolibre.com.ve/telefono-samsung#D[A:telefono%20samsung]')

isNextDisabled = False

while not isNextDisabled:
    try:
        element = WebDriverWait(browser, 10).until(EC.presence_of_element_located(
            (By.CLASS_NAME, 'ui-search-results')))

        items = browser.find_elements(By.CLASS_NAME, "ui-search-layout__item")

        for item in items:
            #get title
            title = item.find_element(By.CLASS_NAME, "ui-search-item__title").text
            price = "No Price Found"

            try:
                #get price
                price = item.find_element(By.CLASS_NAME, "andes-money-amount__fraction").text
            except:
                pass

            print("Title: " + title)
            print("Price: " + price)

            write_json({
                "title": title,
                "price": price,
            })

        next_btn = WebDriverWait(browser, 10).until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/main/div/div[2]/section/div[9]/nav/ul/li[3]/a'))).click()

        # next_class = next_btn.get_attribute('class')

        # if "disabled" in next_class:
        #     isNextDisabled = True
        # else:
        #     browser.find_element(By.CLASS_NAME, 'andes-pagination__link').click()

    except Exception as e:
        print(e, "Main Error")
        isNextDisabled = True