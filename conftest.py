import pytest
from selenium import webdriver
#from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.firefox.options import Options
from data import *

@pytest.fixture()
def driver():
    options = Options()
    options.add_argument ("--window-size=1200,600")
    browser = webdriver.Firefox(options=options)
    browser.get(main_site)
    yield browser
    browser.quit()

