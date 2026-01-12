from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys


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
        self.esperar_elemento(locator)
        assert self.encontrar_elemento(locator).is_displayed(),f"O elemento '{locator}' não foi encontrado na tela"

    def esperar_elemento(self, driver, locator, timeout=10):
        wait = WebDriverWait(driver, 10)
        return wait.until(EC.visibility_of_element_located((By.ID, "user-name")))

    def esperar_elemento(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator))
    
    def clique_dublo(self, locator ):
        element = self.esperar_elemento(locator)
        ActionChains(self.driver).double_click(element).perform()
    
    def clique_botao_direito(self, locator):
        element = self.esperar_elemento(locator)
        ActionChains(self.driver).context_click(element).perform()

    def pressionar_tecla(self, locator, key):
        elem = self.encontrar_elemento(locator)
        if key == "ENTER":
            elem.send_keys(Keys.ENTER)
        elif key == "ESPACO":
            elem.send_keys(Keys.SPACE)
        elif key == "F1":
            elem.send_keys(Keys.F1)
    