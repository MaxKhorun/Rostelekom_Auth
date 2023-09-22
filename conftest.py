import uuid

import pytest
from selenium import webdriver

def web_driver(request):
    browser = webdriver.Chrome()
    browser.set_window_size(1400,1000)

    yield browser

    if request.node.rep_call.failed:
        browser.save_screenshot('screenshots/' + str(uuid.uuid4()) + '.png')

        print('URL:', browser.current_url)
        print('Browser logs:')
        for log in browser.get_log('browser'):
            print(log)

