__author__ = 'MENGMENG'

from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    GO_BUTTON = (By.XPATH, '/html/body/div[2]/div/div/form/div[2]/div/button')

class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should come here"""
    pass