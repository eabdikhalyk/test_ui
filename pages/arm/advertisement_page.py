import os
import time

from selenium.webdriver.remote.webdriver import WebDriver
from locators.arm.popup_locators import ADVERTISING_TAB, POPUP_TAB, CREATE_BUTTON, CODE_OF_PRODUCT, \
    TEXT_CODE_OF_PRODUCT, NAME_OF_POPUP, TEXT_NAME_OF_POPUP, ORDER, TEXT_ORDER, DROPDOWN_LIST, MOBILE, \
    POPUP_FILE_KZ, UPLOAD_FILE_KZ_INPUT
from pages.base_page.base_page import BasePage


class AdvertisementPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open_popup(self):
        super()._click(ADVERTISING_TAB)
        super()._click(POPUP_TAB)

    def add_popup(self):
        super()._click(CREATE_BUTTON)

    def fill_form(self):
        super()._type(CODE_OF_PRODUCT,TEXT_CODE_OF_PRODUCT)
        super()._type(NAME_OF_POPUP,TEXT_NAME_OF_POPUP)
        super()._type(ORDER,TEXT_ORDER)

        DROPDOWN_LISTS = super()._finds(DROPDOWN_LIST)
        CHANNEL = DROPDOWN_LISTS[0]
        CHANNEL.click()
        super()._click(MOBILE)
        time.sleep(2)
        super()._type(UPLOAD_FILE_KZ_INPUT, POPUP_FILE_KZ)





