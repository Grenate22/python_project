from selenium import webdriver
from selenium.webdriver.common.keys import keys
browser=webdriver.Firefox(executable_path='')
print(type(browser))
browser.get('https://inventwithpython.com')
linkelem=browser.find_element('Read It Online')
print(type(linkelem))
linkelem.click()