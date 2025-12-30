from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest


class TestCT01:
    
    def test_ct01_adicionar_produtos_carrinho(self, driver):
        # Fazer Login na Plataforma
        #driver = conftest.driver
        wait = WebDriverWait(driver, 10)
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        assert driver.find_element(By.XPATH, "//span[@class= 'title']")


        # Clica no produto
        driver.find_element(
            By.XPATH,
            "//div[contains(@class,'inventory_item_name') and text()='Sauce Labs Backpack']"
        ).click()

        # Espera botão de adicionar ao carrinho
        wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart"))).click()

        # Acessar o carrinho
        driver.find_element(By.XPATH, "//*[@class= 'shopping_cart_link']").click()

        # Voltar a página principal
        driver.find_element(By.XPATH, "//*[@id= 'continue-shopping']").click()

        # Clica em outro produto
        driver.find_element(
            By.XPATH,
            "//div[contains(@class,'inventory_item_name') and text()='Sauce Labs Bolt T-Shirt']"
        ).click()

        # Espera botão de adicionar ao carrinho e acessar o carrinho
        wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart"))).click()
        driver.find_element(By.XPATH, "//*[@class= 'shopping_cart_link']").click()
