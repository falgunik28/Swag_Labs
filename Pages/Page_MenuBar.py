from selenium.webdriver.common.by import By


class MenuBarPage:
    menu_bar = (By.ID, "react-burger-menu-btn")
    menu_list = (By.CSS_SELECTOR, ".bm-item-list>a")
    all_inventory_items = (By.ID, "inventory_sidebar_link")
    about = (By.ID, "about_sidebar_link")
    logout = (By.ID, "logout_sidebar_link")
    app_reset = (By.ID, "reset_sidebar_link")
    close_button = (By.ID, "react-burger-cross-btn")