from data.urls.url_auth_person import LOGIN
from locators.customer.login_locators import USER_NAME, PASSWORD, BUTTON, MAIN_TITLE
from pages.base_page.base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver

class LoginPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(LOGIN)

    def execute(self, username: str, password: str):
        super()._type(USER_NAME, username)
        super()._type(PASSWORD, password)
        super()._click(BUTTON)

    def get_title(self):
        return super()._get_text(MAIN_TITLE,time=30)
