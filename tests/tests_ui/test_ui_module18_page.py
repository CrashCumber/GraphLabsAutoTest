import time

import pytest
from selenium.webdriver.common.by import By

from tests.base_ui import BaseCase


@pytest.mark.UI
class TestUIModule18Page(BaseCase):

    # def test_displayed(self):
    #     assert self.base_page.find(self.module18_page.locators.BALL_INF0).is_displayed()
    #     assert self.base_page.find(self.module18_page.locators.DONE_BUTTON).is_displayed()
    #     assert self.base_page.find(self.module18_page.locators.TASK_INFO).is_displayed()
    #     assert self.base_page.find(self.module18_page.locators.GRAPH).is_displayed()
    #     assert self.base_page.find(self.module18_page.locators.HELP_BUTTON).is_displayed()
    #     assert self.base_page.find(self.module18_page.locators.BUTTONS).is_displayed()

    # def test_task_displayed(self):
    #     ...
    #
    # def test_ball_displayed(self):
    #     ...
    #
    # def test_button_panel_displayed(self):
    #     ...
    #
    # def test_help_button(self):
    #     ...

    # def test_check_button(self):
    #     ball = self.base_page.find(self.module18_page.locators.BALL_INF0)
    #     assert ball.text == "100"
    #     self.base_page.click(self.module18_page.locators.DONE_BUTTON)
    #     time.sleep(1)
    #     self.base_page.switch_to_alert()
    #     ball = self.base_page.find(self.module18_page.locators.BALL_INF0)
    #     assert ball.text == "87"

    def test_color_button(self):
        edge = self.module18_page.locators.edge_path
        edge = (By.XPATH, edge.replace("{in}", "8").replace("{out}", "1"))
        self.base_page.click(edge)
        time.sleep(2)
        self.base_page.click(self.module18_page.locators.BLUE_BUTTON)


