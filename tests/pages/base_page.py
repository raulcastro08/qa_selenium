from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def encontrar_elemento(self, locator):
        return self.driver.find_element(*locator)

    def escrever(self, locator, texto):
        elemento = self.wait.until(EC.visibility_of_element_located(locator))
        elemento.clear()
        elemento.send_keys(texto)

    def clicar(self, locator):
        elemento = self.wait.until(EC.element_to_be_clickable(locator))
        elemento.click()

    def verificar_se_elemento_exite(self,locator):
        assert self.encontrar_elemento(locator).is_displayed(),f"O elemento '{locator}' não foi encontrado na tela"
