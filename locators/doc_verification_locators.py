from selenium.webdriver.common.by import By

INPUT_ID = (By.XPATH,"//input[@class='FieldInput Input-Field']")
BUTTON = (By.XPATH,"//span[@class='Button-Content']")
RESULT = (By.XPATH,"//h3[starts-with(normalize-space(.), 'Документ')]")

VALID_DOC_ID = "e4602c20-4b58-4db7-b757-0392cb9da4ac"
INVALID_DOC_ID = "04659c1f-94ef-44cc-9e28-4e7433f530e5_1"