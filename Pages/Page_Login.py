from selenium.webdriver.common.by import By


class LoginPage:
    user_name = (By.ID, "user-name")
    password = (By.ID, "password")
    login_button = (By.ID, "login-button")
    product = (By.CLASS_NAME, "title")
    error_msg = (By.CSS_SELECTOR, ".error-message-container.error")
    error_close_btn = (By.CLASS_NAME, "error-button")













