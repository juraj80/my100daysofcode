from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import os

user = os.environ.get('PACKT_USER')
pw = os.environ.get('PACKT_PW')

print(user)
print(pw)
login = 'https://www.packtpub.com/login'

driver = webdriver.Chrome()
driver.get(login)

driver.find_element_by_id('edit-name').send_keys(user)
driver.find_element_by_id('edit-pass').send_keys(pw + Keys.RETURN)

driver.find_element_by_link_text('My eBooks').click()

elements = driver.find_elements_by_class_name("product-line")
books = {e.get_attribute('nid'): e.get_attribute('title') for e in elements}
print(books)

driver.close()

