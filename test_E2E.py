import json

import pytest

from PageObject.LoginPage import LoginPage

data_path = 'Data/test_E2E.json'
with open(data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

@pytest.mark.smoke
@pytest.mark.parametrize("test_list_item", test_list)
def test_e2eTest(open_browser, test_list_item):
    driver = open_browser
    loginPage = LoginPage(driver)
    print(loginPage.browser_title())
    shopPage = loginPage.login(test_list_item["userName"], test_list_item["password"] )
    print(shopPage.browser_title())
    shopPage.select_product_to_cart(test_list_item["productName"])
    checkoutPage = shopPage.check_out_validation()
    print(checkoutPage.browser_title())
    checkoutPage.add_address(test_list_item["country"])
    checkoutPage.checkout_validation()



#    driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()