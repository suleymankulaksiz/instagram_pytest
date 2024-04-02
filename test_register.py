import json
from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import openpyxl
from constants.globalConstants import *

class Test_Source:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(BASE_URL)

    def teardown_method(self):
        self.driver.quit()

    def waitForElementVisible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def test_spassword_register(self):
        kaydol_button = self.waitForElementVisible((By.XPATH, KAYITOL_XPATH))
        kaydol_button.click()

        
        email_or_phone = self.waitForElementVisible((By.NAME, INPUTEOP_NAME))
        email_or_phone.send_keys(EMAIL)
        
        input_name = self.waitForElementVisible((By.NAME, FULLNAME_NAME))
        input_name.send_keys(NAME_LASTNAME)
        
        input_nickname = self.waitForElementVisible((By.NAME, NICKNAME_NAME))
        input_nickname.send_keys(NICK)
        
        input_password = self.waitForElementVisible((By.NAME, PASSWORD_NAME))
        input_password.send_keys(PASSWORD)
        
        register_button = self.waitForElementVisible((By.XPATH, KAYDOL))
        register_button.click()

        alertMessage =self.waitForElementVisible((By.XPATH,ALERTMESSAGE_XPATH))
        if alertMessage.text == ALERTMESSAGE_TEXT:
             print("Uyarı mesajı doğru şekilde görüntülendi.")
        else:
             print("Uyarı mesajı beklenen metinden farklı:", alertMessage.text)

        assert alertMessage.text == ALERTMESSAGE_TEXT