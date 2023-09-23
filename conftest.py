import uuid

import pytest
from selenium import webdriver


@pytest.fixture()
def web_driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    w_driver = webdriver.Chrome(options=options)
    w_driver.set_window_size(1200, 800)

    yield w_driver

    if request.node.rep_call.failed:
        w_driver.save_screenshot('screenshots/' + str(uuid.uuid4()) + '.png')

        print('URL:', w_driver.current_url)
        print('Browser logs:')
        for log in w_driver.get_log('browser'):
            print(log)
