import time

from selenium.webdriver.remote.webdriver import WebDriver

from data.generator import GeneratorData
from data.urls.url_auth_person import AUTH_PERSON_ADD, AUTH_PERSON_APPLICATIONS, AUTH_PERSON
from locators.customer.auth_person_locators import INPUT_IIN, INPUT_NUMBER, CONTINUE_BUTTON, SIGN_BUTTON, SMS_CODE, \
    SUCCESSFUL_TEXT, CARD_BUTTON_WITH_SENT_INVITATION_STATUS, CANCEL_BUTTON, CONFIRM_CANCEL, \
    ALERT_TITLE, CARD_BUTTON_WITHOUT_BLOCKED, BLOCK_BUTTON, CONFIRM_BUTTON, CARD_BUTTON_WITH_BLOCKED, UNBLOCK_BUTTON
from locators.customer.login_locators import MAIN_TITLE
from pages.base_page.base_page import BasePage


class AuthorizedPersonPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        generator = GeneratorData()
        self.iin = generator.iin()
        self.phone_number = generator.phone_number()
        self.status_send_invitation = "Приглашение отправлено"
        self.status_temp_blocked = "Доступ временно закрыт"

    def open_auth_person_add_page(self):
        super()._get_text(locator=MAIN_TITLE)
        super()._open_url(url=AUTH_PERSON_ADD)


    def fill_form(self):
        super()._type(locator=INPUT_IIN, text=self.iin)
        super()._type(locator=INPUT_NUMBER, text=self.phone_number)
        self.click_on_continue()

    def click_on_continue(self):
        super()._wait_until_element_is_clickable(locator=CONTINUE_BUTTON,time= 30)
        super()._click(locator=CONTINUE_BUTTON)

    def click_on_sign(self):
        super()._wait_until_element_is_clickable(locator=SIGN_BUTTON,time=30)
        super()._click(SIGN_BUTTON)

    def enter_sms_code(self):
        inputs = super()._finds(locator=SMS_CODE)
        for input_element in inputs:
            input_element.send_keys("1")
        time.sleep(1)

    def get_successful_text(self):
        return super()._get_text(locator=SUCCESSFUL_TEXT, time=60)

    def open_applications(self):
        super()._get_text(locator=MAIN_TITLE)
        super()._open_url(url=AUTH_PERSON_APPLICATIONS)

    def open_card_with_sent_invitation_status(self):
        super()._find(locator=CARD_BUTTON_WITH_SENT_INVITATION_STATUS)
        super()._click(locator=CARD_BUTTON_WITH_SENT_INVITATION_STATUS)

    def delete_invitation(self):
        super()._wait_until_element_is_visible(locator=CANCEL_BUTTON)
        super()._click(locator=CANCEL_BUTTON)
        super()._wait_until_element_is_visible(locator=CONFIRM_CANCEL)
        super()._click(locator=CONFIRM_CANCEL)
        super()._wait_until_element_is_visible(ALERT_TITLE)
        return super()._get_text(ALERT_TITLE)

    def open_auth_person(self):
        super()._get_text(locator=MAIN_TITLE, time=30)
        super()._open_url(url=AUTH_PERSON)

    def open_auth_person_card(self, locator):
        super()._wait_until_element_is_visible(locator=locator)
        super()._click(locator=locator)

    def block(self):
        self.open_auth_person_card(CARD_BUTTON_WITHOUT_BLOCKED)
        super()._wait_until_element_is_visible(BLOCK_BUTTON)
        super()._click(BLOCK_BUTTON)
        super()._click(CONFIRM_BUTTON)
        self.enter_sms_code()
        super()._wait_until_element_is_visible(CONTINUE_BUTTON)
        super()._click(CONTINUE_BUTTON)
        super()._wait_until_element_is_visible(ALERT_TITLE)
        return super()._get_text(ALERT_TITLE)

    def unblock(self):
        self.open_auth_person_card(CARD_BUTTON_WITH_BLOCKED)
        super()._wait_until_element_is_visible(UNBLOCK_BUTTON)
        super()._click(UNBLOCK_BUTTON)
        super()._click(CONFIRM_BUTTON)
        self.enter_sms_code()
        super()._wait_until_element_is_visible(CONTINUE_BUTTON)
        super()._click(CONTINUE_BUTTON)
        super()._wait_until_element_is_visible(ALERT_TITLE)
        return super()._get_text(ALERT_TITLE)