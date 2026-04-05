from selenium.webdriver.common.by import By

TOTAL_ORDERS_COUNTER = (
    By.XPATH,
    "//p[text()='Выполнено за все время:']/following-sibling::p"
)

TODAY_ORDERS_COUNTER = (
    By.XPATH,
    "//p[text()='Выполнено за сегодня:']/following-sibling::p"
)

ORDER_IN_PROGRESS_ITEM = (
    By.XPATH,
    "//ul[contains(@class,'OrderFeed_orderListReady')]//li"
)
