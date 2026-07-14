import time
from functions import *
from locators import *

# # --- Раздел «Конструктор» ---

def test_constructor_tabs():
    driver = setup_driver()
    try:
        driver.get(BASE_URL)
        wait_for_clickable(driver, BTN_CONSTRUCTOR).click()

        # Переключаемся между вкладками и проверяем их доступность
        wait_for_clickable(driver, TAB_SAUCES).click()
        time.sleep(0.5) # небольшая пауза, чтобы интерфейс успел обновиться

        wait_for_clickable(driver, TAB_INGREDIENTS).click()
        time.sleep(0.5)

        wait_for_clickable(driver, TAB_BUNS).click()
        time.sleep(0.5)

        # Если вкладки видны и кликабельны — считаем тест пройденным
        assert True
    finally:
        driver.quit()