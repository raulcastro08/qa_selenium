from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class TestCT03:
    def test_ct03_checkout(self, driver):

        wait = WebDriverWait(driver, 10)

    # Fazer Login na Plataforma
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

        # Clicar em outro produto
        driver.find_element(
            By.XPATH,
            "//div[contains(@class,'inventory_item_name') and text()='Sauce Labs Bolt T-Shirt']"
        ).click()

        # Esperar botão de adicionar ao carrinho e acessar o carrinho
        wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart"))).click()
        driver.find_element(By.XPATH, "//*[@class= 'shopping_cart_link']").click()

        #Ir para checkout
        driver.find_element(By.XPATH, "//*[@id= 'checkout']").click()

        # Preencher dados do comprador
        driver.find_element(By.ID, "first-name").send_keys("Raul")
        driver.find_element(By.ID, "last-name").send_keys("Santos")
        driver.find_element(By.ID, "postal-code").send_keys("000000000")
        driver.find_element(By.XPATH, "//*[@id= 'continue']").click()

        #Velidar os itens no checkout
        assert driver.find_element(By.XPATH, "//*[text()= 'Sauce Labs Backpack']")     
        assert driver.find_element(By.XPATH, "//*[text()= 'Sauce Labs Bolt T-Shirt']")

        #Finalizar Compra
        driver.find_element(By.XPATH, "//*[@id= 'finish']").click()

        assert driver.find_element(By.XPATH, "//*[text()= 'Thank you for your order!']")

