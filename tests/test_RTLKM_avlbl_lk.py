import pytest
from pages.auth_page import MainAuthPage
from ..settings import onlime_web, elk_web, start_web, smart_hone_web, keys_web, \
    elk_check_part, online_check_part, start_check_part, smart_check_part, keys_check_part

parametrize = pytest.mark.parametrize


@parametrize('url_to_check', [onlime_web, elk_web, start_web, smart_hone_web, keys_web],
             ids=['Онлайм Web', 'ЕЛК Web', 'Старт Web', 'Умный дом Web', 'Ключ Web'])
def test_available_lk_urls(web_driver, url_to_check):
    """Проверка доступности ЛК продуктов из ТЗ. """

    page = MainAuthPage(web_driver)

    page.get(url_to_check)
    url = page.get_current_url()
    if url_to_check == onlime_web:
        assert online_check_part in url
    elif url_to_check == elk_web:
        assert elk_check_part in url
    elif url_to_check == start_web:
        assert start_check_part in url
    elif url_to_check == smart_hone_web:
        assert smart_check_part in url
    elif url_to_check == keys_web:
        assert keys_check_part in url
