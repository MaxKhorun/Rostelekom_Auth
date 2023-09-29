import os

from pages.base import WebPage
from pages.elements import WebElement


class MainAuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("URL") or 'https://b2c.passport.rt.ru'

        super().__init__(web_driver, url)

    # authentication page tabs:
    phone_tab = WebElement(id='t-btn-tab-phone')
    mail_tab = WebElement(id='t-btn-tab-mail')
    login_tab = WebElement(id='t-btn-tab-login')
    ls_n_tab = WebElement(id='t-btn-tab-ls')

    # authentication page locators: fields and buttons:
    username_field = WebElement(id='username')
    passw_field = WebElement(id='password')
    submit_btn = WebElement(id='kc-login')
    submit_to_reg = WebElement(class_name='register-form__reg-btn')

    # authentication page links and check-box:
    remember_checkbox = WebElement(class_name='rt-checkbox__label')
    forgot_pass_link = WebElement(id='forgot_password')
    register_link = WebElement(id='kc-register')
    lk_btn = WebElement(id="lk-btn")
    user_base_info = WebElement(class_name='user-info__name-container')

    # authentication with temporary code: fields and locators
    btn_to_get_code_auth_page = WebElement(id='back_to_otp_btn')
    page_name = WebElement(link_text='Авторизация по коду') #
    hint_text = WebElement(class_name='otp-code-form-container__desc')
    input_field = WebElement(id='address')
    submit_btn_to_get_code = WebElement(id='otp_get_code')
    redirect_to_auth = WebElement(id='standard_auth_btn')

    # page to enter confirmation code; fields and buttons:
    text_above = WebElement(class_name='card-container__title')
    text_field_wth_email = WebElement(partial_link_text='На почту')  # Здесь вставить переменную с почтой.
    code_fields = WebElement(class_name='code-input-container')
    six_wind_for_code = ['rt-code-0', 'rt-code-1', 'rt-code-2', 'rt-code-3', 'rt-code-4', 'rt-code-5']
    resend_btn = WebElement(name='otp_resend_code')

    # reset page
    #    text field: Восстановление пароля:
    text_above_fields = WebElement(class_name='card-container__title')

    #    tabs of reset password form:
    phone_tab_to_reset = WebElement(id='t-btn-tab-phone')
    mail_tab_to_reset = WebElement(id='t-btn-tab-mail')
    login_tab_reset = WebElement(id='t-btn-tab-login')
    ls_n_tab_to_reset = WebElement(id='t-btn-tab-ls')
    error_msg = WebElement(id='form-error-message')

    #    some description on captcha block, fields and buttons of reset password form:
    username_field_to_reset = WebElement(id='username')
    continue_btn = WebElement(id='reset')
    back_btn = WebElement(id='reset-back')
    captcha = WebElement(class_name='rt-captcha__image')
    captcha_field = WebElement(id='captcha')
