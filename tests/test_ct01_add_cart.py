from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.cart_page import CartPage


class TestCT01:
    
    def test_ct01_adicionar_produtos_carrinho(self, driver):
        wait = WebDriverWait(driver, 10)
        
        #Fazer Login na Plataforma
        
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        cart_page = CartPage(driver)

         #Fazer Login
        login_page.fazer_login("standard_user", "secret_sauce")

        #Verificar se o login foi realziado
        home_page.verificar_login_com_sucesso()
        
        
        
        #driver = conftest.driver
        #driver.find_element(By.ID, "user-name").send_keys("standard_user")
        #driver.find_element(By.ID, "password").send_keys("secret_sauce")
        #river.find_element(By.ID, "login-button").click()

        #assert driver.find_element(By.XPATH, "//span[@class= 'title']")



        #Clica no produto
        #driver.find_element(
         #).click()

        # Espera botão de adicionar ao carrinho
        #wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart"))).click()


        #Adcionar ao Carrinho
        home_page.adicionar_ao_carrinho("Sauce Labs Backpack")

        # Acessar o carrinho
        #driver.find_element(By.XPATH, "//*[@class= 'shopping_cart_link']").click()

        home_page.acessar_carrinho()
        cart_page.verificar_item_no_carrinho_exite("Sauce Labs Backpack")
        
        # Voltar a página principal
        ##driver.find_element(By.XPATH, "//*[@id= 'continue-shopping']").click()
        
        cart_page.voltar_as_compras()

        # Clica em outro produto
        home_page.adicionar_ao_carrinho("Sauce Labs Bolt T-Shirt")


        #Acessar carrinho e validar se novo item foi adicionado
        home_page.acessar_carrinho()
        cart_page.verificar_item_no_carrinho_exite("Sauce Labs Bolt T-Shirt")
