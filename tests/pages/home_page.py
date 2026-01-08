from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.titulo_pagina = ( By.XPATH, "//span[@class='title']")
        self.popup_erro = ( By.XPATH, "//*[text()='']")
        self.item_inventario = (By.XPATH, "//div[contains(@class,'inventory_item_name') and text()='{}']")
        self.botao_adicionar_carrinho = (By.ID, "add-to-cart")
        self.icone_carrinho = (By.XPATH, "//*[@class= 'shopping_cart_link']")

    def verificar_login_com_sucesso(self):
        self.verificar_se_elemento_exite(self.titulo_pagina)

# Seleciona iten cliclando no link e adiciona ao carrinho clicando no botão
    def adicionar_ao_carrinho(self, nome_item):
        item = (self.item_inventario[0], self.item_inventario[1].format(nome_item))
        self.clicar(item)
        self.clicar(self.botao_adicionar_carrinho)
    
    
    def acessar_carrinho(self):
        self.clicar(self.icone_carrinho)
