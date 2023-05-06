from selenium.webdriver.common.by import By


class ShoppingCart:
    cart = (By.ID, "shopping_cart_container")
    cart_list = (By.CLASS_NAME, "cart_list")
    cart_item = (By.CLASS_NAME, "cart_item")
    remove_cart_button = (By.CLASS_NAME, "btn.btn_secondary.btn_small.cart_button")
    continue_shopping = (By.ID, "continue-shopping")
    checkout = (By.ID, "checkout")