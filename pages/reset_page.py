import os

from pages.base import WebPage
from pages.elements import WebElement


class ResetPassPage(WebPage):

    # reset password page: fields and locators
    """Каптча на странцие - автоматизацию пока нет возможности реализовать"""

    text_above_fields = WebElement(CSS='section#page-right > div > div > h1')

    phone_tab_to_reset = WebElement(id='t-btn-tab-phone')
    mail_tab_to_reset = WebElement(id='t-btn-tab-mail')
    login_tab_reset = WebElement(id='t-btn-tab-login')
    ls_n_tab_to_reset = WebElement(id='t-btn-tab-ls')
    username_field_to_reset = WebElement(id='username')
    continue_btn = WebElement(id='reset')
    back_btn = WebElement(id='reset-back')
    captcha_startwith = 'https://webapi.passport.rt.ru/captcha/getcaptcha/2.0/'
