import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

action = ActionChains(driver)       # Import ActionChains for mouse actions and add perform @ the end
#action.click_and_hold()  # Long Press
#action.double_click()     # Double Click
#action.drag_and_drop()    # Drag And Drop
#action.context_click()    # Right Click
#action.move_to_element()   # Move to the elememt

action.double_click(driver.find_element(By.CSS_SELECTOR, "#checkBoxOption1")).perform()

action.move_to_element(driver.find_element(By.CSS_SELECTOR, "#mousehover")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()

time.sleep(10)