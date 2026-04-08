from locators.base_page_locators import PERSONAL_ACCOUNT_BUTTON
from pages.base_page import BasePage
from locators.login_page_locators import EMAIL_INPUT, PASSWORD_INPUT, LOGIN_BUTTON
import allure

class LoginPage(BasePage):

    @allure.step("Ввод email в поле для логина")
    
    @allure.step("Клик по кнопке Личный Кабинет")
    def click_personal_account_button(self):
        self.click(PERSONAL_ACCOUNT_BUTTON)
        
    def enter_email(self, email: str):
        self.send_keys(EMAIL_INPUT, email)

    @allure.step("Ввод пароля в поле для пароля")
    def enter_password(self, password: str):
        self.send_keys(PASSWORD_INPUT, password)

    @allure.step("Клик по кнопке Войти")
    def click_login_button(self):
        self.click(LOGIN_BUTTON)

    @allure.step("Авторизация пользователя")
    def login(self, email: str, password: str):
        self.click_personal_account_button()  
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()