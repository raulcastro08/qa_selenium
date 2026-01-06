import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.home_page import HomePage
from pages.login_page import LoginPage



class TestCT03:
    def test_ct03_erro_autenticacao(self, driver):
        wait = WebDriverWait(driver, 10)

        # Espera a página de login carregar
        wait.until(EC.visibility_of_element_located((By.ID, "user-name")))

        home_page = HomePage(driver)
        login_page = LoginPage(driver)

        #Fazer Login
        login_page.fazer_login("standard_user", "secret_sauc")

        #Verificar se o login foi realziado
        home_page.verificar_login_sem_sucesso()



