import allure

from .base_page import BasePage
from ui.locators.locators import RegPageLocators


class RegPage(BasePage):
    locators = RegPageLocators()

    @allure.step("Авторизоваться в системе")
    def authorization(self, user, password):
        self.click(self.locators.ENTER_BUTTON)

        user_field = self.find(self.locators.INPUT_NAME)
        user_field.clear()
        user_field.send_keys(user)

        password_field = self.find(self.locators.INPUT_PASSWORD)
        password_field.clear()
        password_field.send_keys(password)

        self.find(self.locators.AUTHORIZATION_BUTTON).click()
