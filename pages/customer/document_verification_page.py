from data.urls.url_doc_verifcation import DOC_VERIFICATION
from locators.customer.doc_verification_locators import INPUT_ID, BUTTON, RESULT
from pages.base_page.base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver


class DocumentVerification(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(url=DOC_VERIFICATION)

    def verification(self,DOC_ID):
        super()._type(locator=INPUT_ID,text=DOC_ID)
        super()._click(locator=BUTTON)

    def get_result(self):
        return super()._get_text(locator=RESULT)