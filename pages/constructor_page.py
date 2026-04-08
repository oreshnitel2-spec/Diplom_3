import allure

from locators.base_page_locators import FEED_TAB
from pages.base_page import BasePage
from locators.constructor_page_locators import  BURGER_BUN_DROP_AREA, INGREDIENT_MODAL_TITLE, INGREDIENT_MODAL_CLOSE_BUTTON, ORDER_BUTTON, ORDER_MODAL_CLOSE_BUTTON, ORDER_NUMBER, ingredient_image_by_alt, ingredient_image_by_alt, ingredient_name_in_modal_by_text, ingredient_price_in_constructor_by_alt

class ConstructorPage(BasePage):


    @allure.step("Клик по ингредиенту: {alt_text}")
    def click_ingredient_by_alt(self, alt_text: str):
        """Клик по ингредиенту по alt картинки"""
        locator = ingredient_image_by_alt(alt_text)
        self.click(locator)

    @allure.step("Проверка, что модальное окно ингредиента не отображается")
    def ingredient_modal_is_not_visible(self, timeout=5):
        return self.wait_until_not_visible(INGREDIENT_MODAL_TITLE, timeout)
    
    
    @allure.step("Проверка, что имя ингредиента в модалке совпадает с ожидаемым")
    def ingredient_modal_name_matches(self, expected_name: str):
        locator = ingredient_name_in_modal_by_text(expected_name)
        return self.find_element(locator).is_displayed()
    
    @allure.step("Закрытие окна ингредиента")
    def click_close_ingredient_modal(self):
        self.click(INGREDIENT_MODAL_CLOSE_BUTTON)

    @allure.step("Получение цены ингредиента в конструкторе")
    def get_ingredient_price_in_constructor(self, alt_text: str) -> str:
        """Возвращает цену ингредиента в конструкторе по alt картинки"""
        price_locator = ingredient_price_in_constructor_by_alt(alt_text)
        return self.find_element(price_locator).text
    
    @allure.step("Добавление ингредиента в конструктор")
    def add_ingredient_to_constructor_by_alt_js(self, alt_text: str):
        ingredient = self.find_element(ingredient_image_by_alt(alt_text))
        drop_area = self.find_element(BURGER_BUN_DROP_AREA)
        self.drag_and_drop_js(ingredient, drop_area)
        
    @allure.step("Клик по кнопке Оформить заказ")
    def click_order_button(self):
        self.click(ORDER_BUTTON)

    @allure.step("Создание заказа")
    def create_order(self, alt_text: str):
        self.add_ingredient_to_constructor_by_alt_js(alt_text)
        self.click_order_button()
        

    @allure.step("Закрытие окна заказа")
    def close_order_modal(self):
        self.wait_for_clickable(ORDER_MODAL_CLOSE_BUTTON)
        self.js_click(ORDER_MODAL_CLOSE_BUTTON)

    @allure.step("Ожидание появления окна заказа")
    def wait_for_order_modal(self):
        self.wait_for_visibility(ORDER_NUMBER, timeout=15)

    @allure.step("Ожидание появления окна заказа и закрытие его")
    def wait_and_close_order_modal(self):
        self.wait_for_order_modal()
        self.close_order_modal()
       
    @allure.step("Получение номера заказа из модального окна")
    def get_order_number_from_modal(self):
        return self.wait_for_text_change(ORDER_NUMBER,check_func=lambda text: text != "9999" and text != "")
    
    @allure.step("Ожидание изменения текста элемента")
    def wait_for_text_change(self, locator, check_func, timeout=10):
        element = self.wait_for_visibility(locator, timeout)
    
        def _text_changed(driver):
            text = element.text.strip()
            return check_func(text)

        self.wait_until(_text_changed, timeout)
        return element.text.strip()
    
    @allure.step("Клик по вкладке Лента Заказов")
    def click_feed_tab(self):
        self.js_click(FEED_TAB)

    @allure.step("Создать заказ и вернуться на вкладку Лента")
    def create_order_and_return_to_feed(self, ingredient_name):
        self.create_order(ingredient_name)
        self.get_order_number_from_modal()
        self.wait_and_close_order_modal()
        self.click_feed_tab()
        