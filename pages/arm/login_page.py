import time

from data.urls.url_arm_login import LOGIN
from locators.arm.login_locators import USER_NAME, PASSWORD, BUTTON, MAIN_TITLE
from pages.base_page.base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver

class LoginPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(LOGIN)

    def execute(self, username: str, password: str):
        super()._type(USER_NAME, username,30)
        super()._type(PASSWORD, password,30)
        time.sleep(5)
        super()._click(BUTTON, 30)

    def get_title(self):
        return super()._get_text(MAIN_TITLE,time=30)