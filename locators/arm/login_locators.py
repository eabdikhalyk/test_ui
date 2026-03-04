from selenium.webdriver.common.by import By

USER_NAME = (By.XPATH,"//span[contains(text(),'Логин')]/following-sibling::input")
PASSWORD = (By.XPATH, "//input[@type='password']")
BUTTON = (By.XPATH,"//span[contains(text(),'Войти')]")
MAIN_TITLE = (By.XPATH,"//p[contains(text(),'B-Business')]")