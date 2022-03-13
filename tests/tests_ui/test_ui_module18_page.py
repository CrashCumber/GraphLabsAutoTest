import time

import allure
import pytest
from selenium.webdriver.common.by import By

from tests.base_ui import BaseCase


@pytest.mark.UI_MODULE_18
class TestUIModule18Page(BaseCase):
    ...


@pytest.mark.CLICK
class TestElementsClickability(TestUIModule18Page):
    @allure.title("Проверка работоспособности кнопки 'Готово'")
    def test_done_button(self, auto):
        self.base_page = auto
        self.main_page.click(self.main_page.locators.MODULE_CSS_BUTTON)
        time.sleep(1)
        self.module18_page.switch_to_frame(self.module18_page.locators.FRAME)

        ball = self.module18_page.find(self.module18_page.locators.BALL_INF0)
        assert ball.text == "100"

        ball = self.module18_page.check_answer()
        assert ball.text == "87"

        ball = self.module18_page.check_answer()
        assert ball.text == "74"

        ball = self.module18_page.check_answer()
        assert ball.text == "61"

        ball = self.module18_page.check_answer()
        assert ball.text == "0"

        self.module18_page.click(self.module18_page.locators.DONE_BUTTON)
        ball = self.module18_page.find(self.module18_page.locators.BALL_INF0)
        assert ball.text == "0"

    @pytest.mark.skip
    def test_help_button(self, auto):
        self.base_page = auto
        self.main_page.click(self.main_page.locators.MODULE_CSS_BUTTON)
        time.sleep(1)
        self.module18_page.switch_to_frame(self.module18_page.locators.FRAME)

        self.module18_page.click(self.module18_page.locators.HELP_BUTTON)
        info = self.module18_page.find(self.module18_page.locators.HELP_INFO)
        assert info.text == (
            "Для раскарски ребер можно воспользоваться 7 цветами: Для окраски ребра в зеленый цвет щелкните по ребру\n"
            " Для окраски ребра в другие цвет щелкните по ребру, а затем по соответствующей кнопке\n"
            " Гарантируется, что циклов не больше 7(по числу цветов)."
        )

    @pytest.mark.skip
    @pytest.mark.parametrize(
        "color", ("red", "blue", "grey", "yellow", "brown", "magenta")
    )
    def test_change_color_edge_button(self, auto, color):
        self.base_page = auto
        self.main_page.click(self.main_page.locators.MODULE_CSS_BUTTON)
        time.sleep(1)
        self.module18_page.switch_to_frame(self.module18_page.locators.FRAME)

        edge = (
            By.XPATH,
            self.module18_page.locators.edge_path.replace("{in}", "8").replace(
                "{out}", "1"
            ),
        )

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
            assert f"stroke: {color};" in self.module18_page.find(edge).get_attribute(
                "style"
            )

    @pytest.mark.skip
    def test_change_color_vertex(self, auto):
        self.base_page = auto
        self.main_page.click(self.main_page.locators.MODULE_CSS_BUTTON)
        time.sleep(1)
        self.module18_page.switch_to_frame(self.module18_page.locators.FRAME)

        vertex = (By.XPATH, self.module18_page.locators.vertex_path.replace("{}", "1"))
        time.sleep(2)
        self.module18_page.click(vertex, timeout=2)
        assert "fill: rgb(255, 0, 0);" in self.module18_page.find(vertex).get_attribute(
            "style"
        )

        self.module18_page.click(vertex)
        assert "fill: rgb(238, 238, 238);" in self.module18_page.find(
            vertex
        ).get_attribute("style")

    @pytest.mark.skip
    def test_change_color_edge(self, auto):
        self.base_page = auto
        self.main_page.click(self.main_page.locators.MODULE_CSS_BUTTON)
        time.sleep(1)
        self.module18_page.switch_to_frame(self.module18_page.locators.FRAME)

        edge = (
            By.XPATH,
            self.module18_page.locators.edge_path.replace("{in}", "8").replace(
                "{out}", "1"
            ),
        )
        self.module18_page.click(edge)
        assert "stroke: green;" in self.module18_page.find(edge).get_attribute("style")


@pytest.mark.skip
class TestElementsDisplayed(TestUIModule18Page):
    def test_displayed_elements(self, auto):
        self.base_page = auto
        self.main_page.click(self.main_page.locators.MODULE_CSS_BUTTON)
        time.sleep(1)
        self.module18_page.switch_to_frame(self.module18_page.locators.FRAME)

        self.module18_page.find(self.module18_page.locators.BALL_INF0).is_displayed()
        self.module18_page.find(self.module18_page.locators.DONE_BUTTON).is_displayed()
        self.module18_page.find(self.module18_page.locators.TASK_INFO).is_displayed()
        self.module18_page.find(self.module18_page.locators.GRAPH).is_displayed()
        self.module18_page.find(self.module18_page.locators.HELP_BUTTON).is_displayed()
        self.module18_page.find(self.module18_page.locators.BUTTONS)

    def test_displayed_task_info_text(self, auto):
        self.base_page = auto
        self.main_page.click(self.main_page.locators.MODULE_CSS_BUTTON)
        time.sleep(1)
        self.module18_page.switch_to_frame(self.module18_page.locators.FRAME)

        task = self.module18_page.find(self.module18_page.locators.TASK_INFO)
        assert (
            "Цель: Найти компоненты сильной связности с помощь циклового метода"
            in task.text
        )


