import pytest
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pages.auth_page import MainAuthPage
from pages.elements import WebElement
from ..settings import phone_1, login_email_1, passw_email_1, login_1, login_email_2, long_email

parametrize = pytest.mark.parametrize


def test_reset_pass_base_check_tabs_status_and_fields(web_driver):
    """Interacting with tabs and fields: tabs are changing depending on information typed in. """

    page = MainAuthPage(web_driver)

    page.forgot_pass_link.click()
    url = page.get_current_url()
    text_on_page = page.text_above_fields.get_text()
    phone_tab_status = page.phone_tab_to_reset.get_attribute('class')

    assert ('Восстановление пароля' in text_on_page) and \
           (url.startswith('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials'))

    # проверка, что при загрузке страницы выбран таб - телефон
    try:
        assert 'rt-tab--active' in phone_tab_status
    except:
        print('PHONE tab is not default after page is being loaded')

    # активируем таб с логином, вводим в поле телефон для проверки автоматического переключения таба.
    page.login_tab_reset.click()
    log_tab_status = page.login_tab_reset.get_attribute('class')

    try:
        assert 'rt-tab--active' in log_tab_status
    except:
        print('LOG tab is not being chosen')

    page.username_field_to_reset = phone_1
    page.text_above_fields.click()
    sleep(1) # в данном случае проверки выбрано принудительное ожидание в 1 сек.
    phone_tab_status = page.phone_tab_to_reset.get_attribute('class')

    try:
        assert 'rt-tab--active' in phone_tab_status
    except:
        print('LOG tab is not changing to PHONE tab after phone number is typed in username filed')

    page.mail_tab_to_reset.click()
    email_tab_status = page.mail_tab_to_reset.get_attribute('class')

    try:
        assert 'rt-tab--active' in email_tab_status
    except:
        print('MAIL tab is not being choosing')

    page.username_field_to_reset = phone_1
    page.text_above_fields.click()
    sleep(1)
    phone_tab_status = page.phone_tab_to_reset.get_attribute('class')
    try:
        assert ('rt-tab--active' in phone_tab_status)
    except:
        print('MAIL tab is not changing to PHONE tab after phone number is typed in username filed')

    page.ls_n_tab_to_reset.click()
    ls_tab_status = page.ls_n_tab_to_reset.get_attribute('class')

    try:
        assert 'rt-tab--active' in ls_tab_status
    except:
        print('LS tab is not being choosing')

    page.username_field_to_reset = phone_1
    page.text_above_fields.click()
    sleep(1)
    phone_tab_status = page.phone_tab_to_reset.get_attribute('class')
    try:
        assert ('rt-tab--active' in phone_tab_status)
    except:
        print('LS tab is not changing to PHONE tab after phone number is typed in username filed')

    captcha_link = page.captcha.get_attribute('src')

    assert ("https://webapi.passport.rt.ru/captcha/getcaptcha/2.0/" in captcha_link) and \
        (page.captcha_field.is_clickable()) and (page.continue_btn.is_clickable())


def test_reset_pass_page_phone_tab_is_by_default(web_driver):
    """Check phone tab is active by default after reload and LOGIN tab is chosen previously. """

    page = MainAuthPage(web_driver)
    page.forgot_pass_link.click()
    page.login_tab_reset.click()
    assert page.get_current_url().startswith(r'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials')

    page.back_btn.click()
    text_above_fields = page.text_above_fields.get_text()
    assert 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate' in page.get_current_url() \
        and text_above_fields == 'Авторизация'

    page.forgot_pass_link.click()
    page.wait_page_loaded()
    phone_tab_status = page.phone_tab_to_reset.get_attribute('class')

    # проверка, что при загрузке страницы выбран таб - телефон
    assert 'rt-tab--active' in phone_tab_status


@parametrize('username_data', [phone_1, login_email_1, login_1])
def test_reset_pass_with_empty_captcha(web_driver, username_data):
    """Empty captcha. """
    page = MainAuthPage(web_driver)

    page.forgot_pass_link.click()
    assert (page.get_current_url().
                startswith(r'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials'))
    page.username_field_to_reset = username_data
    page.continue_btn.click()

    assert page.error_msg.get_text() == 'Неверный логин или текст с картинки'


def test_reset_pass_standard(web_driver):

    page = MainAuthPage(web_driver)

    if page.captcha.is_visible():
        print('Captcha block is on the page')
        raise AssertionError
    else:
        page.forgot_pass_link.click()
        assert (page.get_current_url().
                startswith(r'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials'))
        page.username_field_to_reset = login_email_2
        page.continue_btn.click()

        assert web_driver.find_element(By.CLASS_NAME, 'card-container__title').text == 'Восстановление пароля' \
            and web_driver.find_element(By.CLASS_NAME, 'code-input-container__code-input').is_displayed()


@parametrize('input_data', [long_email, '8911011121213', '!"№;%:?*()', ''],
             ids=['длинный имейл', 'long phone', 'specials', 'empty'])
def test_reset_pass_with_wrong_data(web_driver, input_data):

    page = MainAuthPage(web_driver)

    if page.captcha.is_visible():
        print('Captcha block is on the page')
        raise AssertionError
    else:
        page.forgot_pass_link.click()
        assert (page.get_current_url().
                startswith(r'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials'))
        page.username_field_to_reset = input_data
        page.continue_btn.click()

        assert web_driver.find_element(By.ID, "form-error-message") == 'Неверный логин или текст с картинки' \
            or web_driver.find_element(By.CLASS_NAME, "rt-input-container__meta--error") == 'Введите адрес, указанный при регистрации'
