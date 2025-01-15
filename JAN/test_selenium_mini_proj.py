import time
from time import sleep
from selenium import webdriver
import allure
import pytest


@allure.title("espocrm tittle verification")
@pytest.mark.regression
def test_espocrm():
    driver = webdriver.Edge()
    driver.get("https://demo.us.espocrm.com/")
    print(driver.title)
    time.sleep(5)
    assert "EspoCRM Demo" in driver.title



@allure.title("espocrm url verification")
@pytest.mark.regression
def test_current_url():
    driver1 = webdriver.Edge()
    driver1.get("https://demo.us.espocrm.com/")
    time.sleep(5)
    assert "https://demo.us.espocrm.com/" in driver1.current_url

