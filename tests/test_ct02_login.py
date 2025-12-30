import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class TestCT02:
    def test_ct02_login(self, driver):
        wait = WebDriverWait(driver, 10)
        # Espera a página de login carregar
        wait.until(EC.visibility_of_element_located((By.ID, "user-name")))


        # Fazer Login na Plataforma
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        assert driver.find_element(By.XPATH, "//span[@class= 'title']").is_displayed
