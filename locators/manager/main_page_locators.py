from selenium.webdriver.common.by import By

CONTEXT_MENU = (By.XPATH,"//td[normalize-space()='sber22200']/../td[7]//button")
BUTTON_INI_DIGITAL = (By.XPATH,"//div/div/div/span[normalize-space()='Инициализировать сертификат УЦ КЦМР']")
MAIN_TITLE = (By.XPATH,"//span[text()='Главная' or text()='common_main']")
BUTTON_MANAGEMENT = (By.XPATH,"//span[text()='Менеджмент']")
BUTTON_ORGANIZATION = (By.XPATH,"//span//div/div[text()='Организации']")
BUTTON_SEARCH = (By.XPATH,"//*[@title='Поиск']")
INPUT_TEXT = (By.XPATH,"//*[@type='text']")
OPERATION = (By.XPATH,"//*[@title='Операции']")
BUTTON_AUTH_PERSON = (By.XPATH,"//div[text()='Уполномоченные лица']")

COMPANY_NAME = "ТОО Hyundai Premium Almaty"