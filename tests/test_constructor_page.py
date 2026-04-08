import allure

from pages.constructor_page import ConstructorPage
from pages.feed_page import FeedPage
from urls import BASE_URL
from data import INGREDIENT_NAME, EXPECTED_INGREDIENT_PRICE

class TestConstructorPage:
    @allure.feature("Страница Конструктор")
    @allure.title("Проверка открытия страницы Конструктор")
    def test_open_constructor_page_is_success(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.click_feed_tab()
        feed_page = FeedPage(driver)
        feed_page.click_constructor_tab()
        assert constructor_page.current_url().rstrip("/") == BASE_URL, "Не открылась страница Конструктор"

    @allure.feature("Страница Конструктор")
    @allure.title("Проверка открытия модального окна ингредиента")
    def test_open_ingredient_modal_is_success(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.click_ingredient_by_alt(INGREDIENT_NAME)
        assert constructor_page.ingredient_modal_name_matches(INGREDIENT_NAME), "Имя ингредиента в модалке не совпадает с ожидаемым"

    @allure.feature("Страница Конструктор")
    @allure.title("Проверка закрытия модального окна ингредиента")
    def test_close_ingredient_modal_is_success(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.click_ingredient_by_alt(INGREDIENT_NAME)
        constructor_page.click_close_ingredient_modal()
        assert constructor_page.ingredient_modal_is_not_visible(), "Модальное окно не закрылось"

    @allure.feature("Страница Конструктор")
    @allure.title("Проверка добавления ингредиента в конструктор")
    def test_add_ingredient_to_constructor_is_success(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.add_ingredient_to_constructor_by_alt_js(INGREDIENT_NAME)
        displayed_price = constructor_page.get_ingredient_price_in_constructor(INGREDIENT_NAME)
        assert displayed_price == EXPECTED_INGREDIENT_PRICE, f"Цена ингредиента в конструкторе ({displayed_price}) не совпадает с ожидаемой ({EXPECTED_INGREDIENT_PRICE})"