import time

import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from ui.pages.base_page import BasePage
from ui.pages.module_18_page import Module18Page
from ui.pages.reg_page import RegPage
from ui.pages.main_page import MainPage


@pytest.fixture(scope="function")
def base_page(driver):
    return BasePage(driver)


@pytest.fixture(scope="function")
def reg_page(driver):
    return RegPage(driver)


@pytest.fixture(scope="function")
def main_page(driver):
    return MainPage(driver)


@pytest.fixture(scope="function")
def module18_page(driver):
    return Module18Page(driver)


@pytest.fixture(scope="function")
def auto(driver):
    page = RegPage(driver)
    page.authorization(page.user, page.password)
    return BasePage(page.driver)


@pytest.fixture(scope="function")
def module(driver):
    page = RegPage(driver)
    page.authorization(page.user, page.password)

    base = BasePage(page.driver)
    time.sleep(1)
    base.get_page(Module18Page.URL)
    time.sleep(1)

    m_page = Module18Page(page.driver)
    m_page.switch_to_frame(m_page.locators.FRAME)
    return m_page


@pytest.fixture(scope="function")
def driver(config):
    browser = config["browser"]
    version = config["version"]
    url = config["url"]
    selenoid = config["selenoid"]
    if not selenoid:
        manager = ChromeDriverManager(version=version)
        service = Service(manager.install())
        driver = webdriver.Chrome(service=service)
    else:
        options = ChromeOptions()
        capabilities = {
            "acceptInsecureCerts": True,
            "browserName": "chrome",
            "version": "83.0",
        }
        driver = webdriver.Remote(
            command_executor="http://127.0.0.1:4444/wd/hub",
            options=options,
            desired_capabilities=capabilities,
        )
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()
