import os

from dotenv import load_dotenv

from pages.customer.login_page import LoginPage
from tests.conftest import driver


def login_with_user(driver,username, password):
    load_dotenv()
    username = os.getenv(username)
    password = os.getenv(password)
    login_page = LoginPage(driver)
    login_page.open()
    login_page.execute(username, password)