from functions import *
from locators import *

# # --- Переход из личного кабинета в конструктор ---

def test_navigate_from_personal_cabinet_to_constructor():
    driver = setup_driver()
    try:
        driver.get(BASE_URL)
        wait_for_clickable(driver, BTN_PERSONAL_CABINET, By.CSS_SELECTOR).click()
        wait_for_clickable(driver, BTN_CONSTRUCTOR).click()
        
        # Проверяем наличие заголовка в конструкторе
        assert wait_for_element(driver, H1_ASSEMBLE_BURGER) is not None
    finally:
        driver.quit()

def test_navigate_via_logo_from_personal_cabinet():
    driver = setup_driver()
    try:
        driver.get(BASE_URL)
        wait_for_clickable(driver, BTN_PERSONAL_CABINET, By.CSS_SELECTOR).click()
        wait_for_clickable(driver, LOGO_STELLAR_BURGERS, By.CSS_SELECTOR).click()

        # После клика по логотипу ожидаем, что вернулись на главную или в конструктор
        # Здесь проверяем, что заголовок конструктора доступен
        assert wait_for_element(driver, H1_ASSEMBLE_BURGER) is not None
    finally:
        driver.quit()

        # # --- Переход в личный кабинет ---

def test_navigate_to_personal_cabinet():
    driver = setup_driver()
    try:
        driver.get(BASE_URL)
        wait_for_clickable(driver, BTN_PERSONAL_CABINET, By.CSS_SELECTOR).click()
        
        # Убеждаемся, что перешли в личный кабинет (есть заголовок/элемент ЛК)
        assert wait_for_element(driver, BTN_LOGIN_SUBMIT) is not None, "Не удалось перейти в личный кабинет"
    finally:
        driver.quit()
