import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#To Invoke chrome
  # Import a class called webdriver
     # 1. webdriver checks with a chrome driver and invokes the chrome

driver = webdriver.Chrome() # all the details driven form this

driver.get("https://rahulshettyacademy.com") # Hit an api "get" is used

driver.maximize_window() # maximizes the window
print(driver.title)      # Gets the title of the tab
print(driver.current_url)  # Gets the url


# To invoke the chrome locally, typically used in VPN situation
#     --where the python unable to connect with chromedriver
#     -- Connected using "Service" Class

driver_local = Service(r"C:\Users\harih\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
localDriver = webdriver.Chrome(service=driver_local) # send it as Parameter
localDriver.get("https://rahulshettyacademy.com")






time.sleep(5) # TO delay the browser to close