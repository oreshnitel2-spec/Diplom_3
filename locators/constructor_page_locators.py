from selenium.webdriver.common.by import By

INGREDIENT_MODAL_TITLE = (By.XPATH, "//h2[text()='Детали ингредиента']")
INGREDIENT_MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class,'Modal_modal__close')]")
BURGER_BUN_DROP_AREA = (By.XPATH,"//span[contains(@class,'constructor-element__row')]//span[text()='Перетяните булочку сюда (верх)']")
ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
ORDER_MODAL_CLOSE_BUTTON = (
    By.XPATH,
    "//div[contains(@class,'Modal_modal__')]//button"
)
ORDER_NUMBER = (
    By.XPATH,
    "//div[contains(@class,'Modal_modal__')]//h2"
)

def ingredient_image_by_alt(alt_text: str):
    return (By.XPATH, f"//img[@alt='{alt_text}']")

def ingredient_name_in_modal_by_text(expected_name: str):
    return (By.XPATH, f"//div[contains(@class,'Modal_modal__')]//p[text()='{expected_name}']")

def ingredient_price_in_constructor_by_alt(alt_text: str):
    return (
        By.XPATH,
        f"//span[contains(@class,'constructor-element__row')][.//img[contains(@alt,'{alt_text}')]]//span[contains(@class,'constructor-element__price')]"
    )
