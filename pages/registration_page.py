import os

from pages.base import WebPage
from pages.elements import WebElement


class MainRegistrationPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("URL") or 'https://b2c.passport.rt.ru'

        super().__init__(web_driver, url)

    # registration page: fields and locators
    register_link = WebElement(id='kc-register')
    name_fld = WebElement(name='firstName')
    surname_field = WebElement(name='lastName')
    region_fld = WebElement(class_name='rt-input__placeholder--top')
    adress_or_phone_fld = WebElement(id='address')
    passw_fld = WebElement(id='password')
    passw_confirm_fld = WebElement(id='password-confirm')
    submit_btn_reg = WebElement(class_name='register-form__reg-btn')
    change_adr_btn = WebElement(name='otp_back_phone')