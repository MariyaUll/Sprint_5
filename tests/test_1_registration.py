from functions import *
from locators import *

# --- Тесты регистрации ---

def test_successful_registration():
    driver = setup_driver()
    try:
        email = generate_unique_email('MariaUllrich', 49)
        name = "Maria"
        password = generate_password(10)
        registration(driver, email, name, password)

        # Проверяем, что регистрация успешна (например, есть элемент личного кабинета или нет ошибок)
        assert wait_for_element(driver, BTN_LOGIN_SUBMIT) is not None, "Не удалось подтвердить успешную регистрацию"
    finally:
        driver.quit()

def test_registration_error_short_password():
    driver = setup_driver()
    try:
        driver.get(BASE_URL)
        wait_for_clickable(driver, BTN_PERSONAL_CABINET, By.CSS_SELECTOR).click()
        try:
            wait_for_clickable(driver, BTN_SIGN_UP, By.CSS_SELECTOR).click()
        except Exception:
            pass

        email = generate_unique_email("petr_petrov", )
        name = "Пётр"
        password = "short"  # меньше 6 символов

        wait_for_element(driver, INPUT_NAME).send_keys(name)
        wait_for_element(driver, INPUT_LOGIN).send_keys(email)
        wait_for_element(driver, INPUT_PASSWORD).send_keys(password)
        wait_for_clickable(driver, BTN_REGISTER_SUBMIT).click()

        # Ожидаем сообщение об ошибке
        error_msg = wait_for_element(driver, ERR_MSG_REG)
        assert error_msg is not None and "пароль" in error_msg.text.lower(), "Не отобразилась ошибка для короткого пароля"
    finally:
        driver.quit()