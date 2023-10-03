import pytest
from time import sleep

from selenium.webdriver.common.by import By

from pages.auth_page import MainAuthPage
from ..settings import phone_1, pass_phone_1, login_email_1, login_email_2, \
    passw_email_2, passw_email_1, login_1, login_phone_1, phone_2, long_email

parametrize = pytest.mark.parametrize


@parametrize('login_data', [phone_1, login_phone_1], ids=['correct phone 1', 'correct login 1'])
@parametrize('passw_data', [pass_phone_1], ids=['correct pass 1'])
def test_auth_standard(web_driver, login_data, passw_data):

    page = MainAuthPage(web_driver)

    assert page.text_above_fields.get_text() == "Авторизация"
    try:
        assert 'rt-tab--active' in page.phone_tab.get_attribute('class')
    except AssertionError as error:
        print('\nATTENTION!\nPHONE tab is not default after page is being loaded.\n',
              '\n', error)

    if page.captcha.is_visible():
        print('Captcha block is on the page')
        raise AssertionError

    else:

        page.username_field = login_data
        page.passw_field.send_keys(passw_data)
        page.remember_checkbox.click()
        page.submit_btn.click()
        page.wait_page_loaded()

        page.screenshot(file_name='auth_stnd_phone.png')
        pers_data = {'login_header_btn': web_driver.find_element(By.CLASS_NAME, 'StyledHeaderTopPartMenuItemLk-kHgfwO').text,
                     'lk_name': web_driver.find_element(By.CLASS_NAME, 'sc-bvFjSx iqOiiv').text}
        print(pers_data)

        assert pers_data['login_header_btn'] == 'Личный кабинет' and pers_data['lk_name'] == 'Макс'


@parametrize('login_data', [phone_2, login_email_2, long_email, '!"№;%:?*()', '8911011121213'],
             ids=['неверная пара к паролю', 'неверная пара к паролю', 'очень длинный имэйл', 'specials', 'long string'])
@parametrize('passw_data', [passw_email_2+'e', 'ghdkjl H8', 'ghdkjlH8ghdkjlH83r5t5', ''],
             ids=['just wrong', 'with space', '21 symbols', 'empty'])
def test_auth_wrong_input(web_driver, login_data, passw_data):

    page = MainAuthPage(web_driver)
    assert page.text_above_fields.get_text() == "Авторизация"
    try:
        assert 'rt-tab--active' in page.phone_tab.get_attribute('class')
    except AssertionError as error:
        print('\nATTENTION!\nPHONE tab is not default after page is being loaded.\n',
              '\n', error)

    if page.captcha.is_visible():
        print('Captcha block is on the page')
        raise AssertionError

    else:
        page.username_field = login_data
        page.passw_field.send_keys(passw_data)
        page.remember_checkbox.click()
        page.submit_btn.click()
        page.wait_page_loaded()

        page.screenshot(file_name='auth_stnd_phone.png')

        assert web_driver.find_element(By.CLASS_NAME, 'card-error__message').is_displayed() \
            and web_driver.find_element(By.CLASS_NAME, 'card-error__message').is_displayed().text == 'Неверный логин или пароль' \
            and 'rt-link--orange' in page.forgot_pass_link.get_attribute('class')


def test_auth_with_empty_captcha(web_driver):

    page = MainAuthPage(web_driver)

    assert page.text_above_fields.get_text() == "Авторизация"
    try:
        assert 'rt-tab--active' in page.phone_tab.get_attribute('class')
    except AssertionError as error:
        print('\nATTENTION!\nPHONE tab is not default after page is being loaded.\n',
              '\n', error)

    if page.captcha.is_visible():

        page.username_field = login_1
        page.passw_field.send_keys(pass_phone_1)
        page.remember_checkbox.click()
        page.submit_btn.click()

        page.screenshot(file_name='empty_captcha.png')

        assert web_driver.find_element(By.ID, 'form-error-message').text == 'Неверно введен текст с картинки'
    else:
        print('На странице нет формы с вводом каптчи')


