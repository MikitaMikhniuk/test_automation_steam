import pytest
from framework.browser import BROWSER, Browser
from framework.utils.json_reader import get_json

CONFIG_PATH = "steam\\resources\\factory_config.json"


@pytest.fixture(scope="session")
def setup():
    BROWSER.maximize_window()
    BROWSER.navigate(get_json(CONFIG_PATH)["START_URL"])
    yield BROWSER.driver
    BROWSER.tear_down(BROWSER.driver)
