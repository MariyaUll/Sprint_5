from functions import *
from locators import *
from constants import *

# --- Тесты регистрации ---
class TestRegistration:
    def test_successful_registration(self, driver):
        email = generate_unique_email('MariaUllrich', 49)
        name = "Maria"
        password = generate_password(10)
        registration(driver, email, name, password)

        # Проверяем, что регистрация успешна (например, есть элемент личного кабинета или нет ошибок)
        assert wait_for_element(driver, BTN_LOGIN_SUBMIT) is not None, "Не удалось подтвердить успешную регистрацию"


    def test_registration_error_short_password(self, driver):
        driver.get(BASE_URL)
        wait_for_clickable(driver, BTN_PERSONAL_CABINET, By.CSS_SELECTOR).click()
        wait_for_clickable(driver, BTN_SIGN_UP, By.CSS_SELECTOR).click()

        email = generate_unique_email("petr_petrov", 12)
        name = "Пётр"
        password = "short"  # меньше 6 символов

        wait_for_element(driver, INPUT_NAME).send_keys(name)
        wait_for_element(driver, INPUT_LOGIN).send_keys(email)
        wait_for_element(driver, INPUT_PASSWORD).send_keys(password)
        wait_for_clickable(driver, BTN_REGISTER_SUBMIT).click()

        # Ожидаем сообщение об ошибке
        error_msg = wait_for_element(driver, ERR_MSG_REG)
        assert error_msg is not None and "пароль" in error_msg.text.lower(), "Не отобразилась ошибка для короткого пароля"
