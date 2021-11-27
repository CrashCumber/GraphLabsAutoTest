from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from .base_page import BasePage
from ui.locators.locators import Module18PageLocators


class Module18Page(BasePage):
    button_colors = ["red", "blue", "grey", "yellow", "brown", "magenta"]
    URL = "http://gl-backend.svtz.ru:5050/module/18/?autotest_mode=HjmqvWTJBu"
    locators = Module18PageLocators()

    def color_edge(self, in_, out, color, timeout=2):
        button = getattr(self.locators, f"{color.upper()}_BUTTON", None)
        if button or color not in self.button_colors:
            self.click_edge(in_, out, timeout)
            self.click(button, timeout)
        else:
            raise AssertionError(f"Button with color {color} does not exist.")

    def click_vertex(self, num, timeout=2):
        vertex = (By.XPATH, self.locators.vertex_path.replace("{}", str(num)))
        self.click(vertex, timeout=timeout)

    def click_edge(self, in_, out, timeout=2):
        edge = (
            By.XPATH,
            self.locators.edge_path.replace("{in}", str(in_)).replace(
                "{out}", str(out)
            ),
        )
        self.click(edge, timeout=timeout)

    def check_answer(self):
        self.click(self.locators.DONE_BUTTON)
        self.close_alert()
        return self.find(self.locators.BALL_INF0)

    def get_edges_parsed(self):
        return [
            (edge.get_attribute("in"), edge.get_attribute("out"))
            for edge in self.find(self.locators.EDGES)
        ]

    def move_vertex(self, num, xoffset=100, yoffset=50):
        vertex = (By.XPATH, self.locators.vertex_path.replace("{}", str(num)))
        ActionChains(self.driver).drag_and_drop_by_offset(
            self.find(vertex), xoffset, yoffset
        ).perform()

    def squash_vertex(self, from_, to):
        from_vertex = (By.XPATH, self.locators.vertex_path.replace("{}", str(from_)))
        to_vertex = (By.XPATH, self.locators.vertex_path.replace("{}", str(to)))
        self.drag_and_drop(from_vertex, to_vertex)

    def color_css(self, edges=None, color="red", timeout=2):
        for in_, out in edges:
            self.color_edge(in_, out, color, timeout)

    def get_first_step_success(self):
        self.click_vertex(1)
        self.click_vertex(2)
        self.click_vertex(3)

        color = "red"
        self.move_vertex(9, -50, 0)
        self.color_edge(9, 10, color)
        self.color_edge(10, 8, color)
        self.color_edge(8, 9, color)

        color = "blue"
        self.move_vertex(5, -50, 80)
        self.color_edge(4, 5, color)
        self.color_edge(6, 4, color)
        self.color_edge(5, 6, color)
        self.color_edge(7, 6, color)
        self.color_edge(5, 7, color)

    def get_first_step_fail(self):
        self.click_vertex(2)
        self.click_vertex(3)

        color = "red"
        self.move_vertex(9, -50, 0)
        self.color_edge(8, 9, color)

        color = "blue"
        self.move_vertex(5, -50, 80)
        self.color_edge(4, 5, color)
        self.color_edge(5, 7, color)

    def get_second_step_fail(self):
        self.get_first_step_success()
        self.check_answer()
        self.squash_vertex(10, 8)
        self.squash_vertex(9, 8)
        self.squash_vertex(7, 8)

    def get_second_step_success(self):
        self.get_first_step_success()
        self.check_answer()
        self.squash_vertex(10, 8)
        self.squash_vertex(9, 8)

        self.squash_vertex(7, 6)
        self.squash_vertex(5, 6)
        self.squash_vertex(4, 6)
