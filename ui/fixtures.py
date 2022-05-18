import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxOptions, FirefoxProfile
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.opera.options import Options as OperaOptions
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
    time.sleep(10)
    return BasePage(page.driver)


@pytest.fixture(scope="function")
def module(driver):
    page = RegPage(driver)
    page.authorization(page.user, page.password)

    base = BasePage(page.driver)
    time.sleep(10)
    base.get_page(Module18Page.URL)
    time.sleep(10)

    m_page = Module18Page(page.driver)
    time.sleep(5)
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
        kwargs = {
            "command_executor": "http://localhost:4444/wd/hub" #selenoid
        }
        options_dict = {
            "chrome": ChromeOptions,
            "firefox": FirefoxOptions,
            "opera": OperaOptions,
        }
        if browser in options_dict:
            opt = options_dict[browser]()
            kwargs["options"] = opt

        capabilities = {
            "acceptInsecureCerts": True,
            "browserName": browser,
        }
        if browser == "opera":
            capabilities["operaOptions"] = {"binary": "/usr/bin/opera"}
            kwargs["options"].add_experimental_option('w3c', False)

        kwargs["desired_capabilities"] = capabilities

        driver = webdriver.Remote(**kwargs)

    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()
