import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.implicitly_wait(5)

driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
products = driver.find_elements(By.CSS_SELECTOR, "div[class='card h-100']")

for product in products:
    productName = product.find_element(By.CSS_SELECTOR," div h4 a").text
    print(productName)
    if productName == "Blackberry":
        product.find_element(By.CSS_SELECTOR, " div button").click()

checkout_text = driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").text
checkout_text = checkout_text.replace("(current)", "").strip()
print(checkout_text)
assert checkout_text != "Checkout ( 0 )"

driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']").click()
driver.find_element(By.ID,"country").send_keys("Ind")

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT, "India").click()
driver.find_element(By.CSS_SELECTOR, ".checkbox.checkbox.checkbox-primary").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()
end_message = driver.find_element(By.CLASS_NAME,"alert-success").text
assert "Success! Thank you" in end_message
print(end_message)

driver.close()