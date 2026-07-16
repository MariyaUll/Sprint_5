import pytest
from functions import *
from locators import *
from constants import *

# # --- Раздел «Конструктор» ---
class TestConstructor:
    @pytest.mark.parametrize("tab_locator, tab_name", TABS_DATA)
    def test_constructor_tabs(self, driver, tab_locator, tab_name):
        driver.get(BASE_URL)
        elem = select_tab(driver, tab_locator)

        assert elem.text == tab_name, f"Выделен не верный таб: ожидалось {tab_name}"


    def test_constructor_tab_buns(self, driver):
        driver.get(BASE_URL)
        wait_for_clickable(driver, BTN_CONSTRUCTOR).click()
        
        #для проверки активации вкладки булки сперва переходим на другой таб а потом возвращаемся обратно
        #переходим на вкладку соусы
        elem = select_tab(driver, TAB_SAUCES)
        
        #переходим обратно на таб булки
        elem = select_tab(driver, TAB_BUNS)
       
        assert elem.text == "Булки", "Выделен не верный таб: ожидалось 'Билки'"