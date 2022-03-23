import os
import pytest
import json
from framework.utils.driver_factory import DriverFactory
from framework.utils.browser import Browser

CONFIG_PATH = "test_data.json"

@pytest.fixture(scope="session")
def setup():
    driver_instance = DriverFactory()
    driver = driver_instance.set_up()
    yield driver
    Browser.tear_down(driver)
    
@pytest.fixture(scope="session")
def get_test_data():
    os.chdir("../..")
    test_data_file = open(CONFIG_PATH)
    test_data = json.load(test_data_file)
    os.chdir("../..")
    return test_data
