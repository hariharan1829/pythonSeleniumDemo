import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/client")
driver.maximize_window()

# By link text only if the text is wrapped in (<a>) tag
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
#driver.find_element(By.PARTIAL_LINK_TEXT, "Forgot").click()      # we can also use partial text

# By Xpath Parent to child
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("hari@gmail.com")

# By CssSelector Parent to child
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(2) input").send_keys("1234567")

# By CssSelector #ID
driver.find_element(By.CSS_SELECTOR,"#confirmPassword").send_keys("1234567")

#driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

#driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Click with text
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()


time.sleep(20)