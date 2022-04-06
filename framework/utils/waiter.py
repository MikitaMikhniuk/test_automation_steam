from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.utils import json_reader

CONFIG_PATH = "steam\\resources\\factory_config.json"
config = json_reader.get_json(CONFIG_PATH)


class Until:

    timeout = config["DEFAULT_WAIT_TIME"]

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, self.timeout)

    def visibility_of_any_elements_located(self, elements):
        self.wait.until(EC.visibility_of_any_elements_located(elements))
        return elements

    def presence_of_element_located(self, element):
        self.wait.until(EC.presence_of_element_located(element))
        return element

    def visibility_of_element_located(self, elements):
        self.wait.until(EC.visibility_of_element_located(elements))
        return elements

    def presence_of_all_elements_located(self, elements):
        self.wait.until(EC.presence_of_all_elements_located(elements))
        return elements


class UntilNot(Until):

    def __init__(self, driver):
        super().__init__(driver)

    def presence_of_element_located(self, element): #одинаковые имена с 21-ой строкой
        self.wait.until_not(EC.presence_of_element_located(element))
        return element

    def visibility_of_element_located(self, element):
        self.wait.until_not(EC.visibility_of_element_located(element))
        return element