def test_empty_both_fields(web_driver):

    page = MainAuthPage(web_driver)
    assert page.text_above_fields.get_text() == "Авторизация"
    try:
        assert 'rt-tab--active' in page.phone_tab.get_attribute('class')
    except AssertionError as error:
        print('\nATTENTION!\nPHONE tab is not default after page is being loaded.\n',
              '\n', error)

    page.phone_tab.click()
    page.submit_btn.click()

    assert web_driver.find_element(By.CLASS_NAME, 'rt-input-container__meta--error').text == 'Введите номер телефона'

    page.mail_tab.click()
    page.submit_btn.click()

    assert web_driver.find_element(By.CLASS_NAME,
                                   'rt-input-container__meta--error').text == 'Введите адрес, указанный при регистрации'

    page.login_tab.click()
    page.submit_btn.click()

    assert web_driver.find_element(By.CLASS_NAME,
                                   'rt-input-container__meta--error').text == 'Введите логин, указанный при регистрации'

    page.ls_n_tab.click()
    page.submit_btn.click()

    assert web_driver.find_element(By.CLASS_NAME,
                                   'rt-input-container__meta--error').text == 'Введите номер вашего лицевого счета'


def test_phone_input_n_tabs_changing(web_driver):
    """Interacting with tabs and fields: tabs are changing depending on information typed in. """

    page = MainAuthPage(web_driver)

    phone_tab_status = page.phone_tab.get_attribute('class')

    # проверка, что при загрузке страницы выбран таб - телефон
    try:
        assert 'rt-tab--active' in phone_tab_status
    except:
        print('\n\nPHONE tab is not default after page is being loaded')

    # активируем таб с логином, вводим в поле телефон для проверки автоматического переключения таба.
    page.login_tab.click()
    log_tab_status = page.login_tab.get_attribute('class')

    try:
        assert 'rt-tab--active' in log_tab_status
    except:
        print('\n\nLOG tab is not being chosen')

    page.username_field = phone_1
    page.passw_field.click()
    sleep(1) # в данном случае проверки выбрано принудительное ожидание в 1 сек.
    phone_tab_status = page.phone_tab.get_attribute('class')

    try:
        assert 'rt-tab--active' in phone_tab_status
    except:
        print('\n\nLOG tab is not changing to PHONE tab after phone number is typed in username filed')

    page.mail_tab.click()
    email_tab_status = page.mail_tab.get_attribute('class')

    try:
        assert 'rt-tab--active' in email_tab_status
    except:
        print('\n\nMAIL tab is not being choosing')

    page.username_field = phone_1
    page.passw_field.click()
    sleep(1) # в данном случае проверки выбрано принудительное ожидание в 1 сек.
    phone_tab_status = page.phone_tab.get_attribute('class')
    try:
        assert ('rt-tab--active' in phone_tab_status)
    except:
        print('\n\nMAIL tab is not changing to PHONE tab after phone number is typed in username filed')

    page.ls_n_tab.click()
    ls_tab_status = page.ls_n_tab.get_attribute('class')

    try:
        assert 'rt-tab--active' in ls_tab_status
    except:
        print('\n\nLS tab is not being choosing')

    page.username_field = phone_1
    page.passw_field.click()
    sleep(1) # в данном случае проверки выбрано принудительное ожидание в 1 сек.
    phone_tab_status = page.phone_tab.get_attribute('class')
    try:
        assert ('rt-tab--active' in phone_tab_status)
    except:
        print('\n\nLS tab is not changing to PHONE tab after phone number is typed in username filed')


def test_email_input_n_tabs_changing(web_driver):
    """Interacting with tabs and fields: tabs are changing depending on information typed in. """

    page = MainAuthPage(web_driver)

    phone_tab_status = page.phone_tab.get_attribute('class')
    if 'rt-tab--active' not in phone_tab_status:
        page.phone_tab.click()
        phone_tab_status = page.phone_tab.get_attribute('class')

    try:
        assert 'rt-tab--active' in phone_tab_status
    except:
        print('\n\nPHONE tab is not being chosen')

    page.username_field = login_email_1
    page.passw_field.click()
    sleep(1) # в данном случае проверки выбрано принудительное ожидание в 1 сек.
    mail_tab_status = page.mail_tab.get_attribute('class')

    try:
        assert 'rt-tab--active' in mail_tab_status
    except:
        print('\n\nPHONE tab is not changing to MAIL tab after email is typed in username filed')

    page.login_tab.click()
    login_tab_status = page.login_tab.get_attribute('class')

    try:
        assert 'rt-tab--active' in login_tab_status
    except:
        print('\n\nLOGIN tab is not being choosing')

    page.username_field = login_email_1
    page.passw_field.click()
    sleep(1) # в данном случае проверки выбрано принудительное ожидание в 1 сек.
    mail_tab_status = page.mail_tab.get_attribute('class')
    try:
        assert ('rt-tab--active' in mail_tab_status)
    except:
        print('\n\nLOGIN tab is not changing to MAIL tab after email is typed in username filed')

    page.ls_n_tab.click()
    ls_tab_status = page.ls_n_tab.get_attribute('class')

    try:
        assert 'rt-tab--active' in ls_tab_status
    except:
        print('\n\nLS tab is not being choosing')

    page.username_field = login_email_1
    page.passw_field.click()
    sleep(1) # в данном случае проверки выбрано принудительное ожидание в 1 сек.
    mail_tab_status = page.mail_tab.get_attribute('class')
    try:
        assert ('rt-tab--active' in mail_tab_status)
    except:
        print('\n\nLS tab is not changing to MAIL tab after email is typed in username filed')


