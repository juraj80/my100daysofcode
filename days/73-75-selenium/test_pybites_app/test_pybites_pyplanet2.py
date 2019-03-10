import re

import pytest
from selenium import webdriver


BASE_URL = 'http://pyplanet.herokuapp.com/'
PAGE_TITLE = 'PyBites 100 Days of Django'
APP_URL = 'http://pyplanet.herokuapp.com/pyplanet/'
APP_NAME = 'PyPlanet Article Sharer App'
USERNAME, PASSWORD = 'guest', 'changeme'
TABLE_CLASS = 'pure-table'


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.close()


def get_first_article_title(driver):
    table = driver.find_element_by_xpath(f'//table[@class="{TABLE_CLASS}"]')
    return table.find_elements_by_xpath(".//td")[0].text


def test_login_logout_process_and_views(driver):
    driver.get(APP_URL)

    assert '<a href="/">Home</a>' in driver.page_source
    assert '<a href="/login/">Login</a>' in driver.page_source
    assert '<a href="/logout/">Logout</a>' not in driver.page_source

    driver.find_element_by_link_text('Login').click()
    username_field = driver.find_element_by_name('username')
    username_field.send_keys(USERNAME)
    password_field = driver.find_element_by_name('password')
    password_field.send_keys(PASSWORD)

    btn_xpath = "//button[contains(@class, 'pure-button-primary')]"
    login_btn = driver.find_element_by_xpath(btn_xpath)
    login_btn.click()

    driver.get(APP_URL)

    assert '<a href="/login/">Login</a>' not in driver.page_source
    assert 'Welcome back, guest' in driver.page_source
    assert '<a href="/logout/">Logout</a>' in driver.page_source

    first_article = get_first_article_title(driver)
    driver.find_element_by_link_text(first_article).click()

    assert 'Go back' in driver.page_source

