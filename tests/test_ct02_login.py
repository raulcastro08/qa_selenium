import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage


class TestCT02:
    def test_ct02_login(self, driver):
        wait = WebDriverWait(driver, 10)

        # Espera a página de login carregar
        wait.until(EC.visibility_of_element_located((By.ID, "user-name")))

        login_page = LoginPage(driver)
        login_page.fazer_login("standard_user", "secret_sauce")

        assert driver.find_element(
            By.XPATH, "//span[@class='title']"
        ).is_displayed()
