import time

from data.urls.url_manager_login import HYUNDAI_AUTH_PERSON
from locators.manager.main_page_locators import CONTEXT_MENU, BUTTON_INI_DIGITAL, MAIN_TITLE, BUTTON_MANAGEMENT, \
    BUTTON_ORGANIZATION, BUTTON_SEARCH, INPUT_TEXT, COMPANY_NAME, BUTTON_AUTH_PERSON
from pages.base_page.base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver


class MainPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(url=HYUNDAI_AUTH_PERSON)


    def open_company_auth_person(self):
        super()._get_text(locator=MAIN_TITLE)
        super()._click(locator=BUTTON_MANAGEMENT, time=30)
        super()._click(locator=BUTTON_ORGANIZATION)
        super()._click(locator=BUTTON_SEARCH)
        super()._type(locator=INPUT_TEXT,text=COMPANY_NAME,time=20)
        super()._click(locator=BUTTON_AUTH_PERSON)

    def click_on_context_menu_auth_person(self):
        super()._wait_until_element_is_visible(locator=CONTEXT_MENU,time=30)
        super()._click(locator=CONTEXT_MENU)

    def click_on_init_digital_signature(self):
        super()._wait_until_element_is_visible(locator=BUTTON_INI_DIGITAL,time=30)
        super()._click(locator=BUTTON_INI_DIGITAL)