import os
import time

from selenium.webdriver.remote.webdriver import WebDriver
from locators.arm.popup_locators import ADVERTISING_TAB, POPUP_TAB, CREATE_BUTTON, CODE_OF_PRODUCT, \
    TEXT_CODE_OF_PRODUCT, NAME_OF_POPUP, TEXT_NAME_OF_POPUP, ORDER, TEXT_ORDER, DROPDOWN_LIST, MOBILE, \
    POPUP_FILE_KZ, POPUP_FILE_RU, POPUP_FILE_EN, UPLOAD_FILE_KZ_INPUT, UPLOAD_FILE_RU_INPUT, UPLOAD_FILE_EN_INPUT, \
    STYLE_OF_BLUE, DEEP_LINK, DEEP_LINK_INPUT, BUTTONS, BUTTON_KZ_INPUT_1, BUTTON_EN_INPUT_1, BUTTON_RU_INPUT_1, \
    STYLE_OF_LIGHT_BLUE, LINKS_INPUT, LINK, BUTTON_KZ_INPUT_2, BUTTON_EN_INPUT_2, BUTTON_RU_INPUT_2, BUTTON_SAVE
from locators.customer.doc_verification_locators import RESULT
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
        STYLE_OF_BUTTON_1 = DROPDOWN_LISTS[1]
        STYLE_OF_BUTTON_2 = DROPDOWN_LISTS[2]
        CHANNEL.click()
        super()._click(MOBILE)
        super()._attach_file(UPLOAD_FILE_KZ_INPUT, POPUP_FILE_KZ)
        super()._attach_file(UPLOAD_FILE_RU_INPUT, POPUP_FILE_RU)
        super()._attach_file(UPLOAD_FILE_EN_INPUT, POPUP_FILE_EN)
        STYLE_OF_BUTTON_1.click()
        super()._click(STYLE_OF_BLUE)
        DEEP_LINK_INPUTS = super()._finds(DEEP_LINK_INPUT)
        DEEP_LINK_INPUTS[0].send_keys(DEEP_LINK)
        NAME_OF_BUTTONS = super()._finds(BUTTONS)
        BUTTON_KZ_FOR_DEEP_LINK = NAME_OF_BUTTONS[0]
        BUTTON_KZ_FOR_DEEP_LINK.send_keys(BUTTON_KZ_INPUT_1)
        BUTTON_EN_FOR_DEEP_LINK = NAME_OF_BUTTONS[1]
        BUTTON_EN_FOR_DEEP_LINK.send_keys(BUTTON_EN_INPUT_1)
        BUTTON_RU_FOR_DEEP_LINK = NAME_OF_BUTTONS[2]
        BUTTON_RU_FOR_DEEP_LINK.send_keys(BUTTON_RU_INPUT_1)
        LINKS = super()._finds(LINKS_INPUT)
        LINKS[1].send_keys(LINK)
        STYLE_OF_BUTTON_2.click()
        super()._click(STYLE_OF_LIGHT_BLUE)
        BUTTON_KZ_FOR_LINK = NAME_OF_BUTTONS[3]
        BUTTON_KZ_FOR_LINK.send_keys(BUTTON_KZ_INPUT_2)
        BUTTON_EN_FOR_LINK = NAME_OF_BUTTONS[4]
        BUTTON_EN_FOR_LINK.send_keys(BUTTON_EN_INPUT_2)
        BUTTON_RU_FOR_LINK = NAME_OF_BUTTONS[5]
        BUTTON_RU_FOR_LINK.send_keys(BUTTON_RU_INPUT_2)

    def save(self):
        super()._click(BUTTON_SAVE)

    def get_result(self):
        return super()._get_text(RESULT)






