from selenium.webdriver.common.by import By

from Pages.utilities import Page


class Login(Page):
    Email = (By.ID, 'userName')
    Password = (By.ID, 'password')
    Submit = (By.CSS_SELECTOR, "button[type='submit']")
    Message = (By.XPATH, "//div[@class='ant-message-notice-content']")

    def open_url(self):
        self.open_page("https://staging.careapps.co.uk/auth/login")

    def input_email(self):
        self.input_text(self.Email, "zalam@tulip-tech.com")

    def input_password(self):
        self.input_text(self.Password, "Bangladesh1#")

    def submit(self):
        self.click(self.Submit)

    def assert_login_message(self):
        self.wait_for_element_to_be_present(self.Message)
        self.assert_text("Login is successful", self.Message)
