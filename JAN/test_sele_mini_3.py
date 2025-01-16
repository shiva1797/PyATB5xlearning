from selenium import webdriver
import allure
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#from dotenv import load_dotenv
import os


@allure.title("VWO Login Negative Testcase")
@allure.description("TC1 - Negative TC - VWO Login with invalid creds.")
@pytest.mark.negativevwologin
def test_app_vwo_login_chrome():
    #load_dotenv()
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://demo.us.espocrm.com/")
    time.sleep(10)

    # <a
    # href="https://vwo.com/free-trial/?utm_medium=website&amp;utm_source=login-page&amp;utm_campaign=mof_eg_loginpage"
    # class="text-link"
    # data-qa="bericafeqo">
    # Start a free trial
    # </a>

    # LinkText and Partial Text


    # LINK_TEXT = EXACT Match
    # anchor_tag_element = driver.find_element(By.LINK_TEXT,"Start a free trial")
    # anchor_tag_element.click()


    # PARTIAL_LINK_TEXT - contains
    anchor_tag_element = driver.find_element(By.PARTIAL_LINK_TEXT, "Advanced Pack")
    anchor_tag_element.click()
    time.sleep(5)
    assert driver.current_url == "https://www.espocrm.com/extensions/advanced-pack/"
   
    #driver.quit()  # close everything.