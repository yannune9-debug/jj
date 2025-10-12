from pages.base_page import BasePage
from utils.config_reader import Config


class SignInPage(BasePage):
    SIGN_IN_BUTTON_MAIN_PAGE = "//a[@class='login']"
    EMAIL_ADDRESS_INPUT = "//input[@id='email']"
    PWD_INPUT = "//input[@id='passwd']"
    SIGN_IN_BUTTON = "//button[@name='SubmitLogin']"
    FAILED_LOGIN =  '//div/p["There is 1 error"]/../ol/li'
    
    def __init__(self, page):
        super().__init__(page)
        self.signin_button_main = page.locator(self.SIGN_IN_BUTTON_MAIN_PAGE)
        self.emailaddress_input = page.locator(self.EMAIL_ADDRESS_INPUT)
        self.pwd_input = page.locator(self.PWD_INPUT)
        self.signin_button = page.locator(self.SIGN_IN_BUTTON)
        self.find_error_message = page.locator(self.FAILED_LOGIN)
       
    def signin(self, email: str, pwd: str):
        self.navigate()
        self.signin_button_main.click()
        self.emailaddress_input.fill(email)
        self.pwd_input.fill(pwd)
        self.signin_button.click()
        
    def get_error_message(self):
        return self.find_error_message.text_content().strip()