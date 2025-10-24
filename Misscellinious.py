import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v135.page import Screenshot


#To come as headless ie not showing the browser for testing

chrome_options = webdriver.ChromeOptions()    # Get webdriver.ChromeOptions() and invoke in driver's argument
chrome_options.add_argument("headless")

#To ingore all certificate errors: ie the page comes as error and we click advanced right
chrome_options.add_argument("--ignore-certificate-errors")


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()


# To auto scroll, we need to use javaScript in inspect and give that to selinium

#driver.execute_script("window.scroll(0, 900)") # scrolls to 900 pixel

driver.execute_script("window.scroll(0, document.body.scrollHeight)") # scrolls to Bottom

#To take Screenshot
driver.get_screenshot_as_file("screen.png")


time.sleep(10)