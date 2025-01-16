from selenium import webdriver
import allure
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#from dotenv import load_dotenv
#import os


@allure.title("escp Login positive Testcase")
@allure.description("TC1 - positive TC - escp.")
@pytest.mark.elements_check
def test_app_vwo_login_chrome():
    driver = webdriver.Chrome()
    driver.get("https://demo.us.espocrm.com/")
    time.sleep(10)
    #https: // www.espocrm.com / extensions / advanced - pack /
    find_elements_esp = driver.find_element(By.LINK_TEXT,"Advanced Pack")
    find_elements_esp.click()
    time.sleep(5)
    assert driver.current_url == "https://www.espocrm.com/extensions/advanced-pack/"

