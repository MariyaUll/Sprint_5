from functions import *
from locators import *
from constants import *

# # --- Раздел «Конструктор» ---
class TestConstructor:

    def test_constructor_tabs(self, driver):
   
        driver.get(BASE_URL)
        wait_for_clickable(driver, BTN_CONSTRUCTOR).click()

        tabs = [
            (TAB_SAUCES, "Соусы"),
            (TAB_INGREDIENTS, "Начинки"),
            (TAB_BUNS, "Булки"),
        ]

        for tab_locator, tab_name in tabs:
            element = wait_for_clickable(driver, tab_locator)
            element.click()

            # Ждём, пока у элемента появится активный класс
            WebDriverWait(driver, 10).until(
                lambda d: CURRENT_TAB_CLASS in element.get_attribute("class")
            )
