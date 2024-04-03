import json
from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import openpyxl
from constants.globalConstants import *
#Kullanıcı login sayfasında
#Doğru kullanıcı adı girilir
#Yanlış şifre girilir
#Login butonuna tıklanır
#Belirtilen uyarı mesajı ekranda görüntülenir => "Bu şifreyi tahmin etmek çok kolay. Lütfen yeni bir şifre oluştur."
class Test_Login:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(BASE_URL)

    def teardown_method(self):
        self.driver.quit()

    def waitForElementVisible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def test_wpassword_login(self):
        login_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='loginForm']/div/div[3]")))
        if login_button.is_enabled():

            print("Login button is enabled.")
        else:
            print("Login button is not enabled.")
        input_username = self.waitForElementVisible((By.NAME,loginusername_NAME))
        input_username.send_keys(NICK)
        input_password = self.waitForElementVisible((By.NAME,loginpassword_NAME))
        input_password.send_keys(wrongpassword)
        login_button = self.waitForElementVisible((By.XPATH,login_button_XPATH))
        login_button.click()
        
        alertMessage = self.waitForElementVisible((By.XPATH, wrongpassword_alert_XPATH))
        assert alertMessage.text == "Üzgünüz, şifren yanlıştı. Lütfen şifreni dikkatlice kontrol et.", "Uyarı mesajı beklenen metinden farklı."