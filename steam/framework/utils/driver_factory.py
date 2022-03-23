from selenium import webdriver
from framework.utils.browser import Browser
from framework.utils import config_reader


class DriverFactory:
    """
    Creates a webdriver instance based on factory_config.json

    """
    @staticmethod
    def set_up():
        """
        Driver set up.
        """
        factory_config = config_reader.get_factory_config()
        s, options = Browser.browser_setup()
        if factory_config["BROWSER"] == "Chrome":
            driver = webdriver.Chrome(service=s, options=options)
        elif factory_config["BROWSER"] == "Firefox":
            driver = webdriver.Firefox(service=s, options=options)
        else:
            raise Exception("I don't know such driver yet!")
        return driver
