import os
import uuid

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

base_url = os.getenv('URL')


@pytest.fixture()
def set_driver(request):
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    service_set = Service(r"C:\SF\GITHUB\chromedriver_win32\chromedriver-win64\chromedriver-win64\chromedriver.exe")
    w_driver = webdriver.Chrome(service=service_set, options=options)
    w_driver.maximize_window()

    return w_driver


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # This function helps to detect that some test failed
    # and pass this information to teardown:

    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture()
def web_driver(set_driver, request):
    w_driver = set_driver

    yield w_driver

    if request.node.rep_call.failed:
        w_driver.save_screenshot('screenshots/' + str(uuid.uuid4()) + '.png')

        print('URL:', w_driver.current_url)
        print('Browser logs:')
        for log in w_driver.get_log('browser'):
            print(log)

    w_driver.quit()
