import allure
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from ui.locators.locators import BaseLocators

RETRY_COUNT = 2


class BasePage:
    locators = BaseLocators()

    def __init__(self, driver):
        self.driver = driver
        self.user = "admin@graphlabs.ru"
        self.password = "admin"

    def find(self, locator, timeout=10):
        try:
            s = self.wait(timeout).until(EC.presence_of_all_elements_located(locator))
            if len(s) == 1:
                return self.wait(timeout).until(EC.presence_of_element_located(locator))
            return self.wait(timeout).until(
                EC.presence_of_all_elements_located(locator)
            )
        except:
            assert False, f"Element {locator} does not exist."

    @allure.step("Кликнуть по элементу {0}")
    def click(self, locator, timeout=10):
        for i in range(RETRY_COUNT):
            try:
                self.find(locator)
                element = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                element.click()
                return
            except StaleElementReferenceException:
                if i < RETRY_COUNT - 1:
                    pass
        raise

    def drag_and_drop(self, locator_from, locator_to, timeout=10):
        for i in range(RETRY_COUNT):
            try:
                self.find(locator_from)
                element_from = self.wait(timeout).until(
                    EC.element_to_be_clickable(locator_from)
                )
                element_to = self.wait(timeout).until(
                    EC.element_to_be_clickable(locator_to)
                )
                ActionChains(self.driver).drag_and_drop(
                    element_from, element_to
                ).perform()
                return
            except StaleElementReferenceException:
                if i < RETRY_COUNT - 1:
                    pass
        raise

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def close_alert(self, accept=True):
        if accept:
            self.driver.switch_to.alert.accept()
        else:
            self.driver.switch_to.alert.cancel()

    def get_alert(self):
        return self.driver.switch_to.alert

    def switch_to_frame(self, locator, timeout=12):
        self.driver.switch_to.frame(
            self.wait(timeout).until(EC.presence_of_element_located(locator))
        )

    def wait(self, timeout=10):
        return WebDriverWait(self.driver, timeout=timeout)

    def get_page(self, url):
        self.driver.get(url)
