
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_page_locators import FEED_TAB, CONSTRUCTOR_TAB, PERSONAL_ACCOUNT_BUTTON


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Получение текущего URL страницы")
    def current_url(self):
        return self.driver.current_url
    
    @allure.step("Поиск элемента")
    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Клик по элементу")
    def click(self, locator):
        self.find_element(locator).click()
        
    @allure.step("Поиск всех элементов")
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)
    
    @allure.step("Клик по вкладке Конструктор")
    def click_constructor_tab(self):
        self.click(CONSTRUCTOR_TAB)

    @allure.step("Ожидание невидимости элемента")
    def wait_until_not_visible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    @allure.step("Отправка текста в элемент")
    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Получение текста элемента")
    def get_text(self, locator):
        return self.find_element(locator).text
    
    @allure.step("Ожидание видимости элемента")
    def wait_for_visibility(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
    
    @allure.step("Ожидание кликабельности элемента")
    def wait_for_clickable(self, locator, timeout=10):
        """Ожидание кликабельности элемента"""
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
    
      
    @allure.step("Клик по элементу через JS")
    def js_click(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)
   

    @allure.step("Ожидание выполнения условия")
    def wait_until(self, condition_function, timeout=10):
        return WebDriverWait(self.driver, timeout).until(condition_function)
    

    @allure.step("Перетаскивание элемента с помощью JS")
    def drag_and_drop_js(self, source, target):

        self.driver.execute_script("""
        const source = arguments[0];
        const target = arguments[1];

        function createEvent(type) {
            const event = new Event(type, { bubbles: true, cancelable: true });
            event.dataTransfer = {
                data: {},
                setData: function(key, value) { this.data[key] = value; },
                getData: function(key) { return this.data[key]; }
            };
            return event;
        }

        const dragStartEvent = createEvent('dragstart');
        source.dispatchEvent(dragStartEvent);

        const dropEvent = createEvent('drop');
        dropEvent.dataTransfer = dragStartEvent.dataTransfer;
        target.dispatchEvent(dropEvent);

        const dragEndEvent = createEvent('dragend');
        dragEndEvent.dataTransfer = dragStartEvent.dataTransfer;
        source.dispatchEvent(dragEndEvent);
        """, source, target)