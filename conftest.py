from pathlib import Path

import pytest
from selenium import webdriver

# import pytest
from Pages.Page_Login import LoginPage
from Pages.Page_MenuBar import MenuBarPage
from utility.utilities import getdata
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="function")
def driver():
    driver_path = str(Path(__file__).parent.joinpath("resources").joinpath("chromedriver.exe"))
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service)
    driver.get(getdata("base_url"))
    driver.maximize_window()
    yield driver
    # app_reset(driver)
    driver.quit()





def app_reset(driver):
    driver.find_element(*MenuBarPage.menu_list).click()
    driver.find_element(*MenuBarPage.app_reset).click()
    driver.find_element(*MenuBarPage.logout).click()
    driver.find_element(*MenuBarPage.close_button).click()