@pytest.mark.skip
class TestLRWorkWithIncorrectAnswer(TestUIModule18Page):
    def test_first_step_error_invalid_highlight_no_cycles(self, module):
        self.module18_page = module

        self.module18_page.click_vertex(1)
        self.module18_page.click_vertex(2)
        self.module18_page.click_vertex(3)

        ball = self.module18_page.check_answer()
        assert ball.text == "87"

    def test_first_step_error_invalid_highlight_no_vertices(self, module):
        self.module18_page = module

        color = "red"
        self.module18_page.move_vertex(9, -50, 0)
        self.module18_page.color_edge(9, 10, color)
        self.module18_page.color_edge(10, 8, color)
        self.module18_page.color_edge(8, 9, color)

        color = "blue"
        self.module18_page.move_vertex(5, -50, 80)
        self.module18_page.color_edge(4, 5, color)
        self.module18_page.color_edge(6, 4, color)
        self.module18_page.color_edge(5, 6, color)
        self.module18_page.color_edge(7, 6, color)
        self.module18_page.color_edge(5, 7, color)

        ball = self.module18_page.check_answer()
        assert ball.text == "87"

    def test_first_step_error_invalid_highlight_one_vertex(self, module):
        self.module18_page = module

        self.module18_page.click_vertex(1)
        self.module18_page.click_vertex(2)
        self.module18_page.click_vertex(3)
        self.module18_page.click_vertex(7)

        color = "red"
        self.module18_page.move_vertex(9, -50, 0)
        self.module18_page.color_edge(9, 10, color)
        self.module18_page.color_edge(10, 8, color)
        self.module18_page.color_edge(8, 9, color)

        color = "blue"
        self.module18_page.move_vertex(5, -50, 80)
        self.module18_page.color_edge(4, 5, color)
        self.module18_page.color_edge(6, 4, color)
        self.module18_page.color_edge(5, 6, color)

        ball = self.module18_page.check_answer()
        assert ball.text == "87"

    def test_first_step_error_invalid_highlight_css(self, module):
        self.module18_page = module

        self.module18_page.click_vertex(1)
        self.module18_page.click_vertex(2)
        self.module18_page.click_vertex(3)

        color = "red"
        self.module18_page.move_vertex(9, -50, 0)
        self.module18_page.color_edge(9, 10, color)
        self.module18_page.color_edge(10, 8, color)
        self.module18_page.color_edge(8, 9, color)

        self.module18_page.move_vertex(5, -50, 80)
        self.module18_page.color_edge(4, 5, color)
        self.module18_page.color_edge(6, 4, color)
        self.module18_page.color_edge(5, 6, color)
        self.module18_page.color_edge(5, 7, color)
        self.module18_page.color_edge(7, 6, color)

        self.module18_page.color_edge(7, 8, color)  # bad

        ball = self.module18_page.check_answer()
        assert ball.text == "87"

    def test_first_step_error_invalid_highlight_one_edge(self, module):
        self.module18_page = module

        self.module18_page.click_vertex(1)
        self.module18_page.click_vertex(2)
        self.module18_page.click_vertex(3)

        color = "red"
        self.module18_page.move_vertex(9, -50, 0)
        self.module18_page.color_edge(9, 10, color)
        self.module18_page.color_edge(10, 8, color)
        self.module18_page.color_edge(8, 9, color)

        color = "blue"
        self.module18_page.move_vertex(5, -50, 80)
        self.module18_page.color_edge(4, 5, color)
        self.module18_page.color_edge(6, 4, color)
        self.module18_page.color_edge(5, 6, color)
        self.module18_page.color_edge(5, 7, color)
        self.module18_page.color_edge(7, 6, color)

        self.module18_page.color_edge(7, 8, color)  # bad

        ball = self.module18_page.check_answer()
        assert ball.text == "87"

    def test_first_step_error_invalid_highlight_not_all_single_vertices(self, module):
        self.module18_page = module

        self.module18_page.click_vertex(1)

        color = "red"
        self.module18_page.move_vertex(9, -50, 0)
        self.module18_page.color_edge(9, 10, color)
        self.module18_page.color_edge(10, 8, color)
        self.module18_page.color_edge(8, 9, color)

        color = "blue"
        self.module18_page.move_vertex(5, -50, 80)
        self.module18_page.color_edge(4, 5, color)
        self.module18_page.color_edge(6, 4, color)
        self.module18_page.color_edge(5, 6, color)
        self.module18_page.color_edge(7, 6, color)
        self.module18_page.color_edge(5, 7, color)

        ball = self.module18_page.check_answer()
        assert ball.text == "87"
    #
    # def test_first_step_error_some_times(self, module):
    #     self.module18_page = module
    #
    #     self.module18_page.click_vertex(1)
    #     self.module18_page.click_vertex(2)
    #     self.module18_page.click_vertex(3)
    #
    #     color = "red"
    #     self.module18_page.move_vertex(9, -50, 0)
    #     self.module18_page.color_edge(9, 10, color)
    #     self.module18_page.color_edge(10, 8, color)
    #     self.module18_page.color_edge(8, 9, color)
    #
    #     self.module18_page.move_vertex(5, -50, 80)
    #     self.module18_page.color_edge(4, 5, color)
    #     self.module18_page.color_edge(6, 4, color)
    #     self.module18_page.color_edge(5, 6, color)
    #     self.module18_page.color_edge(7, 6, color)
    #     self.module18_page.color_edge(5, 7, color)
    #
    #     ball = self.module18_page.check_answer()
    #     assert ball.text == "87"
    #
    #     color = "blue"
    #     self.module18_page.color_edge(4, 5, color)
    #     self.module18_page.color_edge(6, 4, color)
    #     self.module18_page.color_edge(5, 6, color)
    #     self.module18_page.color_edge(7, 6, color)
    #     self.module18_page.color_edge(5, 7, color)
    #     self.module18_page.color_edge(7, 8, color)
    #
    #     ball = self.module18_page.check_answer()
    #     assert ball.text == "74"
    #
    #     self.module18_page.click_vertex(1)
    #
    #     ball = self.module18_page.check_answer()
    #     assert ball.text == "61"
    #     time.sleep(3)
    #
    #     self.module18_page.click_vertex(1)
    #     self.module18_page.click_edge(7, 8)
    #
    #     ball = self.module18_page.check_answer()
    #     assert ball.text == "61"

    def test_first_step_total_fail(self, module):
        self.module18_page = module

        self.module18_page.click_vertex(1)
        self.module18_page.click_vertex(2)
        self.module18_page.click_vertex(3)

        color = "red"
        self.module18_page.move_vertex(9, -50, 0)
        self.module18_page.color_edge(9, 10, color)
        self.module18_page.color_edge(10, 8, color)
        self.module18_page.color_edge(8, 9, color)

        self.module18_page.move_vertex(5, -50, 80)
        self.module18_page.color_edge(4, 5, color)
        self.module18_page.color_edge(6, 4, color)
        self.module18_page.color_edge(5, 6, color)
        self.module18_page.color_edge(7, 6, color)
        self.module18_page.color_edge(5, 7, color)

        ball = self.module18_page.check_answer()
        assert ball.text == "87"

        color = "blue"
        self.module18_page.color_edge(4, 5, color)
        self.module18_page.color_edge(6, 4, color)
        self.module18_page.color_edge(5, 6, color)
        self.module18_page.color_edge(7, 6, color)
        self.module18_page.color_edge(5, 7, color)
        self.module18_page.color_edge(7, 8, color)

        ball = self.module18_page.check_answer()
        assert ball.text == "74"

        self.module18_page.click_vertex(1)

        ball = self.module18_page.check_answer()
        assert ball.text == "61"

        self.module18_page.click_vertex(1)

        ball = self.module18_page.check_answer()
        assert ball.text == "0"

    def test_second_step_fail(self, module):
        self.module18_page = module
        self.module18_page.get_first_step_success()

        ball = self.module18_page.check_answer()
        assert ball.text == "100"

        self.module18_page.squash_vertex(10, 8)
        self.module18_page.squash_vertex(9, 8)

        self.module18_page.squash_vertex(7, 8)
        self.module18_page.squash_vertex(5, 6)

        ball = self.module18_page.check_answer()
        assert ball.text == "0"

    def test_second_step_fail_after_one_first_fail(self, module):
        self.module18_page = module

        self.module18_page.click_vertex(1)

        color = "red"
        self.module18_page.move_vertex(9, -50, 0)
        self.module18_page.color_edge(9, 10, color)
        self.module18_page.color_edge(10, 8, color)
        self.module18_page.color_edge(8, 9, color)

        color = "blue"
        self.module18_page.move_vertex(5, -50, 80)
        self.module18_page.color_edge(4, 5, color)
        self.module18_page.color_edge(6, 4, color)
        self.module18_page.color_edge(5, 6, color)
        self.module18_page.color_edge(7, 6, color)
        self.module18_page.color_edge(5, 7, color)

        ball = self.module18_page.check_answer()
        assert ball.text == "87"

        self.module18_page.click_vertex(2)
        self.module18_page.click_vertex(3)

        ball = self.module18_page.check_answer()
        assert ball.text == "87"

        self.module18_page.squash_vertex(10, 8)
        self.module18_page.squash_vertex(9, 8)

        self.module18_page.squash_vertex(7, 8)
        self.module18_page.squash_vertex(5, 6)

        ball = self.module18_page.check_answer()
        assert ball.text == "0"


