import time
from time import sleep

from selenium import webdriver
import allure
import pytest


@allure.title("vwo")
@pytest.mark.regression
def test_web_dri():
    driver = webdriver.Chrome()
    driver.get("http:/app.vwo.com")
    print(driver.title)
    #time.sleep(2)


