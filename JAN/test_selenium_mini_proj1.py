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
@pytest.mark.negativevwologin
def test_app_vwo_login_chrome():
    driver = webdriver.Chrome()
    driver.get("https://demo.us.espocrm.com/")
    time.sleep(10)
    esp_element =driver.find_element(By.ID,"btn-login")
    esp_element.click()
    assert driver.current_url == "https://demo.us.espocrm.com/?l=en_US"
 #<button type="submit" class="btn btn-primary btn-s-wide" id="btn-login">Login</button>
    time.sleep(10)
    assert driver.current_url == "https://demo.us.espocrm.com/?l=en_US"
    #driver.quit()  # close everything.