@pytest.mark.skip
class TestLRWorkWithCorrectAnswer(TestUIModule18Page):
    def test_first_step_success(self, module):
        self.module18_page = module

        self.module18_page.click_vertex(1)
        self.module18_page.click_vertex(2)
        self.module18_page.click_vertex(3)

        color = "red"
        self.module18_page.move_vertex(9, -50, 0)
        self.module18_page.color_edge(9, 10, color)
        self.module18_page.color_edge(10, 8, color)
        self.module18_page.color_edge(8, 9, color)

        color = "blue"
        self.module18_page.move_vertex(5, -50, 80)
        self.module18_page.color_edge(4, 5, color)
        self.module18_page.color_edge(6, 4, color)
        self.module18_page.color_edge(5, 6, color)
        self.module18_page.color_edge(7, 6, color)
        self.module18_page.color_edge(5, 7, color)

        ball = self.module18_page.check_answer()
        assert ball.text == "100"

    def test_second_step_success(self, module):
        self.module18_page = module
        self.module18_page.get_first_step_success()

        ball = self.module18_page.check_answer()
        assert ball.text == "100"

        self.module18_page.squash_vertex(10, 8)
        self.module18_page.squash_vertex(9, 8)

        self.module18_page.squash_vertex(7, 6)
        self.module18_page.squash_vertex(5, 6)
        self.module18_page.squash_vertex(4, 6)

        ball = self.module18_page.check_answer()
        assert ball.text == "100"

    def test_second_step_success_after_one_first_fail(self, module):
        self.module18_page = module

        self.module18_page.click_vertex(1)

        color = "red"
        self.module18_page.move_vertex(9, -50, 0)
        self.module18_page.color_edge(9, 10, color)
        self.module18_page.color_edge(10, 8, color)
        self.module18_page.color_edge(8, 9, color)

        color = "blue"
        self.module18_page.move_vertex(5, -50, 80)
        self.module18_page.color_edge(4, 5, color)
        self.module18_page.color_edge(6, 4, color)
        self.module18_page.color_edge(5, 6, color)
        self.module18_page.color_edge(7, 6, color)
        self.module18_page.color_edge(5, 7, color)

        ball = self.module18_page.check_answer()
        assert ball.text == "87"

        self.module18_page.click_vertex(2)
        self.module18_page.click_vertex(3)

        ball = self.module18_page.check_answer()
        assert ball.text == "87"

        self.module18_page.squash_vertex(10, 8)
        self.module18_page.squash_vertex(9, 8)

        self.module18_page.squash_vertex(7, 6)
        self.module18_page.squash_vertex(5, 6)
        self.module18_page.squash_vertex(4, 6)

        ball = self.module18_page.check_answer()
        assert ball.text == "87"

