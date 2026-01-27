import time

from data.generator import GeneratorData
from data.urls.url_personal import PERSONAL_PAGE_DETAILS
from locators.login_locators import MAIN_TITLE
from locators.personal_details_locators import EDIT_BUTTON, CONTINUE_BUTTON, INPUT_NUMBER, CHECKBOX, \
    DIALOG_CONTINUE_BUTTON, SMS_CODE, ALERT_TITLE
from pages.base_page.base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver



class PersonalPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.generator = GeneratorData()

    def open_personal_details(self):
        super()._get_text(locator=MAIN_TITLE, time=30)
        super()._open_url(url=PERSONAL_PAGE_DETAILS)

    def click_on_edit(self):
        super()._click(locator=EDIT_BUTTON, time=60)

    def enter_number(self):
        super()._type(INPUT_NUMBER,self.generator.phone_number())

    def click_on_button(self):
        super()._click(CONTINUE_BUTTON)

    def checked_confirmation_doc(self):
        super()._click(CHECKBOX,15)

    def click_on_dialog_button(self):
        super()._click(DIALOG_CONTINUE_BUTTON)

    def enter_sms_code(self):
        super()._wait_until_element_is_visible(SMS_CODE,180)
        inputs = super()._finds(SMS_CODE)
        for input_element in inputs:
            input_element.send_keys("1")
        time.sleep(1)

    def get_successful_text(self):
        return super()._get_text(ALERT_TITLE, 60)