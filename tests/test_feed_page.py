
from pages.feed_page import FeedPage
from pages.login_page import LoginPage
from pages.constructor_page import ConstructorPage
from data import INGREDIENT_NAME
import allure


class TestFeedPage:

    @allure.feature("Страница Лента Заказов")
    @allure.title("Открытие страницы ленты заказов")
    def test_open_feed_page_is_success(self, driver):
        feed_page = FeedPage(driver)
        feed_page.click_feed_tab()
        with allure.step("Проверка URL"):
            assert "/feed" in feed_page.current_url(), "Не открылась страница Лента Заказов"

    @allure.feature("Страница Лента Заказов")
    @allure.title("Создание заказа увеличивает общее количество заказов")
    def test_order_creation_increases_total_count_is_success(self, driver, user):
        feed_page = FeedPage(driver)
        feed_page.click_feed_tab()
        before = feed_page.get_total_orders_count()
        login_page = LoginPage(driver)
        login_page.login(user["email"], user["password"])
        constructor_page = ConstructorPage(driver)
        constructor_page.create_order(INGREDIENT_NAME)
        constructor_page.get_order_number_from_modal()
        constructor_page.wait_and_close_order_modal()
        feed_page.click_feed_tab()
        after = feed_page.get_total_orders_count()
        with allure.step("Проверяем обновление счетчика"):
            assert after > before, "Количество заказов не увеличилось после создания нового заказа"

    @allure.feature("Страница Лента Заказов")
    @allure.title("Создание заказа увеличивает количество заказов за сегодня")
    def test_order_creation_increases_today_count_is_success(self, driver, user):
        feed_page = FeedPage(driver)
        feed_page.click_feed_tab()
        before = feed_page.get_today_orders_count()
        login_page = LoginPage(driver)
        login_page.login(user["email"], user["password"])
        constructor_page = ConstructorPage(driver)
        constructor_page.create_order(INGREDIENT_NAME)
        constructor_page.get_order_number_from_modal()
        constructor_page.wait_and_close_order_modal()
        feed_page.click_feed_tab()
        after = feed_page.get_today_orders_count()
        with allure.step("Проверяем счетчик за сегодня"):
            assert after > before, "Количество заказов за сегодня не увеличилось после создания нового заказа"

    @allure.feature("Страница Лента Заказов")
    @allure.title("Появление созданного заказа в Ленте Заказов")
    def test_order_appears_in_feed_after_creation_is_success(self, driver, user):
        feed_page = FeedPage(driver)
        feed_page.click_feed_tab()
        login_page = LoginPage(driver)
        login_page.login(user["email"], user["password"])
        constructor_page = ConstructorPage(driver)
        constructor_page.create_order(INGREDIENT_NAME)
        order_number = constructor_page.get_order_number_from_modal()
        constructor_page.wait_and_close_order_modal()
        feed_page.click_feed_tab()
        order_text = feed_page.is_order_in_progress(order_number)
        with allure.step("Проверяем появление заказа в ленте"):
            assert order_text == order_number.zfill(7), (f"Ожидался заказ с номером {order_number.zfill(7)}, "f"но в списке найдено: {order_text}")