import time
from selenium import webdriver
from Pages.loginPage import Login

def test_valid_login(setup):
    driver = setup
    lp = Login(driver)
    lp.setuser("Admin")
    lp.setpswrd("admin123")
    time.sleep(2)
    lp.clickLogin()
    time.sleep(5)
    assert "dashboard" in driver.current_url.lower()  # Simple check
