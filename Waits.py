import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
searchName = "ber"
expected_List = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actual_list = []

driver.implicitly_wait(2)         ## Global Implicit wait if not getting the locator

# Search for Products
driver.find_element(By.XPATH,"//input[@type='search']").send_keys(searchName)
time.sleep(2)              # only exception is we are using find elements below as we are not waiting for the locators

inputValue = driver.find_element(By.XPATH,"//input[@type='search']").get_attribute("value")
assert inputValue == searchName

#Expected List = Actual List
productsName = driver.find_elements(By.XPATH,"//div[@class='products']/div/h4")
print(len(productsName))
for listName in productsName:
    names = listName.text
    actual_list.append(names)

assert expected_List == actual_list


# Add to cart
productsCount = driver.find_elements(By.XPATH, "//div[@class='products']/div")
print(len(productsCount))
assert len(productsCount) > 0

for counts in productsCount:
    counts.find_element(By.XPATH,"div/button").click()  ## relative Xpath

# PROCEED TO CHECKOUT
driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()


# To check the Total of all items equals to Total amount
totalSum = driver.find_elements(By.XPATH, "//tr/td[5]/p")
print(len(totalSum))
sumOfProducts = 0
for amount in totalSum:
    sumOfProducts = sumOfProducts + int(amount.text)    # int used to convert string to integer
print(sumOfProducts)
assert sumOfProducts == int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)

# Applying promo code
driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()

#Explicit wait - unlike implicit we are using wait for only for a step - when you know
       # it will take more than Implicit wait
wait = WebDriverWait(driver,10)  # import WebDriverWait
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CSS_SELECTOR, ".promoInfo").text)
assert "Code applied" in driver.find_element(By.CSS_SELECTOR, ".promoInfo").text

# To check the Total Amount is greater than Total After Discount

totalAmount = driver.find_element(By.CSS_SELECTOR, ".totAmt").text
totalAfterDiscount = driver.find_element(By.CSS_SELECTOR, ".discountAmt").text
if "Code applied" in driver.find_element(By.CSS_SELECTOR, ".promoInfo").text:
    assert totalAmount > totalAfterDiscount


time.sleep(10)