from selenium.webdriver.common.by import By


class Checkout:
    first_name = (By.ID, "first-name")
    last_name = (By.ID, "last-name")
    postal_code = (By.ID, "postal-code")
    checkout_continue = (By.ID, "continue")
    summary = (By.CLASS_NAME, "summary_info")
    finish = (By.ID, "finish")
    home_button = (By.ID, "back-to-products")