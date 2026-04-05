import pytest
from selenium import webdriver
from urls import BASE_URL
import allure 

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser_name = request.param
    with allure.step(f"Запуск браузера: {browser_name}"):
        if request.param == "chrome":
            driver = webdriver.Chrome()
        elif request.param == "firefox":
            driver = webdriver.Firefox()
    with allure.step("Открытие главной страницы"):
        driver.get(BASE_URL)
    yield driver
    with allure.step("Закрытие браузера"):
        driver.quit()