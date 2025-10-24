import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()

driver.find_element(By.LINK_TEXT,"Click Here").click()

# To axis to the child window, 1st need to get the window names

windowNames = driver.window_handles  # this will list the window names
print(windowNames)                   # ['2F0F4A145A1B42FA4018B53BCC079A92', 'FEB7BEB3623032BF8A72F83390F18883']

driver.switch_to.window(windowNames[1])    # switch_to.window(windowNames[1]) pass which window to axis in index
print(driver.find_element(By.CSS_SELECTOR,".example").text)
driver.close()   # close the child

driver.switch_to.window(windowNames[0])   # to back to parent
assert "Opening a new window" == driver.find_element(By.TAG_NAME,"h3").text
time.sleep(5)