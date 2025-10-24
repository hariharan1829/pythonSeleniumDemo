import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()
driver.implicitly_wait(2)

driver.find_element(By.XPATH,"//div/a[1]").click()

AnotherWindow = driver.window_handles

driver.switch_to.window(AnotherWindow[1])

emailSentence = driver.find_element(By.XPATH,"//div/p[2]").text
driver.close()
driver.switch_to.window(AnotherWindow[0])
emailFromSentence = emailSentence.split("at ")[1].split(" ")[0]

driver.find_element(By.CSS_SELECTOR,"#username").send_keys(emailFromSentence)
driver.find_element(By.CSS_SELECTOR,"input[type='password']").send_keys("learning")
driver.find_element(By.XPATH,"//label[2]/span[2]").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"#okayBtn").click()
driver.find_element(By.XPATH,"//input[@id='terms']").click()
driver.find_element(By.CSS_SELECTOR,"#signInBtn").click()
time.sleep(2)
errMsg= driver.find_element(By.CSS_SELECTOR,".alert-danger").text
print(errMsg)

assert errMsg

time.sleep(20)