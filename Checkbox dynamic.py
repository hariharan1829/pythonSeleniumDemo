import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()


# Dynamic Checkbox

checkboxCount = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(checkboxCount))

for checkBox in checkboxCount:
    if checkBox.get_attribute("value") == "option2":
        checkBox.click()
        assert checkBox.is_selected()      # to check weather, it is checked or not
        break

time.sleep(10)