import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

# RadioBtn Dynamic

RadioBtn = driver.find_elements(By.XPATH, "//input[@type='radio']")
#RadioBtn[2].click()  # this will select the 2nd radio, use when the options are not changed else go with loop
print(len(RadioBtn))

for Radio in RadioBtn:
    if Radio.get_attribute("value") == "radio2":
        Radio.click()
        assert Radio.is_selected()
        break

# Example for is_displayed

assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert driver.find_element(By.ID, "displayed-text").is_displayed()



time.sleep(5)