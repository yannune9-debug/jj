from pages.base_page import BasePage
from pages.sign_in_page import SignInPage
from pages.address_page import Address
from utils.config_reader import Config
from factories.login_factory import create_login_data
import os
import json
import pytest




@pytest.fixture
def load_address_data(scope="function"):
    fixture_path= "./fixtures/address_fixture.json"
    with open(fixture_path, "r") as f:
        address_data = json.load(f)
        
        return address_data
    
    
@pytest.fixture
def create_and_cleanup_address(page, load_address_data, scope="function"):
    print("🔸 Setup: logging in and navigating")
    sign_in_page = SignInPage(page)
    sign_in_page.navigate()
    login_data = create_login_data()
    sign_in_page.signin(login_data["email"], login_data["pwd"])
    print(load_address_data) 
    address_page = Address(page)  

    yield address_page

    print("🔹 Cleanup: deleting address...")
    page.wait_for_timeout(2000)
    address_page.delete_existing_address()
    print("✅ Address delete action triggered")


def test_address(page, load_address_data, create_and_cleanup_address):
    address_page = create_and_cleanup_address
    address_page.navigate_to_my_addresses()
    print(address_page.no_address_available_info_visible())
    if address_page.no_address_available_info_visible():
        address_page.add_new_address()
        address_page.fill_out_address(load_address_data["firstName"], load_address_data["lastName"],load_address_data["address"],
                                    load_address_data["city"],load_address_data["state"],load_address_data["country"],
                                    load_address_data["mobile"],load_address_data["zip"],load_address_data["title"])
        
    assert address_page.address_title.text_content() == load_address_data["title"]
    
def test_address_1(page, load_address_data, create_and_cleanup_address):
    address_page = create_and_cleanup_address
    address_page.navigate_to_my_addresses()
    print(address_page.no_address_available_info_visible())
    if address_page.no_address_available_info_visible():
        address_page.add_new_address()
        address_page.fill_out_address(load_address_data["firstName"], load_address_data["lastName"],load_address_data["address"],
                                    load_address_data["city"],load_address_data["state"],load_address_data["country"],
                                    load_address_data["mobile"],load_address_data["zip"],load_address_data["title"])
        
    assert address_page.address_title.text_content() == load_address_data["title"]
 
        

