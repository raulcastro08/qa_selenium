from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.titulo_pagina = ( By.XPATH, "//span[@class='title']")
        self.popup_erro = ( By.XPATH, "//*[text()= 'Epic sadface: Username and password do not match any user in this service']")

    def verificar_login_com_sucesso(self):
        self.verificar_se_elemento_exite(self.titulo_pagina)

    def verificar_login_sem_sucesso(self):
        self.verificar_se_elemento_exite(self.popup_erro)