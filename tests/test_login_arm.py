import os

import pytest
from dotenv import load_dotenv

from logs.logger import get_logs
from pages.arm.login_page import LoginPage


class TestAuthorization:
    @pytest.mark.skip(reason="Этот тест временно отключен")
    def test_authorization(self, driver):
        log = get_logs()
        load_dotenv()
        username = os.getenv("MANAGER_USER")
        password = os.getenv("MANAGER_PASSWORD")
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute(username, password)
        text = login_page.get_title()
        log.info("Logged in")
        assert text == "B-Business"