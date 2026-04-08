
import allure
from locators.base_page_locators import CONSTRUCTOR_TAB
from pages.base_page import BasePage
from locators.feed_page_locators import ORDER_IN_PROGRESS_ITEM, TOTAL_ORDERS_COUNTER, TODAY_ORDERS_COUNTER, ORDER_IN_PROGRESS_ITEM
from selenium.common.exceptions import TimeoutException

class FeedPage(BasePage):


    @allure.step("Клик по вкладке Конструктор")
    def click_constructor_tab(self):
        self.click(CONSTRUCTOR_TAB)

    @allure.step("Получение количества выполненных заказов за все время")
    def get_total_orders_count(self):
        text = self.get_text(TOTAL_ORDERS_COUNTER)
        return int(text)

    @allure.step("Получение количества выполненных заказов за сегодня")
    def get_today_orders_count(self):
        text = self.get_text(TODAY_ORDERS_COUNTER)
        return int(text)
    
    @allure.step("Проверка наличия заказа в Ленте Заказов")
    def is_order_in_progress(self, order_number_modal: str, timeout=15) ->str | None:   
        order_number_feed = order_number_modal.zfill(7)
        try:
            return self.wait_for_order_number_in_feed(ORDER_IN_PROGRESS_ITEM, order_number_feed, timeout)
        
        except TimeoutException:
            return None
        
    
    @allure.step("Ожидание появления номера в списке")
    def wait_for_order_number_in_feed(self, locator,order_number_feed: str, timeout=15) -> str:

        def _check_numbers(driver):
            elements = self.find_elements(locator)
            for el in elements:
                text = el.text.strip()
                if text.isdigit() and text == order_number_feed:
                    return text  
            return False  

        return self.wait_until(_check_numbers, timeout)
        
    
    