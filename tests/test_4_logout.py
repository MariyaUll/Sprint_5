from functions import *
from locators import *
import time


email = generate_unique_email('MariaUllrich', 49)
password = generate_password(10)

def test_successful_registration():
    driver = setup_driver()
    try:
        registration(driver, email, 'test', password)
    finally:
        driver.quit()

# тест по выходу из кабинета

def test_logout():
    driver = setup_driver()
    try:
        driver.get(BASE_URL)
        wait_for_clickable(driver, BTN_PERSONAL_CABINET, By.CSS_SELECTOR).click()

        # Заполняем форму входа
        wait_for_element(driver, INPUT_LOGIN).send_keys(email)
        wait_for_element(driver, INPUT_PASSWORD).send_keys(password)
        wait_for_clickable(driver, BTN_LOGIN_SUBMIT).click()

        wait_for_clickable(driver, BTN_PERSONAL_CABINET, By.CSS_SELECTOR).click()
        wait_for_clickable(driver, BTN_LOGOUT).click()
        time.sleep(1)
        # После выхода проверяем, что кнопка входа снова видна
        assert wait_for_element(driver, BTN_LOGIN_SUBMIT) is not None
    finally:
        driver.quit()