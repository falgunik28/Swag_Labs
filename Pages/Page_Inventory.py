from selenium.webdriver.common.by import By


class InventoryPage:
    filter_button = (By.CLASS_NAME, "product_sort_container")
    inventory_item = (By.CLASS_NAME, "inventory_item")
    bag_pack_add = (By.ID, "add-to-cart-sauce-labs-backpack")
    shoppingcart = (By.ID, "shopping_cart_container")
    bag_pack_remove = (By.ID, "remove-sauce-labs-backpack")
    item_description = (By.CSS_SELECTOR, ".inventory_item_description")
    item_price = (By.CSS_SELECTOR, ".inventory_item_price")
    add_to_cart_button = (By.CSS_SELECTOR, "button.btn.btn_primary.btn_small.btn_inventory")
    item_name = (By.CSS_SELECTOR, ".inventory_item_name")
    bag_pack_detail = (By.CSS_SELECTOR, "#item_4_title_link")
    back_to_products_btn = (By.ID, "back-to-products")
    remove_button = (By.CSS_SELECTOR, "button.btn.btn_secondary.btn_small.btn_inventory")
