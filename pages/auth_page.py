import os
from .base import BasePage
from .locators import AuthLPageLocators


class AuthPage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = os.getenv("LOGIN_URL") or 'https://b2c.passport.rt.ru'
        driver.get(url)
        self.username = driver.find_element(*AuthLPageLocators.username_field)
        self.password = driver.find_element(*AuthLPageLocators.passw_field)
        self.check_box = driver.find_element(*AuthLPageLocators.remember_checkbox)
        self.submit = driver.find_element(*AuthLPageLocators.submit_btn)

    def input_username(self):
        value = os.getenv('LOGIN_EMAIL_1')
        self.username.send_keys(value)

    def input_password(self):
        value = os.getenv('PASSW_EMAIL_1')
        self.username.send_keys(value)

    def forget_me(self):
        self.check_box.click()

    def submit_btn(self):
        self.submit.click()
