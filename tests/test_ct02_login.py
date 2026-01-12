import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.home_page import HomePage


class TestCT02:
    def test_ct02_login(self, driver):
        

        home_page = HomePage(driver)
        login_page = LoginPage(driver)

        #Fazer Login
        login_page.fazer_login("standard_user", "secret_sauce")

        #Verificar se o login foi realziado
        home_page.verificar_login_com_sucesso()

    
