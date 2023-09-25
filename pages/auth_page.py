import os

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class MainAuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.automationexercise.com/products'

        super().__init__(web_driver, url)

    # Main search field
    search = WebElement(id='search_product')

    # Search button
    search_run_button = WebElement(xpath='//button[@type="button"]')

    # Titles of the products in search results
    products_titles = ManyWebElements(xpath="//div[contains(@class, 'productinfo text-center')]")

    product_prices = ManyWebElements(CSS=".productinfo.text-center>h2"[0])

    # authentication page locators: fields and buttons
    username_field = WebElement(id='username')
    passw_field = WebElement(id='password')
    submit_btn = WebElement(id='kc-login')

    remember_checkbox = WebElement(name='rememberMe')
    forgot_pass_link = WebElement(id='forgot_password')
    register_link = WebElement(id='kc-register')

    phone_tab = WebElement(id='t-btn-tab-phone')
    mail_tab = WebElement(id='t-btn-tab-mail')
    login_tab = WebElement(id='t-btn-tab-login')
    ls_n_tab = WebElement(id='t-btn-tab-ls')

    # registration page: fields and locators
    name_fld = WebElement(name='firstName')
    surname_field = WebElement(name='lastName')
    region_fld = ()
    adress_or_phone_fld = WebElement(id='address')
    passw_fld = WebElement(id='password')
    passw_confirm_fld = WebElement(id='password-confirm')
    submit_btn_reg = WebElement(link_text=' Зарегистрироваться ')

    # reset password page: fields and locators
    """Каптча на странцие - автоматизацию пока не смогу"""
    phone_tab_to_reset = WebElement(id='t-btn-tab-phone')
    mail_tab_to_reset = WebElement(id='t-btn-tab-mail')
    login_tab_reset = WebElement(id='t-btn-tab-login')
    ls_n_tab_to_reset = WebElement(id='t-btn-tab-ls')
    username_field_to_reset = WebElement(id='username')
    continue_btn = WebElement(id='reset')
    back_btn = WebElement(id='reset-back')

    # authentication with temporary code: fields and locators
    page_name = WebElement(link_text='Авторизация по коду')
    hint_text = WebElement(class_name='card-container__desc')
    input_field = WebElement(id='address')
    submit_btn_to_get_code = WebElement(id='otp_get_code')
    redirect_to_auth = WebElement(id='standard_auth_btn')

    # page to enter confirmation codes
    text_field_wth_email = WebElement(link_text='На почту sea-of-max@yandex.ru') #Здесь вставить переменную с почтой.
    hange_btn = WebElement(name='otp_back_phone')
    six_wind_for_code = ['rt-code-0', 'rt-code-1', 'rt-code-2', 'rt-code-3', 'rt-code-4', 'rt-code-5']
    resend_btn = WebElement(name='otp_resend_code')