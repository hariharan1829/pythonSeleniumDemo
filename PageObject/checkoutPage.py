from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils.BrowserUtils import Browser_utils


class CheckoutPage(Browser_utils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.country_btn = (By.CSS_SELECTOR, "button[class='btn btn-success']")
        self.country_input = (By.ID, "country")
        self.country_option = (By.LINK_TEXT, "India")
        self.checkbox = (By.CSS_SELECTOR, ".checkbox.checkbox.checkbox-primary")
        self.submit_btn = (By.XPATH, "//input[@type='submit']")
        self.checkout_message = (By.CLASS_NAME, "alert-success")


    def add_address(self, selectCountry):
        self.driver.find_element(*self.country_btn).click()
        self.driver.find_element(*self.country_input).send_keys("Ind")

        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.visibility_of_element_located(self.country_option))
        self.driver.find_element(By.LINK_TEXT, selectCountry).click()
        self.check_submit()


    def check_submit(self):
        self.driver.find_element(*self.checkbox)
        self.driver.find_element(*self.submit_btn).click()


    def checkout_validation(self):
        end_message = self.driver.find_element(*self.checkout_message).text
        print(end_message)
        assert "Success! Thank you" in end_message
