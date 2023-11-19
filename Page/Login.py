from Locators import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


def wait_until_element_has_an_attribute(self, element_selector, element_locator):
    wait = WebDriverWait(self.driver, 20)
    element = wait.until(EC.element_to_be_clickable((element_selector, element_locator)))
    sleep(0.5)
    element.click()
    sleep(0.5)


def wait_until_element_has_an_attribute_and_send_keys(self, element_selector, element_locator, text):
    wait = WebDriverWait(self.driver, 20)
    element = wait.until(EC.element_to_be_clickable((element_selector, element_locator)))
    sleep(0.5)
    element.clear()
    sleep(0.5)
    element.send_keys(text)
    sleep(0.5)


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_phone(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', phone, text)

    def enter_check_phone_number_btn(self):
        wait_until_element_has_an_attribute(self, 'xpath', check_phone_number_btn)

    def enter_password_input(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', password_input, text)

    def enter_password_submit(self):
        wait_until_element_has_an_attribute(self, 'xpath', password_submit)

    def enter_assert_phone(self):
        assert 'نام کاربری نامعتبر' or 'تعداد درخواست های شما بیشتر از حد مجاز' in self.driver.find_element('xpath', assert_phone).get_attribute("innerHTML")

    def enter_assert_password(self):
        wait_until_element_has_an_attribute(self, 'xpath', assert_password)
        assert 'نام کاربری یا رمز عبور اشتباه' in self.driver.find_element('xpath', assert_password).get_attribute("innerHTML")

    def enter_assert_login(self):
        self.driver.refresh()
        sleep(2)
        assert '09379161533' in self.driver.find_element('xpath', assert_login).get_attribute("innerHTML")




