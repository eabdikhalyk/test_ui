from selenium.webdriver.common.by import By

USER_NAME = (By.ID, "log-name")
PASSWORD = (By.ID, "log-pass")
BUTTON = (By.XPATH, "//*[contains(text(),'Войти')]")
MAIN_TITLE = (By.XPATH,"//span[text()='Главная' or text()='common_main']")