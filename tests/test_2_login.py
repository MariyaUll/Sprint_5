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

def test_login_via_enter_account_button():
    driver = setup_driver()
    try:
        driver.get(BASE_URL)
        wait_for_clickable(driver, BTN_ENTER_ACCOUNT).click()

        # Заполняем форму входа
        wait_for_element(driver, INPUT_LOGIN).send_keys(email)
        wait_for_element(driver, INPUT_PASSWORD).send_keys(password)
        wait_for_clickable(driver, BTN_LOGIN_SUBMIT).click()

        # Проверяем вход (наличие элемента личного кабинета)
        assert wait_for_element(driver, BTN_ORDER) is not None, "Вход не выполнен"
    finally:
        driver.quit()

def test_login_via_personal_cabinet_button():
    driver = setup_driver()
    try:
        driver.get(BASE_URL)
        wait_for_clickable(driver, BTN_PERSONAL_CABINET, By.CSS_SELECTOR).click()
        wait_for_element(driver, INPUT_LOGIN).send_keys(email)
        wait_for_element(driver, INPUT_PASSWORD).send_keys(password)
        wait_for_clickable(driver, BTN_LOGIN_SUBMIT).click()

        assert wait_for_element(driver, BTN_ORDER) is not None, "Вход не выполнен"
    finally:
        driver.quit()

def test_login_after_registration():
    driver = setup_driver()
    try:
        driver.get(BASE_URL)
        wait_for_clickable(driver, BTN_PERSONAL_CABINET, By.CSS_SELECTOR).click()
        wait_for_clickable(driver, BTN_SIGN_UP, By.CSS_SELECTOR).click()
        
        email = generate_unique_email('MariaUllrich', 49)
        name = "Maria"
        password = generate_password(10)

        # Заполняем форму регистрации
        wait_for_element(driver, INPUT_NAME).send_keys(name)
        wait_for_element(driver, INPUT_LOGIN).send_keys(email)
        wait_for_element(driver, INPUT_PASSWORD).send_keys(password)
        wait_for_clickable(driver, BTN_REGISTER_SUBMIT).click()
        time.sleep(1) # ставим задержку, т.к. форма не успевает отстроить нужные элементы

        wait_for_element(driver, INPUT_LOGIN).send_keys(email)
        wait_for_element(driver, INPUT_PASSWORD).send_keys(password)
        wait_for_clickable(driver, BTN_LOGIN_SUBMIT).click()

        assert wait_for_element(driver, BTN_ORDER) is not None, "Вход не выполнен"
    finally:
        driver.quit()

# вход в систему на странице восстановления пароля
def test_login_via_password_recovery_button():
    driver = setup_driver()
    try:
        driver.get(BASE_URL)
        wait_for_clickable(driver, BTN_PERSONAL_CABINET, By.CSS_SELECTOR).click()
        wait_for_clickable(driver, BTN_FORGOT_PASSWORD, By.CSS_SELECTOR).click()
        wait_for_clickable(driver, BTN_LOGIN, By.CSS_SELECTOR).click()

        wait_for_element(driver, INPUT_LOGIN).send_keys(email)
        wait_for_element(driver, INPUT_PASSWORD).send_keys(password)
        wait_for_clickable(driver, BTN_LOGIN_SUBMIT).click()

        assert wait_for_element(driver, BTN_ORDER) is not None, "Вход не выполнен"
    finally:
        driver.quit()        