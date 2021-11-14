from .base_page import BasePage
from ui.locators.locators import RegPageLocators


class RegPage(BasePage):
    locators = RegPageLocators()

    def authorization(self, user, password):
        user_field = self.find(self.locators.INPUT_NAME)
        user_field.clear()
        password_field = self.find(self.locators.INPUT_PASSWORD)
        password_field.clear()
        password_field.send_keys(password)
        user_field.send_keys(user)
        self.find(self.locators.AUTHORIZATION_BUTTON).click()
