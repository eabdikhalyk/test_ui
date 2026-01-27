from selenium.webdriver.common.by import By

EDIT_BUTTON = (By.XPATH,"//button[@class='ButtonBase IconButtonNext IconButtonNext_variant_function IconButtonNext_size_m IconButtonNext_color_secondary']")
CONTINUE_BUTTON = (By.XPATH,"//span[text()='Продолжить']")
SMS_CODE = (By.XPATH,"//div[@class='InputOTP-InputContainer']//input")
DIALOG_CONTINUE_BUTTON = (By.XPATH,"//div[@class='Dialog-Footer']//span[text()='Продолжить']")
INPUT_NUMBER = (By.XPATH,"//input[@class='FieldInput Input-Field' and @type='text']")
CHECKBOX = (By.XPATH,'//span[@class="FormControlLabel-Content"]')
ALERT_TITLE = (By.XPATH,"//div[@class='Alert-Content']//div[@class='Alert-Title']")