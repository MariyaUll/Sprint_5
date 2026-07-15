import random
import string
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from constants import *

def wait_for_element(driver, locator, by_id=By.XPATH, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located((by_id, locator))
    )

def wait_for_clickable(driver, locator, by_id=By.XPATH, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((by_id, locator))
    )


def generate_unique_email(name: str = 'ivan_ivanov', cohort: int = 1) -> str:
    """
    Генерирует уникальный email по шаблону:
    имя_фамилия_номер когорты_любые 3 цифры@домен
    name_second_name_cohort_numbers
    Пример: ivan_ivanov1123@yandex.ru
    """
    digits = "".join(random.choices(string.digits, k=3))
    return f"{name}{str(cohort)}{digits}@yandex.ru"


def generate_password(length: int = 8) -> str:
    """Генерирует случайный пароль заданной длины (минимум 6 символов)."""
    if length < 6:
        length = 6
    chars = string.ascii_letters + string.digits
    return "".join(random.choices(chars, k=length))

def registration(driver, email: str, name, password: str):
    driver.get(BASE_URL)
    wait_for_clickable(driver, BTN_PERSONAL_CABINET, By.CSS_SELECTOR).click()
    wait_for_clickable(driver, BTN_SIGN_UP, By.CSS_SELECTOR).click()
    wait_for_element(driver, INPUT_NAME).send_keys(name)
    wait_for_element(driver, INPUT_LOGIN).send_keys(email)
    wait_for_element(driver, INPUT_PASSWORD).send_keys(password)
    wait_for_clickable(driver, BTN_REGISTER_SUBMIT).click()
