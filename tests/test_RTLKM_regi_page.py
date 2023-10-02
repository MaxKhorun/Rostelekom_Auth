import pytest
from selenium.webdriver.common.by import By
from pages.registration_page import MainRegistrationPage
from ..settings import phone_2, login_email_1, long_email, long_name

parametrize = pytest.mark.parametrize


def test_reg_empty_fields(web_driver):
    page = MainRegistrationPage(web_driver)

    page.register_link.click()
    url = page.get_current_url()
    text_above = web_driver.find_element(By.CLASS_NAME, 'card-container__title')

    if text_above.text == 'Регистрация':
        page.submit_btn_reg.click()
        page.screenshot(file_name='empty_fields.png')
        txt_err = []
        if url == page.get_current_url():

            errors = web_driver.find_elements(By.CLASS_NAME, 'rt-input-container__meta--error')
            txt_err = [errors[i].text for i in range(len(errors))]

            if len(txt_err) == 0:
                print('No errors on the page')
                raise AssertionError
            else:
                assert txt_err == ['Необходимо заполнить поле кириллицей. От 2 до 30 символов.',
                                        'Необходимо заполнить поле кириллицей. От 2 до 30 символов.',
                                        'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru',
                                        'Длина пароля должна быть не менее 8 символов',
                                        'Длина пароля должна быть не менее 8 символов']

    else:
        print('Загрузилась страница: {0}'.format(page.get_current_url()))
        page.screenshot(file_name='test_email_reg.png')


@parametrize('contact_data', ['Remember.ever@me.com', '+79959112267'])
@parametrize('name', ['НовыйОдин', 'НовыйДва'])
@parametrize('surname', ['КлиентОдин', 'КлиентДва'])
def test_standard_registration(web_driver, contact_data, name, surname):

    page = MainRegistrationPage(web_driver)

    page.register_link.click()
    text_above = web_driver.find_element(By.CLASS_NAME, 'card-container__title').text

    if text_above == 'Регистрация':

        page.name_fld = name
        page.surname_field = surname
        page.adress_or_phone_fld = contact_data
        page.passw_fld = '567890xcvbnmM'
        page.passw_confirm_fld = '567890xcvbnmM'
        page.submit_btn_reg.click()

        assert web_driver.find_element(By.CLASS_NAME, 'card-container__title').text == 'Подтверждение email' \
            or web_driver.find_element(By.CLASS_NAME, 'card-container__title').text == 'Подтверждение телефона' \
            and web_driver.find_element(By.CLASS_NAME, 'code-input-container__code-input').is_displayed()

    else:
        print('Загрузилась страница: {0}'.format(page.get_current_url()))
        page.screenshot(file_name='test_email_reg.png')


def test_re_registration_same_phone(web_driver):
    page = MainRegistrationPage(web_driver)

    page.register_link.click()
    text_above = web_driver.find_element(By.CLASS_NAME, 'card-container__title').text

    if text_above == 'Регистрация':

        page.name_fld = 'КлиентОдин'
        page.surname_field = 'НомерОдин'
        page.adress_or_phone_fld = phone_2
        page.passw_fld = '567890xcvbnmM'
        page.passw_confirm_fld = '567890xcvbnmM'
        page.submit_btn_reg.click()

        assert web_driver.find_element(By.CLASS_NAME, 'card-modal__card-wrapper').is_displayed() \
            and web_driver.find_element(By.CLASS_NAME, 'card-modal__title').text == 'Учётная запись уже существует' \
            and web_driver.find_element(By.NAME, 'gotoLogin').is_displayed() \
            and web_driver.find_element(By.ID, 'reg-err-reset-pass').is_displayed() \
            and web_driver.find_element(By.NAME, 'registration_confirm_btn').is_displayed()

    else:
        print('Загрузилась страница: {0}'.format(page.get_current_url()))
        page.screenshot(file_name='test_email_reg.png')


def test_re_registration_same_email(web_driver):
    page = MainRegistrationPage(web_driver)

    page.register_link.click()
    text_above = web_driver.find_element(By.CLASS_NAME, 'card-container__title').text

    if text_above == 'Регистрация':

        page.name_fld = 'КлиентДва'
        page.surname_field = 'НомерДва'
        page.adress_or_phone_fld = login_email_1
        page.passw_fld = '567890xcvbnmM'
        page.passw_confirm_fld = '567890xcvbnmM'
        page.submit_btn_reg.click()

        assert web_driver.find_element(By.CLASS_NAME, 'card-modal__card-wrapper').is_displayed() \
            and web_driver.find_element(By.CLASS_NAME, 'card-modal__title').text == 'Учётная запись уже существует' \
            and web_driver.find_element(By.NAME, 'gotoLogin').is_displayed() \
            and web_driver.find_element(By.NAME, 'reg-err-reset-pass').is_displayed()

    else:
        print('Загрузилась страница: {0}'.format(page.get_current_url()))
        page.screenshot(file_name='test_email_reg.png')


@parametrize('contact_data', [login_email_1, phone_2])
def test_back_to_change_email_adress(web_driver, contact_data):

    page = MainRegistrationPage(web_driver)

    page.register_link.click()
    text_above = web_driver.find_element(By.CLASS_NAME, 'card-container__title').text

    if text_above == 'Регистрация':
        page.name_fld = 'КлиентДва'
        page.surname_field = 'НомерДва'
        page.adress_or_phone_fld = contact_data
        page.passw_fld = '567890xcvbnmM'
        page.passw_confirm_fld = '567890xcvbnmM'
        page.submit_btn_reg.click()

        if web_driver.find_element(By.CLASS_NAME, 'card-container__title').text == 'Подтверждение email':
            page.change_adr_btn.click()


# @parametrize('contact_data', ['п@п.рф', long_email, 'йцукенгшщзх', 'qwertyuiop', '+73453425',
#                               '88133453425', '8911011121213', '!"№;%:?*()_+@mail.ru'],
#              ids=['кириллица.рф', 'very long email', 'кириллица', 'латиница', 'wrong number',
#                   'city code number', 'long number', 'specials@mail.ru'])
# @parametrize('name', ['А', 'АА', 'Аj', '!"№;%:?*()', '', '-', long_name],
#              ids=['одна буква криллицей', '2 буквы кириллицей', '2 буквы: латиница и кириллица',
#                   'specials', 'empty', 'dash', 'long_name'])
# @parametrize('surname', ['А', 'АА', 'Аj', '!"№;%:?*()', '', '-', long_name],
#              ids=['одна буква криллицей', '2 буквы кириллицей', '2 буквы: латиница и кириллица',
#                   'specials', 'empty', 'dash', 'long_name'])
# @parametrize('passw', ['ghdkjlH8', 'hdkjlH8', 'ghdkjl H8', 'ghdkjlH8ghdkjlH83r5t5', ''],
#              ids=['good', 'to short', 'with space', 'to long', 'empty'])
def test_negative_standard_registration(web_driver): #, contact_data, name, surname, passw
    page = MainRegistrationPage(web_driver)

    page.register_link.click
    text_above = web_driver.find_element(By.CLASS_NAME, 'card-container__title').text

    if text_above == 'Регистрация':

        page.name_fld = long_name
        page.surname_field = long_name
        page.adress_or_phone_fld = 'п@п.рф'
        page.passw_fld = 'ghdkjl H8'
        page.passw_confirm_fld = 'ghdkjl H8'
        page.submit_btn_reg.click()

        assert page.errors_under_fields.is_visible()

    else:
        print('Загрузилась страница: {0}'.format(page.get_current_url()))
        page.screenshot(file_name='test_email_reg.png')