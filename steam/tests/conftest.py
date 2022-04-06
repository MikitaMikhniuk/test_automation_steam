import pytest
from framework.utils.browser import Browser
from framework.utils.json_reader import get_json

CONFIG_PATH = "steam\\resources\\factory_config.json"


@pytest.fixture(scope="session")
def setup():
    browser = Browser()
    browser.maximize_window()
    browser.navigate(get_json(CONFIG_PATH)["START_URL"])
    yield browser.driver
    browser.tear_down(browser.driver)
