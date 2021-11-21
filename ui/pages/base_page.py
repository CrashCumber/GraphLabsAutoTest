from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from ui.locators.locators import BaseLocators
import json

RETRY_COUNT = 2


class BasePage:
    locators = BaseLocators()

    def __init__(self, driver):
        self.driver = driver
        self.user = 'admin@graphlabs.ru'
        self.password = 'admin'

    def find(self, locator, timeout=None):
        try:
            s = self.wait(timeout).until(EC.presence_of_all_elements_located(locator))
            if len(s) == 1:
                return self.wait(timeout).until(EC.presence_of_element_located(locator))
            return self.wait(timeout).until(EC.presence_of_all_elements_located(locator))
        except:
            assert False, f'Элемента {locator} на странице не обнаружено '

    def click(self, locator, timeout=1):
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

    def drag_and_drop(self, locator_from, locator_to, timeout=1):
        for i in range(RETRY_COUNT):
            try:
                self.find(locator_from)
                element_from = self.wait(timeout).until(EC.element_to_be_clickable(locator_from))
                element_to = self.wait(timeout).until(EC.element_to_be_clickable(locator_to))
                ActionChains(self.driver).drag_and_drop(element_from, element_to).perform()
                return
            except StaleElementReferenceException:
                if i < RETRY_COUNT - 1:
                    pass
        raise

    def scroll_to_element(self, element):
        self.driver.execute_script('arguments[0].scrollIntoView(true);', element)

    def switch_to_alert(self, accept=True):
        if accept:
            self.driver.switch_to.alert.accept()
        else:
            self.driver.switch_to.alert.cancel()

    def switch_to_frame(self, locator, timeout=1):
        self.driver.switch_to.frame(self.wait(timeout).until(EC.presence_of_element_located(locator)))

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 3
        return WebDriverWait(self.driver, timeout=timeout)

    def get_storage(self, key="components"):
        return self.driver.execute_script("return window.sessionStorage.getItem(arguments[0]);", key)

