from pages.base_page import BasePage
from utils.config_reader import Config

class Address(BasePage):
    MY_ADDRESS_BUTTON = '//a[@title="Addresses"]'
    NO_ADDRESS_PARAGRAPH = '//p[contains(text(), "No addresses are available.")]'
    FNAME_FIELD = "//input[@name='firstname']"
    LNAME_FIELD = "//input[@name='lastname']"
    ADDRESS_FIELD = "//input[@name='address1']"
    CITY_FIELD = "//input[@name='city']"
    STATE_DROPDOWN = '//select[@name="id_state"]'
    ZIP = '//input[@name="postcode"]'
    MOBILE = '//input[@name="phone_mobile"]'
    TITLE = '//input[@name="alias"]'
    SAVE_BUTTON = '//button[@id="submitAddress"]'
    ADD_NEW_ADDRESS_BUTTON = '//a[@title="Add an address"]'
    DELETE_ADDRESS_BUTTON= '//a[@title="Delete"]'
    ADDRESS_TITLE = '//h3[@class="page-subheading"]'
    
    def __init__(self, page):
        super().__init__(page)
        
        self.my_address_button = page.locator(self.MY_ADDRESS_BUTTON)
        self.no_address_paragraph = page.locator(self.NO_ADDRESS_PARAGRAPH)
        self.fname_field = page.locator(self.FNAME_FIELD)
        self.lname_field = page.locator(self.LNAME_FIELD)
        self.address_field = page.locator(self.ADDRESS_FIELD)
        self.city_field = page.locator(self.CITY_FIELD)
        self.state_dropdown = page.locator(self.STATE_DROPDOWN)
        self.zip = page.locator(self.ZIP)
        self.mobile = page.locator(self.MOBILE)
        self.title = page.locator(self.TITLE)
        44444444
        sssssssssssssssssssssssss
        self.save_button = page.locator(self.SAVE_BUTTON) 
        self.add_new_address_button = page.locator(self.ADD_NEW_ADDRESS_BUTTON)
        self.delete_address_button = page.locator(self.DELETE_ADDRESS_BUTTON)
        self.address_title = page.locator(self.ADDRESS_TITLE)
        
    def navigate_to_my_addresses(self):
        self.my_address_button.click()    
        
    def fill_out_address(self, firstName: str, lastName: str, 
                         address: str, city: str, state: str, country: str,
                         mobile: str, zip: str, title: str):
        self.fname_field.fill(firstName) 
        self.lname_field.fill(lastName)   
        self.address_field.fill(address)
        self.city_field.fill(city)
        self.state_dropdown.select_option(state)
        self.zip.fill(zip)
        self.mobile.fill(mobile)
        self.title.fill(title)
        self.save_button.click()
        
    def add_new_address(self):
        self.add_new_address_button.click()    
        
        
    def is_add_new_address_button_visible(self):
        return self.my_address_button.is_visible()
    
    def no_address_available_info_visible(self):
        try:
            self.no_address_paragraph.wait_for(state="visible")
            return True
        except:
            return False
    
    def delete_existing_address(self):
        self.page.once("dialog", lambda dialog: dialog.accept())   
        self.delete_address_button.wait_for(state="visible")
        self.delete_address_button.click()  
          
        
           