#
# class TestAlerts(TestUIModule18Page):
#     def test_alert_after_first_step_fail(self, module):
#         self.module18_page = module
#         self.module18_page.get_first_step_fail()
#         self.module18_page.click(self.module18_page.locators.DONE_BUTTON)
#         alert = self.module18_page.get_alert()
#         assert alert.text == "Вы ошиблись. Попробуйте еще раз."
#
#     def test_alert_after_first_step_success(self, module):
#         self.module18_page = module
#         self.module18_page.get_first_step_success()
#         self.module18_page.click(self.module18_page.locators.DONE_BUTTON)
#         alert = self.module18_page.get_alert()
#         assert (
#             alert.text
#             == "Вы можете перейти ко второму этапу. Постройте конденсат графа, перетащив вершины."
#         )
#
#     def test_alert_after_second_step_fail(self, module):
#         self.module18_page = module
#         self.module18_page.get_second_step_fail()
#         self.module18_page.click(self.module18_page.locators.DONE_BUTTON)
#         alert = self.module18_page.get_alert()
#         assert alert.text == "Упражнение окончено. Вы допустили слишом много ошибок."
#
#     def test_alert_after_second_step_success(self, module):
#         self.module18_page = module
#         self.module18_page.get_second_step_success()
#         self.module18_page.click(self.module18_page.locators.DONE_BUTTON)
#         alert = self.module18_page.get_alert()
#         assert alert.text == "Поздравляю, вы справились с заданием."
