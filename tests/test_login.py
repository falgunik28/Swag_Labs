from Pages.Page_Login import LoginPage
from utility.utilities import getdata


def test_login_successful(driver):

    driver.find_element(*LoginPage.user_name).click()
    driver.find_element(*LoginPage.user_name).send_keys(getdata("user1"))
    driver.find_element(*LoginPage.password).click()
    driver.find_element(*LoginPage.password).send_keys(getdata("password"))
    driver.find_element(*LoginPage.login_button).click()
    product_name = driver.find_element(*LoginPage.product).text
    assert product_name == "Products", "Login is not successful with standard_user"


def test_login_with_wrong_username(driver):
    driver.find_element(*LoginPage.user_name).click()
    driver.find_element(*LoginPage.user_name).send_keys(getdata("wrong_user"))
    driver.find_element(*LoginPage.password).click()
    driver.find_element(*LoginPage.password).send_keys(getdata("wrong_pwd"))
    driver.find_element(*LoginPage.login_button).click()
    error_text = driver.find_element(*LoginPage.error_msg).text
    assert error_text == getdata("Error_wrong_user"), "Logged in with wrong user"


def test_login_with_wrong_pwd(driver):
    driver.find_element(*LoginPage.user_name).click()
    driver.find_element(*LoginPage.user_name).send_keys(getdata("user1"))
    driver.find_element(*LoginPage.password).click()
    driver.find_element(*LoginPage.password).send_keys(getdata("wrong_pwd"))
    driver.find_element(*LoginPage.login_button).click()
    error_text = driver.find_element(*LoginPage.error_msg).text
    assert error_text == getdata("Error_wrong_user"), "Logged in with wrong user"


def test_login_with_locked_user(driver):
    driver.find_element(*LoginPage.user_name).click()
    driver.find_element(*LoginPage.user_name).send_keys(getdata("user2"))
    driver.find_element(*LoginPage.password).click()
    driver.find_element(*LoginPage.password).send_keys(getdata("password"))
    driver.find_element(*LoginPage.login_button).click()
    error_text = driver.find_element(*LoginPage.error_msg).text
    assert error_text == getdata("Error_locked_user"), " Logged in with Locked user"
