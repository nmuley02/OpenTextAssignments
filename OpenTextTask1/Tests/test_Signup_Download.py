from logging import exception

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
from OpenTextTask1.Config import Config
from OpenTextTask1.Pages.SignupPage import SignupPage
from OpenTextTask1.Pages.SignupPage_Locators import SignupPageLocators
from selenium.webdriver.chrome.service import Service

# This is a simple test case for the web automation part.
def test_signup_download():
    #Need to add a generic pth for the chromedriver exe here
    service = Service("C:/Users/aniru/Desktop/neha/Assignments/PythonProject/chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    #Add wait for the page to load
    driver.implicitly_wait(20)

    # Maximise the Page Window
    driver.maximize_window()

    #Enter the website URL
    driver.get(Config.default_url)
    assert "Carbonite" in driver.title
    #Creating Object of the Signup Page Class
    signup_page = SignupPage(driver)

    #Accepting cookies on the web page launch
    signup_page.accept_cookies()
    driver.implicitly_wait(10)

    #Filling out the form for the Free Claim Trail Signup Page
    signup_page.fill_form(Config.username, Config.confirm_email, Config.password, Config.confirm_password)

    ##The test is not completely working as I couldnt capture or automate captcha as its nit an ideal way of automation
    ##The workaround could be mock API, disabling captcha in test/dev env
    try:
        # Attempt to click the submit button
        signup_page.click_freeTrial()

        # Wait for an element on the success page to appear
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "success-message"))
        )
    except TimeoutException:
        # If the wait times out, it means the page did not change, likely due to the CAPTCHA
        pytest.fail("Test failed: Page did not load after form submission, likely due to CAPTCHA.")

    print("Testing signup download complete... ")

