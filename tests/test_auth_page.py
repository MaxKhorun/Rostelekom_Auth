from pages.auth_page import MainAuthPage
from settings import login_email_1, passw_email_1


def test_reset_pass_standard(web_driver):

    page = MainAuthPage(web_driver)
    page.wait_page_loaded()
    page.username_field.send_keys(login_email_1)
    page.passw_field.send_keys(passw_email_1)
    page.submit_btn.click()
