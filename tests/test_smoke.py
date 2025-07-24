import os
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.mark.smoke
def test_tc015_smoke_login_add_item(driver, base_url):
    username = os.getenv("USER", "standard_user")
    password = os.getenv("PASS", "secret_sauce")

    login = LoginPage(driver, base_url)
    login.open()
    login.login(username, password)

    inventory = InventoryPage(driver)
    assert inventory.is_loaded(), "Inventory page didn't load"

    inventory.add_backpack()
    assert inventory.cart_count() == 1, "Cart count is not 1"
