import os

from pages.base import WebPage
from pages.elements import WebElement, ManyWebElements


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
    errors_under_fields = WebElement(class_name='rt-input-container__meta--error')
    all_errors_under_fields = ManyWebElements(class_name='rt-input-container__meta--error')
    main_locator_f_field = ManyWebElements(class_name='rt-input__placeholder--top')
    error_class = ManyWebElements(class_name='rt-input-container--error')
    container_name = ManyWebElements(class_name='rt-input-container')
