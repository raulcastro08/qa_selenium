import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class TestCT03:
    def test_ct03_erro_autenticacao(self, driver):
        #driver = conftest.driver
        wait = WebDriverWait(driver, 10)


        # Fazer Login na Plataforma
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauc")
        driver.find_element(By.ID, "login-button").click()

        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()= 'Epic sadface: Username and password do not match any user in this service']"))).is_displayed
