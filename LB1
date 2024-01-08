from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

driver = webdriver.Chrome()
driver.get('https://iotvega.com/product')

driver.execute_script("window.scrollTo(0, 500);")
time.sleep(10)

itemName = driver.find_elements(By.CLASS_NAME, "product-name")
itemPrice = driver.find_elements(By.CLASS_NAME, "product-cost")

Name = []
Price = []

for elem in itemName:
    Name.append(f'{elem.text}')

for elem in itemPrice:
    Price.append(f'{elem.text}')

df = pd.DataFrame({'Наименование': Name, 'Цена': Price})
df.to_excel('./output.xlsx')

driver.quit()
