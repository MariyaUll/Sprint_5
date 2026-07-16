from functions import *
from locators import *
from constants import *

class TestLogin:

    def test_login_via_enter_account_button(self, registered_user):
        driver, email, password = registered_user

        driver.get(BASE_URL)
        wait_for_clickable(driver, BTN_ENTER_ACCOUNT).click()

        # Заполняем форму входа
        wait_for_element(driver, INPUT_LOGIN).send_keys(email)
        wait_for_element(driver, INPUT_PASSWORD).send_keys(password)
        wait_for_clickable(driver, BTN_LOGIN_SUBMIT).click()

        # Проверяем вход (наличие элемента личного кабинета)
        assert wait_for_element(driver, BTN_ORDER) is not None, "Вход не выполнен"


    def test_login_via_personal_cabinet_button(self, registered_user):
        driver, email, password = registered_user

        driver.get(BASE_URL)
        wait_for_clickable(driver, BTN_PERSONAL_CABINET, By.CSS_SELECTOR).click()
        wait_for_element(driver, INPUT_LOGIN).send_keys(email)
        wait_for_element(driver, INPUT_PASSWORD).send_keys(password)
        wait_for_clickable(driver, BTN_LOGIN_SUBMIT).click()

        assert wait_for_element(driver, BTN_ORDER) is not None, "Вход не выполнен"


    def test_login_after_registration(self, driver):
    
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

        # Ждём, пока не произойдет переход на страницу login
        WebDriverWait(driver, 10).until(EC.url_contains("/login"))

        wait_for_element(driver, INPUT_LOGIN).send_keys(email)
        wait_for_element(driver, INPUT_PASSWORD).send_keys(password)
        wait_for_clickable(driver, BTN_LOGIN_SUBMIT).click()

        assert wait_for_element(driver, BTN_ORDER) is not None, "Вход не выполнен"


    # вход в систему на странице восстановления пароля
    def test_login_via_password_recovery_button(self, registered_user):
        driver, email, password = registered_user

        driver.get(BASE_URL)
        wait_for_clickable(driver, BTN_PERSONAL_CABINET, By.CSS_SELECTOR).click()
        wait_for_clickable(driver, BTN_FORGOT_PASSWORD, By.CSS_SELECTOR).click()
        wait_for_clickable(driver, BTN_LOGIN, By.CSS_SELECTOR).click()

        wait_for_element(driver, INPUT_LOGIN).send_keys(email)
        wait_for_element(driver, INPUT_PASSWORD).send_keys(password)
        wait_for_clickable(driver, BTN_LOGIN_SUBMIT).click()

        assert wait_for_element(driver, BTN_ORDER) is not None, "Вход не выполнен"      