import os

import pytest
from dotenv import load_dotenv

from logs.logger import get_logs
from pages.customer.login_page import LoginPage
from tests.conftest import driver


class TestAuthorization:
    @pytest.mark.skip(reason="Этот тест временно отключен")
    def test_authorization(self, driver):
        log = get_logs()
        load_dotenv()
        username = os.getenv("ACQUIRING_USERNAME")
        password = os.getenv("ACQUIRING_PASSWORD")
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute(username, password)
        text = login_page.get_title()
        log.info("Logged in")
        assert text == "Главная"