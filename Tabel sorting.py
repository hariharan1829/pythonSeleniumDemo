import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.maximize_window()

driver.find_element(By.XPATH, "//th[1]").click()
webSortedItems = []

webItems = driver.find_elements(By.XPATH,"//tr/td[1]")
for ele in webItems:
    webSortedItems.append(ele.text)

originalWebSortedItems = webSortedItems.copy()
webSortedItems.sort()

assert originalWebSortedItems == webSortedItems

time.sleep(10)