from selenium.webdriver.common.by import By

ADVERTISING_TAB = (By.XPATH,"//span[contains(text(),'Реклама')]")
POPUP_TAB = (By.XPATH,"//span[contains(text(),'Pop-up')]")
CREATE_BUTTON = (By.XPATH,"//span[contains(text(),'Создать')]")
#Fields
CODE_OF_PRODUCT = (By.XPATH,"//span[contains(text(),'Код продукта')]/following-sibling::input")
NAME_OF_POPUP = (By.XPATH,"//span[contains(text(),'Название pop-up')]/following-sibling::input")
ORDER = (By.XPATH,"//span[contains(text(),'Порядок')]/following-sibling::input")
DROPDOWN_LIST = (By.XPATH,"//div[@class='Select-FieldContainer']")
MOBILE = (By.XPATH,"//div[@class='ListItemText']/span[contains(text(),'MOBILE')]")
UPLOAD_FILE_KZ= (By.XPATH,"//span[contains(text(),'Файл (RU)')]")
UPLOAD_FILE_KZ_INPUT = (By.XPATH,"//span[contains(text(),'Файл (RU)')]/ancestor::*[contains(@class,'FilePicker')][1]//input[@type='file']")
UPLOAD_FILE_RU= (By.XPATH,"//span[contains(text(),'Файл (RU)')]")
UPLOAD_FILE_EN= (By.XPATH,"//span[contains(text(),'Файл (EN)')]")
DEEP_LINK = (By.XPATH,"//span[contains(text(),'Deep link')]")

#Text
TEXT_CODE_OF_PRODUCT = "CODE_OF_PRODUCT"
TEXT_NAME_OF_POPUP = "NAME_OF_POPUP"
TEXT_ORDER = "1"
POPUP_FILE_KZ = r"D:\popup\popup_kz.png"
POPUP_FILE_RU = "POPUP_FILE_RU"
POPUP_FILE_EN = "POPUP_FILE_EN"
