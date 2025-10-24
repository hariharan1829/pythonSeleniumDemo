import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()

#To select static dropdown

#dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1")) # Import select
  #Examples
#dropdown.select_by_index(1)
#dropdown.select_by_visible_text("Male")
#dropdown.deselect_by_value()

#To select Dynamic dropdown

driver.find_element(By.ID,"autosuggest").send_keys("ind")
time.sleep(3)

counties = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(counties))

for selectCountry in counties:
    if selectCountry.text == "India":
        selectCountry.click()
        break

# To check whether, the India is selected, check with assert

        # .text is used to see the static text, after changing anything we need to use getattribute

assert driver.find_element(By.ID,"autosuggest").get_attribute("value") == "india"

















time.sleep(20)