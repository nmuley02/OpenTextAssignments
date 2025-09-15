from selenium.webdriver.common.by import By

class SignupPageLocators:
    # Page Locators
    email_locator = (By.XPATH, "//input[@id='personal-trial-email']")
    confirm_email_locator = (By.XPATH, "//input[@id='personal-trial-confirm-email']")
    passowrd_locator = (By.XPATH, "//input[@id='personal-trial-password']")
    confirm_password_locator = (By.XPATH, "//input[@id='personal-trial-confirm-password']")
    claim_free_trail_locator = (By.XPATH, "//p[@class='css-tp2wmw']")