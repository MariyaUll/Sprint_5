from functions import *
from locators import *
from constants import *

# # --- Переход из личного кабинета в конструктор ---
class TestNavigation:

    def test_navigate_from_personal_cabinet_to_constructor(self, driver):
   
        driver.get(BASE_URL)
        wait_for_clickable(driver, BTN_PERSONAL_CABINET, By.CSS_SELECTOR).click()
        wait_for_clickable(driver, BTN_CONSTRUCTOR).click()
        
        # Проверяем наличие заголовка в конструкторе
        assert wait_for_element(driver, H1_ASSEMBLE_BURGER) is not None

    def test_navigate_via_logo_from_personal_cabinet(self, driver):
    
        driver.get(BASE_URL)
        wait_for_clickable(driver, BTN_PERSONAL_CABINET, By.CSS_SELECTOR).click()
        wait_for_clickable(driver, LOGO_STELLAR_BURGERS, By.CSS_SELECTOR).click()

        # После клика по логотипу ожидаем, что вернулись на главную или в конструктор
        # Здесь проверяем, что заголовок конструктора доступен
        assert wait_for_element(driver, H1_ASSEMBLE_BURGER) is not None

        # # --- Переход в личный кабинет ---

    def test_navigate_to_personal_cabinet(self, driver):
  
        driver.get(BASE_URL)
        wait_for_clickable(driver, BTN_PERSONAL_CABINET, By.CSS_SELECTOR).click()
        
        # Убеждаемся, что перешли в личный кабинет (есть заголовок/элемент ЛК)
        assert wait_for_element(driver, BTN_LOGIN_SUBMIT) is not None, "Не удалось перейти в личный кабинет"
        