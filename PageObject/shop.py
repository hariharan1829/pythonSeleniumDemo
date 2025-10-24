from selenium.webdriver.common.by import By

from PageObject.checkoutPage import CheckoutPage
from utils.BrowserUtils import Browser_utils


class ShopPage(Browser_utils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.products = (By.CSS_SELECTOR, "div[class='card h-100']")
        self.checkOutText = (By.XPATH, "//a[@class='nav-link btn btn-primary']")
        self.addCardBtn = (By.XPATH, "//a[@class='nav-link btn btn-primary']")


    def select_product_to_cart(self,selectedproductName ):
        products = self.driver.find_elements(*self.products)

        for product in products:
            productName = product.find_element(By.CSS_SELECTOR, " div h4 a").text
            print(productName)
            if productName == selectedproductName:
                product.find_element(By.CSS_SELECTOR, " div button").click()


    def check_out_validation(self):
        checkout_text = self.driver.find_element(*self.checkOutText).text
        checkout_text = checkout_text.replace("(current)", "").strip()
        print(checkout_text)
        assert checkout_text != "Checkout ( 0 )"
        self.driver.find_element(*self.addCardBtn).click()
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage
