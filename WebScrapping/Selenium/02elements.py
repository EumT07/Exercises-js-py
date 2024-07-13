import os
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from dotenv import load_dotenv
import time

browser = webdriver.Chrome()
# browser.get("https://www.facebook.com/")
browser.get("https://listado.mercadolibre.com.ve/telefono-samsung#D[A:telefono%20samsung]")

#GET id  Element

# browser.find_element(By.ID, "email")
browser.implicitly_wait(10)
items = browser.find_elements(By.CLASS_NAME, "ui-search-layout__item")
allItems = []
for item in items:
    #get title
    title = item.find_element(By.CLASS_NAME, "ui-search-item__title").text
    #get price
    price = item.find_element(By.CLASS_NAME, "andes-money-amount__fraction").text
    #get img link
    # img_link = item.find_element(By.CLASS_NAME,"ui-search-result-image__element").get_attribute("src")

    #Creating a Dictionary
    get_items = {
        "Title": title,
        "Price": price,
        # "Img": img_link,
    }

    # allItems.append(get_items)
    # allItems.append(title)
    allItems.append(price)


print(allItems)


    
