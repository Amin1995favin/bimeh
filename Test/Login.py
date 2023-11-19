import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from time import sleep
from Locators import *
from Page.Login import LoginPage


service = Service()
options = webdriver.ChromeOptions()
# options.add_argument("--headless")
driver = webdriver.Chrome(service=service, options=options)


class Test_Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

###Loginssfsdfdsdsdaszsaa

    def test01_should_get_error_if_mobile_not_send(self):
        self.driver.get("https://bimeh.com/auth/login")
        login = LoginPage(driver=self.driver)
        login.enter_phone(" ")
        login.enter_check_phone_number_btn()
        login.enter_assert_phone()
        print("باید شماره وارد شود.")

    def test02_should_get_error_if_mobile_is_wrong(self):
        self.driver.get(url_login)
        login = LoginPage(driver=self.driver)
        login.enter_phone("0 9 3 7 9 1 6 1 5 3 3 ")
        login.enter_check_phone_number_btn()
        login.enter_assert_phone()
        print("با زدن شماره اشتباه و کد صحیح وارد نمی شود.")

    def test03_should_get_error_if_mobile_is_wrong(self):
        self.driver.get(url_login)
        login = LoginPage(driver=self.driver)
        login.enter_phone("0937916153A")
        login.enter_check_phone_number_btn()
        login.enter_assert_phone()
        print("با زدن شماره اشتباه و کد صحیح وارد نمی شود.")

    def test04_should_get_error_if_password_not_send(self):
        self.driver.get(url_login)
        login = LoginPage(driver=self.driver)
        login.enter_phone(mobile)
        login.enter_check_phone_number_btn()
        login.enter_password_input(" ")
        login.enter_password_submit()
        login.enter_assert_password()
        print("با زدن شماره اشتباه و کد صحیح وارد نمی شود.")

    def test05_should_get_error_if_password_is_wrong(self):
        self.driver.get(url_login)
        login = LoginPage(driver=self.driver)
        login.enter_phone(mobile)
        login.enter_check_phone_number_btn()
        login.enter_password_input("43126")
        login.enter_password_submit()
        login.enter_assert_password()
        print("با زدن شماره اشتباه و کد صحیح وارد نمی شود.")

    def test06_should_get_ok(self):
        self.driver.get(url_login)
        login = LoginPage(driver=self.driver)
        login.enter_phone(mobile)
        login.enter_check_phone_number_btn()
        login.enter_password_input(password)
        login.enter_password_submit()
        login.enter_assert_login()
        print("با زدن شماره اشتباه و کد صحیح وارد نمی شود.")



    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
