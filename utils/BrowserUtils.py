class Browser_utils:

    def __init__(self, driver):
        self.driver = driver


    def browser_title(self):
        return self.driver.title
