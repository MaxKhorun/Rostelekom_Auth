from selenium.webdriver.common.by import By

class AuthLPageLocators():
    username_field = (By.ID, 'username')
    passw_field = (By.ID, 'password')
    submit_btn = (By.ID, 'kc-login')
    remember_checkbox = (By.NAME, 'rememberMe')
    forgot_pass_link = (By.ID, 'forgot_password')
    register_link = (By.ID, 'kc-register')
    phone_tab = (By.ID, 't-btn-tab-phone')
    mail_tab = (By.ID, 't-btn-tab-mail')
    login_tab = (By.ID, 't-btn-tab-login')
    ls_n_tab = (By.ID, 't-btn-tab-ls')

class RegistrationPageLocators():
    name_fld = (By.NAME, 'firstName')
    surname_field = (By.NAME, 'lastName')
    region_fld = ()
    adress_or_phone_fld = (By.ID, 'address')
    passw_fld = (By.ID, 'password')
    passw_confirm_fld = (By.ID, 'password-confirm')
    submit_btn = (By.LINK_TEXT, ' Зарегистрироваться ')


class ResetPasswPageLocators():
    """Каптча на странцие - автоматизацию пока не смогу"""
    phone_tab = (By.ID, 't-btn-tab-phone')
    mail_tab = (By.ID, 't-btn-tab-mail')
    login_tab = (By.ID, 't-btn-tab-login')
    ls_n_tab = (By.ID, 't-btn-tab-ls')
    username_field = (By.ID, 'username')
    continue_btn = (By.ID, 'reset')
    back_btn = (By.ID, 'reset-back')
    pass

class TemporaryCodePageLocators():
    page_name = (By.LINK_TEXT, 'Авторизация по коду')
    hint_text = (By.CLASS_NAME, 'card-container__desc')
    input_field = (By.ID, 'address')
    submit_btn = (By.ID, 'otp_get_code')
    redirect_to_auth = (By.ID, 'standard_auth_btn')

class ConfirmationCodeLocators():

    text_field_wth_email = (By.LINK_TEXT, 'На почту sea-of-max@yandex.ru') #Здесь вставить переменную с почтой.
    hange_btn = (By.NAME, 'otp_back_phone')
    six_wind_for_code = ['rt-code-0', 'rt-code-1', 'rt-code-2', 'rt-code-3', 'rt-code-4', 'rt-code-5']
    resend_btn = (By.NAME, 'otp_resend_code')
