import json
from ui.fixtures import *
from dataclasses import dataclass


def pytest_addoption(parser):
    parser.addoption('--url', default='http://localhost:3000')
    parser.addoption('--browser', default='chrome')
    parser.addoption('--browser_ver', default='latest')
    parser.addoption('--selenoid', default=None)


@pytest.fixture(scope='session')
def config(request):
    url = request.config.getoption('--url')
    browser = request.config.getoption('--browser')
    version = request.config.getoption('--browser_ver')
    selenoid = request.config.getoption('--selenoid')       #true or none
    if selenoid:
        url = 'http://myapp:8082'
    return {'browser': browser, 'version': version, 'url': url, 'selenoid': selenoid}


@dataclass
class Settings:
    URL: str = None

#
# @pytest.fixture(scope='session')
# def config_api(docker_api) -> Settings:
#     settings = Settings(URL="http://0.0.0.0:8082/")
#     return settings


# @pytest.fixture(scope='function')
# def api_client(config_api):
#     user = 'valentina'
#     password = 'valentina'
#     client = ApiClient(config_api.URL, user, password)
#     return client


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        try:
            if 'driver' in item.fixturenames:
                web_driver = item.funcargs['driver']
            else:
                return

            allure.attach(
                web_driver.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            pass


def logs_record(app, db):

    app_data = []
    db_data = []

    for i in app.logs(stream=True):
        app_data.append(i.decode())

    for i in db.logs(stream=True):
        db_data.append(i.decode())

    with open("app_logs.json", "w") as file:
        json.dump(app_data, file, indent=3)

    with open("db_logs.json", "w") as file:
        json.dump(db_data, file, indent=3)
