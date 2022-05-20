import time

import allure
import pytest
from selenium.webdriver.common.by import By

from tests.base_ui import BaseCase


@pytest.mark.UI_MODULE_18
@pytest.mark.parametrize(
    "browser", ("Firefox", "Safari", "Chrome", "Opera", "Edge")
)
@allure.epic("Проверка модуля построения компонент сильной связности")
class TestUIModule18Page(BaseCase):
    ...


@allure.story("Проверка кликабельности элементов")
@pytest.mark.CLICKABILITY
class TestElementsClickability(TestUIModule18Page):
    @allure.title("Проверка работоспособности кнопки 'Готово' - {browser}")
    def test_done_button(self, auto, browser):
        self.base_page = auto
        self.main_page.click(self.main_page.locators.MODULE_CSS_BUTTON)
        time.sleep(10)
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

    @allure.title("Проверка работоспособности кнопки 'Помощь' - {browser}")
    def test_help_button(self, auto, browser):
        self.base_page = auto
        self.main_page.click(self.main_page.locators.MODULE_CSS_BUTTON)
        time.sleep(10)
        self.module18_page.switch_to_frame(self.module18_page.locators.FRAME)

        self.module18_page.click(self.module18_page.locators.HELP_BUTTON)
        info = self.module18_page.find(self.module18_page.locators.HELP_INFO)
        assert info.text == (
            "Для раскарски ребер можно воспользоваться 7 цветами: Для окраски ребра в зеленый цвет щелкните по ребру\n"
            " Для окраски ребра в другие цвет щелкните по ребру, а затем по соответствующей кнопке\n"
            " Гарантируется, что циклов не больше 7(по числу цветов)."
        )

    @pytest.mark.parametrize(
        "color", ("red", "blue", "grey", "yellow", "brown", "magenta")
    )
    @allure.title("Проверка работоспособности кнопки смены цвета ребра в {color} - {browser}")
    def test_change_color_edge_button(self, auto, color, browser):
        self.base_page = auto
        self.main_page.click(self.main_page.locators.MODULE_CSS_BUTTON)
        time.sleep(10)
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

    @allure.title("Проверка возможности смены цвета вершины при нажатии на нее - {browser}")
    def test_change_color_vertex(self, auto, browser):
        self.base_page = auto
        self.main_page.click(self.main_page.locators.MODULE_CSS_BUTTON)
        time.sleep(10)
        self.module18_page.switch_to_frame(self.module18_page.locators.FRAME)

        vertex = (By.XPATH, self.module18_page.locators.vertex_path.replace("{}", "1"))
        time.sleep(7)
        self.module18_page.click(vertex, timeout=2)
        assert "fill: rgb(255, 0, 0);" in self.module18_page.find(vertex).get_attribute(
            "style"
        )

        self.module18_page.click(vertex)
        assert "fill: rgb(238, 238, 238);" in self.module18_page.find(
            vertex
        ).get_attribute("style")

    @allure.title("Проверка возможности смены цвета ребра при нажатии на него - {browser}")
    def test_change_color_edge(self, auto, browser):
        self.base_page = auto
        self.main_page.click(self.main_page.locators.MODULE_CSS_BUTTON)
        time.sleep(10)
        self.module18_page.switch_to_frame(self.module18_page.locators.FRAME)

        edge = (
            By.XPATH,
            self.module18_page.locators.edge_path.replace("{in}", "8").replace(
                "{out}", "1"
            ),
        )
        self.module18_page.click(edge)
        assert "stroke: green;" in self.module18_page.find(edge).get_attribute("style")


