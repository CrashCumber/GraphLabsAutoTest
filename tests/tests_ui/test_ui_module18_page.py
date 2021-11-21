import json
import time

import pytest
from selenium.webdriver.common.by import By

from tests.base_ui import BaseCase


class TestUIModule18Page(BaseCase):
    ...


class TestButtons(TestUIModule18Page):

    @pytest.mark.skip
    def test_done_button(self, auto):
        self.base_page = auto
        self.main_page.click(self.main_page.locators.MODULE_CSS_BUTTON)
        self.module18_page.switch_to_frame(self.module18_page.locators.FRAME)

        ball = self.base_page.find(self.module18_page.locators.BALL_INF0)
        assert ball.text == "100"
        self.base_page.click(self.module18_page.locators.DONE_BUTTON)
        time.sleep(1)
        self.base_page.switch_to_alert()
        ball = self.base_page.find(self.module18_page.locators.BALL_INF0)
        assert ball.text == "87"

    @pytest.mark.skip
    def test_help_button(self, auto):
        self.base_page = auto
        self.main_page.click(self.main_page.locators.MODULE_CSS_BUTTON)
        self.module18_page.switch_to_frame(self.module18_page.locators.FRAME)

        self.base_page.click(self.module18_page.locators.HELP_BUTTON)
        info = self.base_page.find(self.module18_page.locators.HELP_INFO)
        assert info.text == (
            "Для раскарски ребер можно воспользоваться 7 цветами: Для окраски ребра в зеленый цвет щелкните по ребру\n"
            " Для окраски ребра в другие цвет щелкните по ребру, а затем по соответствующей кнопке\n"
            " Гарантируется, что циклов не больше 7(по числу цветов)."
        )

    @pytest.mark.skip
    @pytest.mark.parametrize("color", ("red", "blue", "grey", "yellow", "brown", "magenta"))
    def test_change_color_edge(self, auto, color):
        self.base_page = auto
        self.main_page.click(self.main_page.locators.MODULE_CSS_BUTTON)
        self.module18_page.switch_to_frame(self.module18_page.locators.FRAME)

        edge = (By.XPATH, self.module18_page.locators.edge_path.replace("{in}", "8").replace("{out}", "1"))

        self.module18_page.click(edge)
        button = getattr(self.module18_page.locators, f"{color.upper()}_BUTTON", None)
        if button:
            self.module18_page.click(button)

            if color == "brown":
                color = "sienna"
            if color == "magenta":
                color = "fuchsia"
            if color == "grey":
                color = "silver"
            assert f"stroke: {color};" in self.module18_page.find(edge).get_attribute("style")

    @pytest.mark.skip
    def test_change_color_vertex(self, auto):
        self.base_page = auto
        self.main_page.click(self.main_page.locators.MODULE_CSS_BUTTON)
        self.module18_page.switch_to_frame(self.module18_page.locators.FRAME)

        vertex = (By.XPATH, self.module18_page.locators.vertex_path.replace("{}", "1"))
        time.sleep(2)
        self.module18_page.click(vertex, timeout=2)
        assert "fill: rgb(255, 0, 0);" in self.module18_page.find(vertex).get_attribute("style")

        self.module18_page.click(vertex)
        assert "fill: rgb(238, 238, 238);" in self.module18_page.find(vertex).get_attribute("style")


class TestDisplayedElements(TestUIModule18Page):
    @pytest.mark.skip
    def test_displayed_elements(self, auto):
        self.base_page = auto
        self.main_page.click(self.main_page.locators.MODULE_CSS_BUTTON)
        self.module18_page.switch_to_frame(self.module18_page.locators.FRAME)

        self.module18_page.find(self.module18_page.locators.BALL_INF0).is_displayed()
        self.module18_page.find(self.module18_page.locators.DONE_BUTTON).is_displayed()
        self.module18_page.find(self.module18_page.locators.TASK_INFO).is_displayed()
        self.module18_page.find(self.module18_page.locators.GRAPH).is_displayed()
        self.module18_page.find(self.module18_page.locators.HELP_BUTTON).is_displayed()
        self.module18_page.find(self.module18_page.locators.BUTTONS)


class TestLRWork(TestUIModule18Page):
    # @pytest.mark.skip
    def test_first_step_error(self):
        # self.base_page = auto
        # self.main_page.click(self.main_page.locators.MODULE_CSS_BUTTON)
        # self.module18_page.switch_to_frame(self.module18_page.locators.FRAME)

        components = json.loads(self.base_page.get_storage())
        button_colors = ["red", "blue", "grey", "yellow", "brown", "magenta"]
        edge_path = '//*[name()="svg"]/*[@in="{in}"]'
        for cmp in components:
            if len(cmp) == 1:
                vertex = (By.XPATH, self.module18_page.locators.vertex_path.replace("{}", cmp[0]))
                time.sleep(2)
                self.module18_page.click(vertex, timeout=2)
            else:
                color = button_colors.pop(0)
                button = getattr(self.module18_page.locators, f"{color.upper()}_BUTTON", None)
                for i in range(1, len(cmp)):
                    edge = (By.XPATH, self.module18_page.locators.edge_path.replace("{in}", "8"))

                    self.module18_page.click(edge)
                    time.sleep(2)
                    self.module18_page.click(button)
