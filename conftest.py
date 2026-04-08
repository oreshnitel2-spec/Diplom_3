import time

import pytest
from selenium import webdriver
from urls import BASE_URL, CREATE_USER, DELETE_USER
import allure 
from faker import Faker
import requests



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

fake = Faker()
@pytest.fixture
def user():
    email = f"{fake.first_name().lower()}{int(time.time()*1000)}@example.com"
    password = "Pass@!"
    name = fake.first_name()
    with allure.step(f"Создание тестового пользователя: {email}"):
        response = requests.post(
        CREATE_USER,
        json={"email": email, "password": password, "name": name},
        headers={"Content-Type": "application/json"})
   
    access_token = response.json().get("accessToken")
    yield {
        "email": email,
        "password": password,
        "token": access_token
    }
    with allure.step(f"Удаление тестового пользователя: {email}"):
        requests.delete(
        DELETE_USER,
        headers={"Authorization": access_token})