def test_login_input_n_tabs_changing(web_driver):
    """Interacting with tabs and fields: tabs are changing depending on information typed in. """

    page = MainAuthPage(web_driver)

    phone_tab_status = page.phone_tab.get_attribute('class')
    if 'rt-tab--active' not in phone_tab_status:
        page.phone_tab.click()
        phone_tab_status = page.phone_tab.get_attribute('class')

    try:
        assert 'rt-tab--active' in phone_tab_status
    except:
        print('\n\nPHONE tab is not being chosen')

    page.username_field = login_1
    page.passw_field.click()
    sleep(1)  # в данном случае проверки выбрано принудительное ожидание в 1 сек.
    login_tab_status = page.login_tab.get_attribute('class')

    try:
        assert 'rt-tab--active' in login_tab_status
    except:
        print('\n\nPHONE tab is not changing to LOGIN tab after LOGIN is typed in username filed')

    page.mail_tab.click()
    mail_tab_status = page.mail_tab.get_attribute('class')

    try:
        assert 'rt-tab--active' in mail_tab_status
    except:
        print('\n\nMAIL tab is not being choosing')

    page.username_field = login_1
    page.passw_field.click()
    sleep(1)  # в данном случае проверки выбрано принудительное ожидание в 1 сек.
    login_tab_status = page.login_tab.get_attribute('class')

    try:
        assert 'rt-tab--active' in login_tab_status
    except:
        print('\n\nMAIL tab is not changing to LOGIN tab after LOGIN is typed in username filed')

    page.ls_n_tab.click()
    ls_tab_status = page.ls_n_tab.get_attribute('class')

    try:
        assert 'rt-tab--active' in ls_tab_status
    except:
        print('\n\nLS tab is not being choosing')

    page.username_field = login_1
    page.passw_field.click()
    sleep(1)  # в данном случае проверки выбрано принудительное ожидание в 1 сек.
    login_tab_status = page.login_tab.get_attribute('class')

    try:
        assert 'rt-tab--active' in login_tab_status
    except:
        print('\n\nLS tab is not changing to LOGIN tab after LOGIN is typed in username filed')


def test_ls_tab_behaviour_input(web_driver):
    """Interacting with tabs and fields: tabs are changing depending on information typed in. """

    page = MainAuthPage(web_driver)

    page.ls_n_tab.click()
    ls_tab_status = page.ls_n_tab.get_attribute('class')

    try:
        assert 'rt-tab--active' in ls_tab_status
    except:
        print('\n\nLS tab is not being choosing')

    page.username_field = login_1
    page.passw_field.click()
    sleep(1)  # в данном случае проверки выбрано принудительное ожидание в 1 сек.
    login_tab_status = page.login_tab.get_attribute('class')

    try:
        assert 'rt-tab--active' in login_tab_status
    except:
        print('\n\nLS tab is not changing to LOGIN tab after login is typed in username filed')

    page.ls_n_tab.click()
    ls_tab_status = page.ls_n_tab.get_attribute('class')

    try:
        assert 'rt-tab--active' in ls_tab_status
    except:
        print('\n\nLS tab is not being choosing')

    page.refresh()
    page.ls_n_tab.click()
    page.username_field.send_keys(phone_1)
    page.passw_field.click()
    sleep(1)  # в данном случае проверки выбрано принудительное ожидание в 1 сек.
    phone_tab_status = page.phone_tab.get_attribute('class')

    try:
        assert 'rt-tab--active' in phone_tab_status
    except:
        print('\n\nLS tab is not changing to PHONE tab after phone number is typed in username filed')

    page.ls_n_tab.click()
    ls_tab_status = page.ls_n_tab.get_attribute('class')

    try:
        assert 'rt-tab--active' in ls_tab_status
    except:
        print('\n\nLS tab is not being choosing')

    page.refresh()
    page.ls_n_tab.click()
    page.username_field.send_keys(login_email_1)
    page.passw_field.click()
    sleep(1)  # в данном случае проверки выбрано принудительное ожидание в 1 сек.
    mail_tab_status = page.mail_tab.get_attribute('class')

    try:
        assert 'rt-tab--active' in mail_tab_status
    except:
        print('\n\nLS tab is not changing to MAIL tab after email is typed in username filed')


