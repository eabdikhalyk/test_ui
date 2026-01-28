import os
import time

from dotenv import load_dotenv

from data.login_with_manager import login_with_manager
from pages.manager.login_page import LoginPage
from pages.manager.main_page import MainPage


class TestInitDigitalSignature:
    #@pytest.mark.skip(reason="Этот тест временно отключен")
    def test_init_digital_signature(self,driver):
        login_with_manager(driver,"MANAGER_USER","MANAGER_PASSWORD")
        main_page = MainPage(driver)
        main_page.open_company_auth_person()
        main_page.click_on_context_menu_auth_person()
        main_page.click_on_init_digital_signature()
        # main_page.fill_proFile()
        # main_page.click_on_button_init_digital()
        # is_successfully_issued = main_page.get_result_of_init_digital()
        # assert True == is_successfully_issued