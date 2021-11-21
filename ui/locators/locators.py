from selenium.webdriver.common.by import By


class BaseLocators:
    ##  http://gl-backend.svtz.ru:5050/
    ENTER_BUTTON = (By.XPATH,  '//a[text()="Вход"]')


class RegPageLocators(BaseLocators):
    ##  http://gl-backend.svtz.ru:5050/auto
    INPUT_NAME = (By.XPATH, '//input[@name="email"]')
    INPUT_PASSWORD = (By.XPATH, '//input[@name="password"]')
    AUTHORIZATION_BUTTON = (By.XPATH, '//button[text()="Войти"]')
    CREATE_ACCOUNT_BUTTON = (By.PARTIAL_LINK_TEXT, 'Create an account')
    INVALID_DATA_DIV = (By.XPATH, '//p[text()="Не правильный логин/пароль"]')


class MainPageLocators(BaseLocators):
    ##  http://gl-backend.svtz.ru:5050/modules
    MODULE_CSS_BUTTON = (By.XPATH, '//td[text()="Построение КСС с помощью циклового метода"]')
    LOGOUT_BUTTON = (By.XPATH, '//button[text()="Выйти"]')


class Module18PageLocators(BaseLocators):
    ##  http://gl-backend.svtz.ru:5050/modules/18

    FRAME = (By.XPATH, '/html/body/div/div/div[2]/div/iframe')
    BUTTONS = (By.XPATH, '//div[contains(@class,"btn-success")]')

    HELP_BUTTON = (By.XPATH, "//img[@src=\"http://gl-backend.svtz.ru:5000/odata/downloadImage(name='Help.png')\"]")
    HELP_INFO = (By.XPATH, "/html/body/div/div/div/div[1]/div[3]/div/div[2]/div[1]")

    DONE_BUTTON = (By.XPATH, "//img[@src=\"http://gl-backend.svtz.ru:5000/odata/downloadImage(name='Complete.png')\"]")

    BLUE_BUTTON = (By.XPATH, "//img[@src=\"http://svtz.ru:5000/odata/downloadImage(name='blue.jpg')\"]")
    RED_BUTTON = (By.XPATH, "//img[@src=\"http://svtz.ru:5000/odata/downloadImage(name='red.jpg')\"]")
    MAGENTA_BUTTON = (By.XPATH, "//img[@src=\"http://svtz.ru:5000/odata/downloadImage(name='magenta.jpg')\"]")
    YELLOW_BUTTON = (By.XPATH, "//img[@src=\"http://svtz.ru:5000/odata/downloadImage(name='yellow.jpg')\"]")
    GREY_BUTTON = (By.XPATH, "//img[@src=\"http://svtz.ru:5000/odata/downloadImage(name='grey.jpg')\"]")
    BROWN_BUTTON = (By.XPATH, "//img[@src=\"http://svtz.ru:5000/odata/downloadImage(name='brown.jpg')\"]")

    BALL_INF0 = (By.XPATH, '//p[@class="MarkPositive___gKoZp"]')
    TASK_INFO = (By.XPATH, '//div[@class="TaskCell___13bM1"]')

    GRAPH = (By.XPATH, '//*[name()="svg"]')

    graph_base = '//*[name()="svg"]'

    vertex_base = '//*[name()="svg"]/*[name()="circle"]'
    vertex_path = '//*[name()="svg"]/*[@label="{}"]'

    edge_base = '//*[name()="svg"]/*[name()="line"]'
    edge_path = '//*[name()="svg"]/*[@in="{in}" and @out="{out}"]'

    VERTICES = (By.XPATH, '//*[name()="svg"]/*[name()="circle"]')
    EDGES = (By.XPATH, '//*[name()="svg"]/*[name()="line"]')



    # LOGOUT_BUTTON = (By.XPATH,  '//a[contains(text(),"Logout")]')
    # LOG_INFO_DIV = (By.ID, 'login-controls')
    # LOG_VK_ID = (By.XPATH,  '//li[contains(text(),"VK ID:")]')
    # LOG_USERNAME = (By.XPATH,  '//li[contains(text(),"Logged as")]')
    #
    # API_BUTTON = (By.XPATH, '//a[@href="https://en.wikipedia.org/wiki/Application_programming_interface"]')
    # FUT_INTERNET_BUTTON = (By.XPATH, '//a[@href="https://www.popularmechanics.com/technology/infrastructure/a29666802/future-of-the-internet/"]')
    # SMTP_BUTTON = (By.XPATH, '//a[@href="https://ru.wikipedia.org/wiki/SMTP"]')
    #
    # FACT_PYTHON_DIV = (By.XPATH, '//div[contains(@class,"uk-text-large")]/p[2]')
    #
    # HOME_BUTTON = (By.XPATH, '//a[contains(text(),"HOME")]')
    #
    # PYTHON_BUTTON = (By.XPATH, '//a[text()="Python"]')
    # PYTHON_HISTORY_BUTTON = (By.XPATH, '//a[text()="Python history"]')
    # FLASK_BUTTON = (By.XPATH, '//a[text()="About Flask"]')
    #
    # NETWORK_BUTTON = (By.XPATH, '//a[contains(text(),"Network")]')
    # NEWS_BUTTON = (By.XPATH, '//a[contains(text(),"News")]')
    # DOWNLOAD_BUTTON = (By.XPATH, '//a[text()="Download"]')
    # TCPEXAMP_BUTTON = (By.XPATH, '//a[contains(text(),"Examples ")]')
    #
    # LINUX_BUTTON = (By.XPATH, '//a[contains(text(),"Linux")]')
    # CENTOS_BUTTON = (By.XPATH, '//a[contains(text(),"Download Centos7")]')





