import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from OpenTextTask1.Config import Config
from OpenTextTask1.Config.Config import username, password, default_url
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from OpenTextTask1.Pages.SignupPage_Locators import SignupPageLocators



# This is a Page Object for a Free Trial sign-up form.
# It encapsulates all the web elements and methods related to this page.
# It's a key part of the Page Object Model (POM) pattern.

class SignupPage:
    def __init__(self, driver):
        # The constructor receives the WebDriver instance from the test.
        self.driver = driver


    def fill_form(self, email_address, confirm_email, password, confirm_password):
        self.driver.find_element(*SignupPageLocators.email_locator).send_keys(username)
        self.driver.find_element(*SignupPageLocators.confirm_email_locator).send_keys(username)
        self.driver.find_element(*SignupPageLocators.passowrd_locator).send_keys(password)
        self.driver.find_element(*SignupPageLocators.confirm_password_locator).send_keys(password)

    def click_freeTrial(self):
        element = self.driver.find_element(*SignupPageLocators.claim_free_trail_locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()





