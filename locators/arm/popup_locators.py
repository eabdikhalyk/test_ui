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
UPLOAD_FILE_KZ_INPUT = (By.XPATH,"//span[contains(text(),'Файл (KZ)')]/ancestor::*[contains(@class,'FilePicker')][1]//input[@type='file']")
UPLOAD_FILE_RU_INPUT= (By.XPATH,"//span[contains(text(),'Файл (RU)')]/ancestor::*[contains(@class,'FilePicker')][1]//input[@type='file']")
UPLOAD_FILE_EN_INPUT= (By.XPATH,"//span[contains(text(),'Файл (EN)')]/ancestor::*[contains(@class,'FilePicker')][1]//input[@type='file']")
DEEP_LINK_INPUT = (By.XPATH,"//span[contains(text(),'Deep link')]/following-sibling::input")
STYLE_OF_BLUE = (By.XPATH,"//div/span[contains(text(),'Синяя')]")
STYLE_OF_LIGHT_BLUE = (By.XPATH,"/html/body/div[3]/ul/li[2]/div/span[1]")
BUTTONS = (By.XPATH,"//span[starts-with(text(),'Название кнопки')]/following-sibling::input")
LINKS_INPUT = (By.XPATH,"//span[contains(text(),'Ссылка для редиректа')]/following-sibling::input")
BUTTON_SAVE = (By.XPATH,"//span[contains(text(),'Сохранить')]")
RESULT = (By.XPATH,"//td[contains(text(),'CODE_OF_PRODUCT')]")
#Text
TEXT_CODE_OF_PRODUCT = "CODE_OF_PRODUCT"
TEXT_NAME_OF_POPUP = "NAME_OF_POPUP"
TEXT_ORDER = "1"
POPUP_FILE_KZ = r"D:\popup\popup_kz.png"
POPUP_FILE_RU = r"D:\popup\popup_ru.png"
POPUP_FILE_EN = r"D:\popup\popup_en.png"
DEEP_LINK = "/applink/gov-services/gov-cabinet/fines"

BUTTON_KZ_INPUT_1 = "Басу"
BUTTON_RU_INPUT_1 = "Нажать"
BUTTON_EN_INPUT_1 = "Click"

LINK = "https://berekebank.kz/ru/small_business/credits/business/"

BUTTON_KZ_INPUT_2 = "Өту"
BUTTON_RU_INPUT_2 = "Перейти"
BUTTON_EN_INPUT_2 = "Go"

