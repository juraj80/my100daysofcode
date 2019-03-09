from selenium import webdriver
from selenium.webdriver.common.keys import Keys

URL = "http://pyplanet.herokuapp.com/"
LINK_TEXT = "Codementor: PySpark Programming"


def test_setup():
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()

def test_header():
    driver.get(URL)

    heading = driver.find_element_by_tag_name('h1').text
    assert heading == "PyBites 100 Days of Django"

def test_navbar():
    driver.find_element_by_link_text('Login')
    driver.find_element_by_link_text('Home')

def test_hyperlink():
    driver.find_element_by_link_text('PyPlanet Article Sharer App').click()

def test_table():
    driver.find_element_by_class_name('pure-table')
    heading = driver.find_element_by_tag_name('th').text
    assert heading == "Title"
    elements = driver.find_elements_by_xpath('//tbody/tr')
    assert len(elements) == 100


def test_header_link():
    # url = "/pyplanet/2393/"
    # driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    home_page = driver.current_url
    driver.find_element_by_link_text(LINK_TEXT).click()
    heading = driver.find_element_by_tag_name('h2').text
    assert heading == LINK_TEXT

    buttons = driver.find_elements_by_link_text('Go back')
    assert len(buttons) == 1

    buttons[0].click()
    assert home_page == driver.current_url

def test_login():
    driver.find_element_by_xpath('//a[@href="/login/"]').click()
    driver.find_element_by_name('username').send_keys('guest')
    driver.find_element_by_name('password').send_keys('changeme')
    driver.find_element_by_tag_name('button').click()

def test_redirect():
    assert URL == driver.current_url
    login_text = driver.find_element_by_id('login').text
    assert login_text == 'Welcome back, guest! Logout  | Home'

def test_tweet_button():
    driver.find_element_by_link_text('PyPlanet Article Sharer App').click()
    driver.find_element_by_link_text(LINK_TEXT).click()
    driver.find_element_by_link_text('Tweet this')

def test_logout():
    driver.find_element_by_link_text('Logout').click()
    assert 'logout' in driver.current_url
    # driver.find_element_by_link_text('See you!')
    # driver.find_element_by_link_text('You have been successfully logged out.')
    # driver.find_element_by_partial_link_text('You have been')
    assert 'See you!' == driver.find_element_by_tag_name('h1').text
    assert 'You have been successfully logged out.' == driver.find_element_by_tag_name('p').text





# def test_teardown():
#     driver.close()
#     driver.quit()
#     print("Test completed.")