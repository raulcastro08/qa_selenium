from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class CartPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.titulo_pagina = ( By.XPATH, "//span[@class='title']")
        self.itens_no_carrinho = (By.XPATH, "//div[contains(@class,'inventory_item_name') and text()='{}']")
        self.botao_voltar_compras = (By.XPATH, "//*[@id= 'continue-shopping']")
       

# Seleciona iten cliclando no link e adiciona ao carrinho clicando no botão
    def verificar_item_no_carrinho_exite(self, nome_item):
        item = (self.itens_no_carrinho[0], self.itens_no_carrinho[1].format(nome_item))
        self.verificar_se_elemento_exite(item)
  
    def voltar_as_compras(self):
        self.clicar(self.botao_voltar_compras)