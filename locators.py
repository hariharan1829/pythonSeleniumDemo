import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

# Interact with HTML:
          # Locators: ID, ClassName, CssSelector, name, linkText, Xpath
          # Taken form the inspecting in web page
#By Name & ID
driver.find_element(By.NAME, "email").send_keys("hari@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID,"exampleCheck1").click()

# By CSSSelector tagname[attribute='value']
   # we can use #id, .classname

driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Hariharan")

driver.find_element(By.CSS_SELECTOR, "input[name='bday']").send_keys("08/18/1996")

driver.find_element(By.CSS_SELECTOR, "#inlineRadio2").click()

#To select static dropdown

dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1")) # Import select
  #Examples
dropdown.select_by_index(1)
#dropdown.select_by_visible_text("Male")
#dropdown.deselect_by_value()

# By Xpath  //tagname[@attribute='value']
driver.find_element(By.XPATH, "//input[@type='submit']").click()

    # if the xpath is mot unique we can send with index
driver.find_element(By.XPATH, "(//input[@name='name'])[2]").send_keys("Hari")

# By ClassName
success_msg = driver.find_element(By.CLASS_NAME, "alert-success").text
print(success_msg)
assert "success" in success_msg















time.sleep(20)