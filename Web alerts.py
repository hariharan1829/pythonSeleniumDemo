import time

from selenium import webdriver
from selenium.webdriver.common.by import By

name = "Hariharan"

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.CSS_SELECTOR, "#alertbtn").click()

alert = driver.switch_to.alert   # switches to alert
alertText = alert.text
print(alertText)
if name in alertText:
    alert.accept()             # positive button
else:
    alert.dismiss()            # Negative btn



time.sleep(5)