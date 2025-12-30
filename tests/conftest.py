import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    # Setup
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com")

    yield driver

    # Teardown
    driver.quit()