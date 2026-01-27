import pytest
from selenium import webdriver
from logs.logger import get_logs

log = get_logs()

@pytest.fixture
def driver():
    log.info(f"starting driver")
    options = webdriver.ChromeOptions()
    #options.add_argument("--headless")  # Для CI
    options.add_argument("--incognito")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--allow-insecure-localhost")
    options.add_argument("--allow-running-insecure-content")
    options.add_experimental_option("detach", True)
    my_driver = webdriver.Chrome(options=options)
    my_driver.implicitly_wait(10)
    my_driver.maximize_window()
    yield my_driver
    log.info(f"closing driver")
    my_driver.quit()
