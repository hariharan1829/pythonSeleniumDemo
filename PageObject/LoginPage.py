from selenium.webdriver.common.by import By

from PageObject.shop import ShopPage
from utils.BrowserUtils import Browser_utils


class LoginPage(Browser_utils):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.userName = (By.ID, "username")
        self.password = (By.ID, "password")
        self.signInBtn = (By.ID, "signInBtn")



    def login(self, username, password):
        self.driver.find_element(*self.userName).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.signInBtn).click()
        shopPage = ShopPage(self.driver)
        return shopPage