@pytest.mark.DISPLAYED
@allure.story("Проверка отображения элементов")
class TestElementsDisplayed(TestUIModule18Page):
    @allure.title("Проверка отображения всех требуемых элементов - {browser}")
    def test_displayed_elements(self, auto, browser):
        self.base_page = auto
        self.main_page.click(self.main_page.locators.MODULE_CSS_BUTTON)
        time.sleep(10)
        self.module18_page.switch_to_frame(self.module18_page.locators.FRAME)

        self.module18_page.find(self.module18_page.locators.BALL_INF0).is_displayed()
        self.module18_page.find(self.module18_page.locators.DONE_BUTTON).is_displayed()
        self.module18_page.find(self.module18_page.locators.TASK_INFO).is_displayed()
        self.module18_page.find(self.module18_page.locators.GRAPH).is_displayed()
        self.module18_page.find(self.module18_page.locators.HELP_BUTTON).is_displayed()
        self.module18_page.find(self.module18_page.locators.BUTTONS)

    @allure.title("Проверка текста задания - {browser}")
    def test_displayed_task_info_text(self, auto, browser):
        self.base_page = auto
        self.main_page.click(self.main_page.locators.MODULE_CSS_BUTTON)
        time.sleep(10)
        self.module18_page.switch_to_frame(self.module18_page.locators.FRAME)

        task = self.module18_page.find(self.module18_page.locators.TASK_INFO)
        assert (
            "Цель: Найти компоненты сильной связности с помощь циклового метода"
            in task.text
        )


@allure.story(
    "Проверка корректности подсчета оценки при неверном выполнении лабораторной работы и отображения соответствующих сообщения"
)
@pytest.mark.LR_WORK_INCORRECT
class TestLRWorkWithIncorrectAnswer(TestUIModule18Page):
    @allure.title(
        "Выделение только КСС, состоящих из одной вершины. Отсутствие выделения циклов, образующих КСС - {browser}"
    )
    def test_first_step_error_invalid_highlight_no_cycles(self, module, browser):
        self.module18_page = module

        self.module18_page.click_vertex(1)
        self.module18_page.click_vertex(2)
        self.module18_page.click_vertex(3)

        ball = self.module18_page.check_answer()
        assert ball.text == "87"

    @allure.title(
        "Выделение только циклов, образующих КСС. Отсутствие выделения единичных КСС - {browser}"
    )
    def test_first_step_error_invalid_highlight_no_vertices(self, module, browser):
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

    @allure.title("Выделение вершины, которая входит в цикл, как единичную КСС - {browser}")
    def test_first_step_error_invalid_highlight_one_vertex(self, module, browser):
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

    @allure.title("Неверное выделение циклов, образующих КСС - {browser}")
    def test_first_step_error_invalid_highlight_css(self, module, browser):
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

    @allure.title("Выделение ребра, которое не принадлежит ни одному циклу - {browser}")
    def test_first_step_error_invalid_highlight_one_edge(self, module, browser):
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

    @allure.title(
        "Выделение не всех присутствующих в графе вершин-стоков и вершин-истоков - {browser}"
    )
    def test_first_step_error_invalid_highlight_not_all_single_vertices(self, module, browser):
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

    @allure.title("Неверное выделение КСС три раза подряд - {browser}")
    def test_first_step_total_fail(self, module, browser):
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

    @allure.title("Неверное выделение конденсата - {browser}")
    def test_second_step_fail(self, module, browser):
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

    @allure.title(
        "Неверное построении конденсата на втором этапе при одной истраченной попытке на первом этапе - {browser}"
    )
    def test_second_step_fail_after_one_first_fail(self, module, browser):
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


@pytest.mark.LR_WORK_CORRECT
@allure.story(
    "Проверка корректности подсчета оценки при верном выполнении лабораторной работы и отображения соответствующих сообщения - {browser}"
)
class TestLRWorkWithCorrectAnswer(TestUIModule18Page):
    @allure.title("Верное выделение КСС на первом этапе")
    def test_first_step_success(self, module, browser):
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

    @allure.title("Верное построение конденсата на втором этапе - {browser}")
    def test_second_step_success(self, module, browser):
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

    @allure.title("Верное построение КСС со второго раза на первом этапе - {browser}")
    def test_second_step_success_after_one_first_fail(self, module, browser):
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
