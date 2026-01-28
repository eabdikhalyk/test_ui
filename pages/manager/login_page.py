from selenium.webdriver.remote.webdriver import WebDriver

from data.urls.url_manager_login import LOGIN
from locators.manager.login_locators import USER_NAME, PASSWORD, BUTTON
from pages.base_page.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(url=LOGIN)

    def execute(self, username, password):
        super()._type(locator=USER_NAME, text=username,time=60)
        super()._type(locator=PASSWORD, text=password,time=60)
        super()._click(locator=BUTTON,time=60)