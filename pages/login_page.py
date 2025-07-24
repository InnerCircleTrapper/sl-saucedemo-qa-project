from selenium.webdriver.common.by import By

class LoginPage:
    USER = (By.ID, "user-name")
    PASS = (By.ID, "password")
    BTN  = (By.ID, "login-button")

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def open(self):
        self.driver.get(self.base_url)

    def login(self, username, password):
        self.driver.find_element(*self.USER).send_keys(username)
        self.driver.find_element(*self.PASS).send_keys(password)
        self.driver.find_element(*self.BTN).click()
