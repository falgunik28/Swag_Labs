from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.Page_MenuBar import MenuBarPage
from Pages.Page_Inventory import InventoryPage
from utility.utilities import getdata


def test_menu(driver, login):
    driver.find_element(*MenuBarPage.menu_bar).click()
    menu_options = []
    elements = driver.find_elements(*MenuBarPage.menu_list)
    WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located(MenuBarPage.menu_list))
    for element in elements:
        menu_options.append(element.text)
    assert len(menu_options) == 4, "All 4 options are not available"
    assert menu_options == getdata("menu-items"), "Expected menu options are not available"


def test_add_to_cart(driver, login):
    driver.find_element(*InventoryPage.bag_pack_add).click()
    count = driver.find_element(*InventoryPage.shoppingcart).text
    assert int(count) == 1, "After adding item, cart doesn't show correct number"


def test_remove_from_cart(driver, login):
    driver.find_element(*InventoryPage.bag_pack_add).click()
    count = driver.find_element(*InventoryPage.shoppingcart).text
    assert count == '1', "After adding item, cart doesn't show correct number"
    driver.find_element(*InventoryPage.bag_pack_remove).click()
    new_count = driver.find_element(*InventoryPage.shoppingcart).text
    assert new_count == '', "After removing item, cart doesn't show correct number"


def test_product_details(driver, login):
    items = driver.find_elements(*InventoryPage.inventory_item)
    for item in items:
        item_name = item.find_element(*InventoryPage.item_name).text
        assert item_name != '', "Item name is missing"
        item_desc = item.find_element(*InventoryPage.item_description).text
        assert item_desc != '', "Item description is missing"
        item_price = item.find_element(*InventoryPage.item_price).text
        assert item_price != '', "Item price is missing"
        assert item.find_element(*InventoryPage.add_to_cart_button).is_displayed(), "Add to cart is not present"
        item.find_element(*InventoryPage.add_to_cart_button).click()
        assert item.find_element(*InventoryPage.remove_button).is_displayed(), "Remove button is not present"


def test_product_detail_page(driver, login):
    driver.find_element(*InventoryPage.bag_pack_detail).click()
    assert driver.find_element(*InventoryPage.back_to_products_btn).is_displayed(), "Backtoproduct btn is not available"
    assert driver.find_element(*InventoryPage.bag_pack_add).is_displayed(), "Add to cart button is not available"
    driver.find_element(*InventoryPage.bag_pack_add).click()
    assert driver.find_element(*InventoryPage.bag_pack_remove).is_displayed(), "Remove button is not available"

def test_1():
    pass