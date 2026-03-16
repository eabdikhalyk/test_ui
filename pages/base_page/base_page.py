import time
import os
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage():

    def __init__(self, driver: WebDriver):
        self._driver = driver
    def _get_driver(self):
        return self._driver
    def _find(self, locator: tuple) -> WebElement:
        return self._driver.find_element(*locator)

    def _finds(self, locator: tuple) -> list[WebElement]:
        return self._driver.find_elements(*locator)

    def _wait_until_element_is_visible(self, locator: tuple, time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.visibility_of_element_located(locator))

    def _wait_until_invisibility_of_element(self, locator: tuple, time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.invisibility_of_element(locator))

    def _wait_until_element_is_clickable(self, locator: tuple, time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.element_to_be_clickable(locator))

    def _wait_presence_of_element_located(self, locator: tuple, time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.presence_of_element_located(locator))

    def _wait_presence_of_all_elements_located(self, locator: tuple, time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.presence_of_all_elements_located(locator))

    def _type(self, locator: tuple, text: str, time: int = 10):
        self._wait_until_element_is_visible(locator, 10)
        self._find(locator).send_keys(text)

    def _click(self, locator: tuple, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).click()

    def _open_url(self, url: str):
        self._driver.get(url)

    def _get_text(self, locator: tuple, time: int = 10) -> str:
        self._wait_until_element_is_visible(locator, time)
        return self._find(locator).text

    def _is_displayed(self, locator: tuple) -> bool:
        try:
            return self._find(locator).is_displayed()
        except NoSuchElementException:
            return False

    def _safe_wait_for_page_load(self,driver, timeout=30):
        try:
            WebDriverWait(driver, timeout).until(
                lambda d: d.execute_script("return document.readyState") == "complete"
            )
            return True
        except TimeoutException:
            print("Страница не загрузилась в течение таймаута")
            return False

    def _wait_for_download(self,directory, timeout=30):
        print("[*] Ждём загрузку файла в:", directory)

        # Сохраняем список файлов до скачивания
        before = set(os.listdir(directory))
        print("[*] Файлы до:", before)

        seconds = 0
        while seconds < timeout:
            time.sleep(1)
            after = set(os.listdir(directory))
            # Новые файлы = скачанные
            new_files = after - before

            if new_files:
                downloading = any(f.endswith(".crdownload") or f.endswith(".part") for f in new_files)
                if not downloading:
                    print(f"[✓] Новый файл загружен: {new_files}")
                    return True
                else:
                    print(f"[...] Файл {new_files} ещё загружается...")

            seconds += 1

        print("[✗] Файл не был загружен за указанное время.")
        return False