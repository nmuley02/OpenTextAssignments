from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
from OpenTextTask1.Config import Config
from OpenTextTask1.Pages.SignupPage import SignupPage
from selenium.webdriver.chrome.service import Service

# This is a simple test case for the web automation part.
def test_signup_download():
    service = Service("C:/Users/aniru/Desktop/neha/Assignments/PythonProject/chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(20)
    driver.maximize_window()
    driver.get(Config.default_url)
    assert "Carbonite" in driver.title

    signup_page = SignupPage(driver)

    signup_page.fill_form(Config.username, Config.confirm_email, Config.password, Config.confirm_password)

    ##The test is not completely working as I couldnt capture or automate captcha as its nit an ideal way of automation
    ##The workaround could be mock API, disabling captcha in test/de env
    signup_page.click_freeTrial()

    print("Testing signup download complete... ")

test_signup_download()
