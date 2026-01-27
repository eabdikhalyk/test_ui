import pytest
from data.login_with_user import login_with_user
from pages.customer.authorized_persons_page import AuthorizedPersonPage


class TestAuthorizedPerson:
    @pytest.mark.order(1)
    def test_send_invitation(self,driver):
        login_with_user(driver,"FIRST_DIRECTOR_USERNAME","FIRST_DIRECTOR_PASSWORD")
        auth_person_page = AuthorizedPersonPage(driver)
        auth_person_page.open_auth_person_add_page()
        auth_person_page.fill_form()
        auth_person_page.click_on_sign()
        auth_person_page.enter_sms_code()
        auth_person_page.click_on_continue()
        successful_text = auth_person_page.get_successful_text()
        assert successful_text is not None

    @pytest.mark.order(2)
    def test_delete_invitation(self, driver):
        login_with_user(driver, "FIRST_DIRECTOR_USERNAME", "FIRST_DIRECTOR_PASSWORD")
        auth_person_page = AuthorizedPersonPage(driver)
        auth_person_page.open_applications()
        auth_person_page.open_card_with_sent_invitation_status()
        successful_title = auth_person_page.delete_invitation()
        assert successful_title == "Заявка отменена"

    @pytest.mark.order(3)
    def test_block_auth_person(self, driver):
        login_with_user(driver, "FIRST_DIRECTOR_USERNAME", "FIRST_DIRECTOR_PASSWORD")
        auth_person_page = AuthorizedPersonPage(driver)
        auth_person_page.open_auth_person()
        successful_title = auth_person_page.block()
        assert successful_title == "Вы закрыли доступ"

    @pytest.mark.order(4)
    def test_unblock_auth_person(self, driver):
        login_with_user(driver, "FIRST_DIRECTOR_USERNAME", "FIRST_DIRECTOR_PASSWORD")
        auth_person_page = AuthorizedPersonPage(driver)
        auth_person_page.open_auth_person()
        successful_title = auth_person_page.unblock()
        assert successful_title == "Доступ открыт"
