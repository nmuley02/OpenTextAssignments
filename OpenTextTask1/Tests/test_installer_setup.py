import time
import pytest
from pywinauto.application import Application

# This file demonstrates how to use Pywinauto to automate a desktop installer.
# This is a separate concern from web automation but can be a part of the same test flow.
# Example: After clicking 'Download', you need to handle the installer pop-up.

def test_Installer_setup():
    # Start and connect to the installer application.
    app = Application(backend='uia').start("C:\\Users\\aniru\\Desktop\\neha\\Assignments\\PythonProject\\Carbonite-personal-client.exe")
    app = Application(backend='uia').connect(title='Installing Carbonite', timeout=100)

    # get control identifier handles for the elements on the GUI
    app.InstallingCarbonite.print_control_identifiers()

    #Click on the term and conditions checkbox
    Terms_CheckBox= app.InstallingCarbonite.child_window(title="I agree to Carbonite's Terms of Service and acknowledge Carbonite's Privacy Policy", auto_id="crbSetupCheckbox", control_type="CheckBox").wrapper_object()
    Terms_CheckBox.click_input()

    # Click the 'Next' button to proceed.
    Continue_Installation = app.InstallingCarbonite.child_window(title="Continue", auto_id="crbSetupButton1", control_type="Hyperlink").wrapper_object()
    Continue_Installation.click_input()

    print("Installer setup complete")

test_Installer_setup()