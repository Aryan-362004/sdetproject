# pages/login_pg.py

from selenium.webdriver.common.by import By

class Login:
    txt_name = "username"
    txt_pswrd = "password"
    btn_xpth = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'

    def __init__(self, driver):
        self.driver = driver

    def setuser(self, username):
        self.driver.find_element(By.NAME, self.txt_name).send_keys(username)

    def setpswrd(self, password):
        self.driver.find_element(By.NAME, self.txt_pswrd).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.btn_xpth).click()
