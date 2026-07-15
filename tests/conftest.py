import pytest
from selenium import webdriver
from functions import *

@pytest.fixture(scope="function")
def driver():
    driver_instance = webdriver.Chrome()
    driver_instance.maximize_window()
    yield driver_instance
    driver_instance.quit()

@pytest.fixture(scope="function")
def registered_user():
    """
    Регистрирует пользователя и возвращает кортеж: (driver, email, password)
    """
    driver = webdriver.Chrome()
    driver.maximize_window()

    email = generate_unique_email('RegUser', 999)
    name = "TestName"
    password = generate_password(10)

    registration(driver, email, name, password)
    yield driver, email, password
    driver.quit()