__author__ = 'MENGMENG'

from selenium import webdriver
import page
import os
from selenium.common.exceptions import NoSuchElementException
from setting import configuration

def bemossCheck():

    """
    Tests python.org search feature. Searches for the word "kw" then verified that some results show up.
    Note that it does not look for any particular text in search results page. This test verifies that
    the results were not empty.
    """

    chrome_driver = os.path.abspath\
        (r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
    os.environ["webdriver.chrome.driver"] = chrome_driver

    driver = webdriver.Chrome(chrome_driver)
    driver.get(configuration.IPadress)

    #Load the main page. In this case the home page of Python.org.
    main_page = page.MainPage(driver)
    #Checks if the word "BEMOSS" is in title
    assert main_page.is_title_matches(), "Title doesn't match."
    #Log in the bemoss by admin authority
    main_page.input_login_message()
    main_page.click_go_button()
    now_handle = driver.current_window_handle

    driver.switch_to.window(now_handle)

    try:
        print driver.find_element_by_Xpath('/div[id="side-nav"]/ul/li[8]/a')
    except:
        NoSuchElementException

    #search_results_page = page.SearchResultsPage(driver)
    #Verifies that the results page is not empty
    #assert search_results_page.is_results_found(), "No results found."
    driver.close()


if __name__ == "__main__":
    bemossCheck()