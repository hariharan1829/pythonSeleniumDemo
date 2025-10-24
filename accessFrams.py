import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/iframe")


# change the words inside the Iframe
       # selenium does not access the Iframe because it is not a part of the current HTML
driver.switch_to.frame("mce_0_ifr")         # Switch to frame and give its Id
driver.find_element(By.CSS_SELECTOR,"div[aria-label='Close']").click()
driver.find_element(By.ID,"tinymce").clear()
driver.find_element(By.ID,"tinymce").send_keys("Im able to automate frame")

driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR, "h3").text)


time.sleep(5)