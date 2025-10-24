from selenium import webdriver

chrome_options = webdriver.ChromeOptions()

#There are lots of chrome_options we can check in programcreek.com website

chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

print(driver.title)