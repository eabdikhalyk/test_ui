from data.login_with_user import login_with_user
from pages.customer.personal_page import PersonalPage


class TestChangeNumber:
    def test_change_number(self, driver):
        login_with_user(driver,"FIRST_DIRECTOR_USERNAME","FIRST_DIRECTOR_PASSWORD")
        personal_page = PersonalPage(driver)
        personal_page.open_personal_details()
        personal_page.click_on_edit()
        personal_page.enter_number()
        personal_page.click_on_button()
        personal_page.checked_confirmation_doc()
        personal_page.click_on_dialog_button()
        personal_page.enter_sms_code()
        personal_page.click_on_button()
        successful_title = personal_page.get_successful_text()
        assert successful_title == "Номер изменён"