@parametrize('input_data', [phone_1, ''], ids=['correct phone number', 'empty'])
def test_auth_temp_code_to_phonenumber(web_driver, input_data):

    page = MainAuthPage(web_driver)

    if page.btn_to_get_code_auth_page.is_visible():
        page.btn_to_get_code_auth_page.click()
        url = page.get_current_url()
        if page.captcha.is_visible():
            print('Captcha block is on the page')
            raise AssertionError

        page.input_field = input_data
        page.submit_btn_to_get_code.click()

        if (page.get_current_url() != url) and (page.text_above.get_text() == 'Код подтверждения отправлен'):
            hint_text = page.hint_text.get_text()

            assert phone_1 in hint_text \
                and page.code_fields.is_visible()

        if page.get_current_url() == url and \
                web_driver.find_element(By.CLASS_NAME, 'rt-input-container__meta--error').is_displayed():
            error_msg = web_driver.find_element(By.CLASS_NAME, 'rt-input-container__meta--error').text
            assert error_msg == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'
    else:
        print('Переход на страницу невозможен - кнопка отсутствует на странице.')
        raise AssertionError


@parametrize('input_data', [login_email_2, ''], ids=['correct phone number', 'empty'])
def test_auth_temp_code_to_email(web_driver, input_data):

    page = MainAuthPage(web_driver)

    if page.btn_to_get_code_auth_page.is_visible():
        page.btn_to_get_code_auth_page.click()
        url = page.get_current_url()
        if page.captcha.is_visible():
            print('Captcha block is on the page')
            raise AssertionError

        page.input_field = input_data
        page.submit_btn_to_get_code.click()

        if (page.get_current_url() != url) and (page.text_above.get_text() == 'Код подтверждения отправлен'):
            hint_text = page.hint_text.get_text()

            assert login_email_2 in hint_text \
                   and page.code_fields.is_visible()

        if page.get_current_url() == url and \
                web_driver.find_element(By.CLASS_NAME, 'rt-input-container__meta--error').is_displayed():
            error_msg = web_driver.find_element(By.CLASS_NAME, 'rt-input-container__meta--error').text
            assert error_msg == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'

    else:
        print('Переход на страницу невозможен - кнопка отсутсвует на странице.')
        raise AssertionError


@parametrize('input_data', [login_email_2, phone_1, ''], ids=['correct email', 'correct phone number', 'empty'])
def test_change_phone_adress(web_driver, input_data):
    page = MainAuthPage(web_driver)

    if page.btn_to_get_code_auth_page.is_visible():
        page.btn_to_get_code_auth_page.click()
        url = page.get_current_url()
        if page.captcha.is_visible():
            print('Captcha block is on the page')
            raise AssertionError

        page.input_field = input_data
        page.submit_btn_to_get_code.click()

        if (page.get_current_url() != url) and (page.text_above.get_text() == 'Код подтверждения отправлен'):
            hint_text = page.hint_text.get_text()

            assert phone_1 in hint_text \
                   and page.code_fields.is_visible()
            assert web_driver.find_element(By.CLASS_NAME, 'code-input-container__timeout').is_displayed() \
                and web_driver.find_element(By.CLASS_NAME, 'code-input-container__timeout')

            page.change_address.click()
            assert web_driver.find_element(By.ID, 'card-container__title') == 'Авторизация по коду' \
                and web_driver.find_element(By.CLASS_NAME, 'otp-form__timeout')

            page.username_field = input_data
            page.submit_btn_to_get_code.click()

            assert url == page.get_current_url()

        if page.get_current_url() == url and \
                web_driver.find_element(By.CLASS_NAME, 'rt-input-container__meta--error').is_displayed():
            error_msg = web_driver.find_element(By.CLASS_NAME, 'rt-input-container__meta--error').text
            assert error_msg == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'
    else:
        print('Переход на страницу невозможен - кнопка отсутствует на странице.')
        raise AssertionError
