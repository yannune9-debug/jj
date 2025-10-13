import pytest
from pages.sign_in_page import SignInPage
from factories.login_factory import create_login_data
import allure

@pytest.mark.parametrize("login_data", [
    #create_login_data({"isValidEmail": True, "isValidPWD": True}),
    create_login_data({"isInValidEmail": True, "isInValidPWD": True}),
    #create_login_data({"isValidEmail": True, "isInValidPWD": True}),
])

@pytest.mark.parametrize("login_data", [
    #create_login_data({"isValidEmail": True, "isValidPWD": True}),
    create_login_data({"isInValidEmail": True, "isInValidPWD": True}),
    #create_login_data({"isValidEmail": True, "isInValidPWD": True}),
])



@allure.title("Login with valid credentials")
@allure.description("This test verifies that the user can log in with valid credentials.")
@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Login")
@allure.story("Positive login flow") 
def test_signin(page, login_data):
    signin_page = SignInPage(page)
    signin_page.signin(login_data["email"], login_data["pwd"])
   
    if login_data.get("isValidEmail") and login_data.get("isValidPassword"):
        assert page.url.endswith("controller=my-account")
    
    else:
        assert signin_page.get_error_message() == "Invalid password1."  

   