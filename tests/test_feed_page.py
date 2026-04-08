
import pytest
from pages.feed_page import FeedPage
from pages.login_page import LoginPage
from pages.constructor_page import ConstructorPage
from data import INGREDIENT_NAME, PARAMETRIZE_ORDER_COUNTER
import allure


class TestFeedPage:

    @allure.feature("Страница Лента Заказов")
    @allure.title("Открытие страницы ленты заказов")
    def test_open_feed_page_is_success(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.click_feed_tab()
        with allure.step("Проверка URL"):
            assert "/feed" in constructor_page.current_url(), "Не открылась страница Лента Заказов"


    @pytest.mark.parametrize("counter_method, allure_step_name, title", PARAMETRIZE_ORDER_COUNTER)
    @allure.feature("Страница Лента Заказов")
    @allure.title("Создание заказа увеличивает счетчик")
    def test_order_creation_increases_counter(self,driver, user, counter_method, allure_step_name, title):
        allure.dynamic.title(title)
    
        constructor_page = ConstructorPage(driver)
        constructor_page.click_feed_tab()
    
        feed_page = FeedPage(driver)
        before = getattr(feed_page, counter_method)()
    
        login_page = LoginPage(driver)
        login_page.login(user["email"], user["password"])
    
        constructor_page.create_order_and_return_to_feed(INGREDIENT_NAME)
        
        after = getattr(feed_page, counter_method)()
    
        with allure.step(allure_step_name):
            assert after > before, f"{allure_step_name} не увеличился после создания нового заказа"
        

    @allure.feature("Страница Лента Заказов")
    @allure.title("Появление созданного заказа в Ленте Заказов")
    def test_order_appears_in_feed_after_creation_is_success(self, driver, user):
        constructor_page = ConstructorPage(driver)
        constructor_page.click_feed_tab()
        feed_page = FeedPage(driver)
        login_page = LoginPage(driver)
        login_page.login(user["email"], user["password"])    
        constructor_page.create_order(INGREDIENT_NAME)
        order_number = constructor_page.get_order_number_from_modal()
        constructor_page.wait_and_close_order_modal()
        constructor_page.click_feed_tab()
        order_text = feed_page.is_order_in_progress(order_number)
        with allure.step("Проверяем появление заказа в ленте"):
            assert order_text == order_number.zfill(7), (f"Ожидался заказ с номером {order_number.zfill(7)}, "f"но в списке найдено: {order_text}")