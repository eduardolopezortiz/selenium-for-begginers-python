import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


#class TestPositiveScenarios
class TestPositiveScenarios:

    @pytest.mark.login
    def test_positive_login(self):
        # Test case 1: Positive LogIn test

        # Open browser
        driver = webdriver.Chrome()
        time.sleep(2)

        # Go to webpage
        driver.get("https://practicetestautomation.com/practice-test-login/")
        # Max the browser windows
        driver.maximize_window()
        time.sleep(5)

        # Type username student into Username field
        username_locator = driver.find_element(By.XPATH, "/html//input[@id='username']")
        username_locator.send_keys("student")
        time.sleep(2)

        # Type password Password123 into Password field
        password_locator = driver.find_element(By.XPATH, "/html//input[@id='password']")
        password_locator.send_keys("Password123")
        time.sleep(2)

        # Push Submit button
        submit_button_locator = driver.find_element(By.XPATH, "/html//button[@id='submit']")
        submit_button_locator.click()
        time.sleep(2)

        # Verify new page URL contains practicetestautomation.com/logged-in-successfully/
        actual_url = driver.current_url
        assert actual_url == "https://practicetestautomation.com/logged-in-successfully/"

        # Verify new page contains expected text ('Congratulations' or 'successfully logged in')
        text_locator = driver.find_element(By.TAG_NAME, "h1")
        actual_text = text_locator.text
        assert actual_text == "Logged In Successfully"

        # Verify button Log out is displayed on the new page
        log_out_button_locator = driver.find_element(By.LINK_TEXT, "Log out")
        assert log_out_button_locator.is_displayed()




