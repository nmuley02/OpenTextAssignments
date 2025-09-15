from selenium.webdriver.common.by import By

class SignupPageLocators:
    # Page Locators
    accept_cookies_locator = (By.ID, "onetrust-accept-btn-handler")
    email_locator = (By.XPATH, "//input[@id='personal-trial-email']")
    confirm_email_locator = (By.XPATH, "//input[@id='personal-trial-confirm-email']")
    passowrd_locator = (By.XPATH, "//input[@id='personal-trial-password']")
    confirm_password_locator = (By.XPATH, "//input[@id='personal-trial-confirm-password']")
    country_locator = (By.XPATH, "//button[@aria-label='form select button']")
    claim_free_trail_locator = (By.XPATH, "//p[@class='css-tp2wmw']")