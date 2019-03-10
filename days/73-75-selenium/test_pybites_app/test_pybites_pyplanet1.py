from selenium import webdriver
import pytest

URL = "http://pyplanet.herokuapp.com/"
LINK_TEXT = "Codementor: PySpark Programming"
PAGE_TITLE = "PyBites 100 Days of Django"
APP_NAME = 'PyPlanet Article Sharer App'
USERNAME, PASSWORD = 'guest', 'changeme'


@pytest.fixture(scope='module')
def test_setup():
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    driver.close()
    driver.quit()
    print("Test completed.")


def test_header(test_setup):
    """
    Go to the http://pyplanet.herokuapp.com/. The header should say PyBites 100 Days of Django.
    """
    driver.get(URL)
    heading = driver.find_element_by_tag_name('h1').text
    assert heading == PAGE_TITLE


def test_navbar(test_setup):
    """
    The navbar has Login and
    Home links. The first link in the main div is PyPlanet Article Sharer App.
    """
    driver.find_element_by_link_text('Login')
    driver.find_element_by_link_text('Home')


def test_hyperlink(test_setup):
    """
    Click on the PyPlanet Article Sharer App link.
    """
    driver.find_element_by_link_text(APP_NAME).click()


def test_table(test_setup):
    """
    Test the page contains a table with a th (table header) containing
    the word Title. This app watches the PyPlanet feed so the titles change every day so that is hard test. What we can
    test though is if the table contains 100 entries (tr).
    """
    driver.find_element_by_class_name('pure-table')
    heading = driver.find_element_by_tag_name('th').text
    assert heading == "Title"
    elements = driver.find_elements_by_xpath('//tbody/tr')
    assert len(elements) == 100


def test_header_link(test_setup):
    """
    Go to an article and check there is only a Go back button (logged out view). Check if the header link at the top is
    the same as the link you clicked on. The Go back should redirect back to the app's home page.
    """
    home_page = driver.current_url
    driver.find_element_by_link_text(LINK_TEXT).click()
    heading = driver.find_element_by_tag_name('h2').text
    assert heading == LINK_TEXT

    buttons = driver.find_elements_by_link_text('Go back')
    assert len(buttons) == 1

    buttons[0].click()
    assert home_page == driver.current_url


def test_login(test_setup):
    """
    Using Selenium click Login and login with user: guest / password: changeme - then click the blue Login button
    """
    driver.find_element_by_xpath('//a[@href="/login/"]').click()
    driver.find_element_by_name('username').send_keys(USERNAME)
    driver.find_element_by_name('password').send_keys(PASSWORD)
    driver.find_element_by_tag_name('button').click()


def test_redirect(test_setup):
    """
    Check you are redirected back to 100Days home and if navigation contains Welcome back, guest! and Logout and Home links.
    """
    assert URL == driver.current_url
    login_text = driver.find_element_by_id('login').text
    assert login_text == 'Welcome back, guest! Logout  | Home'


def test_tweet_button(test_setup):
    """
    Going back to the article link (3.), check that you now have a Tweet this button alongside the Go back button. Optionally
    you can check the link of the Tweet this button (extra check: PyBites entries have New PyBites Article prepended).
    """
    driver.find_element_by_link_text('PyPlanet Article Sharer App').click()
    driver.find_element_by_link_text(LINK_TEXT).click()
    driver.find_element_by_link_text('Tweet this')


def test_logout(test_setup):
    """
    Finally logout with Selenium and check for See you! and You have been successfully logged out., logout in the URL,
    and navbar links are Login and Home again
    """
    driver.find_element_by_link_text('Logout').click()
    assert 'logout' in driver.current_url
    assert 'See you!' == driver.find_element_by_tag_name('h1').text
    assert 'You have been successfully logged out.' == driver.find_element_by_tag_name('p').text



