from functions import *
from locators import *
from constants import *

# тест по выходу из кабинета
class TestLogout:
    def test_logout(self, registered_user):
        driver, email, password = registered_user

        driver.get(BASE_URL)
        wait_for_clickable(driver, BTN_PERSONAL_CABINET, By.CSS_SELECTOR).click()

        # Заполняем форму входа
        wait_for_element(driver, INPUT_LOGIN).send_keys(email)
        wait_for_element(driver, INPUT_PASSWORD).send_keys(password)
        wait_for_clickable(driver, BTN_LOGIN_SUBMIT).click()

        wait_for_clickable(driver, BTN_PERSONAL_CABINET, By.CSS_SELECTOR).click()

        # Ждём, пока не произойдет переход на страницу профиля
        WebDriverWait(driver, 10).until(EC.url_contains("/profile"))
        wait_for_clickable(driver, BTN_LOGOUT).click()

        # Ждём, пока не произойдет переход на страницу login
        WebDriverWait(driver, 10).until(EC.url_contains("/login"))
        
        # После выхода проверяем, что кнопка входа снова видна
        assert wait_for_element(driver, BTN_LOGIN_SUBMIT) is not None