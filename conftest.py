from pathlib import Path

import pytest
from selenium import webdriver

# import pytest
from Pages.Page_Login import LoginPage
from Pages.Page_MenuBar import MenuBarPage
from utility.utilities import getdata


@pytest.fixture(scope="session", autouse=True)
def driver():
    driver_path = Path(__file__).parent.joinpath("resources").joinpath("chromedriver.exe")
    print(f"driver path: {driver_path}")
    driver = webdriver.Chrome(executable_path=driver_path)
    driver.get(getdata("base_url"))
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def login(driver):
    driver.find_element(*LoginPage.user_name).click()
    driver.find_element(*LoginPage.user_name).send_keys(getdata("user1"))
    driver.find_element(*LoginPage.password).click()
    driver.find_element(*LoginPage.password).send_keys(getdata("password"))
    driver.find_element(*LoginPage.login_button).click()


def logout(driver):
    driver.find_element(*MenuBarPage.menu_bar).click()
    driver.find_element(*MenuBarPage.logout).click()
