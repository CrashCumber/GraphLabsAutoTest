import json
from ui.fixtures import *


def pytest_addoption(parser):
    parser.addoption('--url', default='http://gl-backend.svtz.ru:5050')
    parser.addoption('--browser', default='chrome')
    parser.addoption('--browser_ver', default='83.0.4103.14')
    parser.addoption('--selenoid', default=False)


@pytest.fixture(scope='session')
def config(request):
    url = request.config.getoption('--url')
    browser = request.config.getoption('--browser')
    version = request.config.getoption('--browser_ver')
    selenoid = request.config.getoption('--selenoid')
    return {'browser': browser, 'version': version, 'url': url, 'selenoid': selenoid}


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
