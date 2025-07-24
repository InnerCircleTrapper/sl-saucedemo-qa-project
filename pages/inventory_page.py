from selenium.webdriver.common.by import By

class InventoryPage:
    TITLE = (By.CLASS_NAME, "title")
    BACKPACK_ADD = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self, driver):
        self.driver = driver

    def is_loaded(self):
        return self.driver.find_element(*self.TITLE).text == "Products"

    def add_backpack(self):
        self.driver.find_element(*self.BACKPACK_ADD).click()

    def cart_count(self):
        badge = self.driver.find_element(*self.CART_BADGE)
        return int(badge.text)
