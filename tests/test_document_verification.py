from locators.customer.doc_verification_locators import VALID_DOC_ID, INVALID_DOC_ID
from pages.customer.document_verification_page import DocumentVerification


class TestDocumentVerification:
    def test_valid_document_id(self,driver):
        document = DocumentVerification(driver)
        document.open()
        document.verification(VALID_DOC_ID)
        successful_text = document.get_result()
        assert successful_text == "Документ найден"

    def test_invalid_document_id(self,driver):
        document = DocumentVerification(driver)
        document.open()
        document.verification(INVALID_DOC_ID)
        successful_text = document.get_result()
        assert successful_text == "Документ не найден"
