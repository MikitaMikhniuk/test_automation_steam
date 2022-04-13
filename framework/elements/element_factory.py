from enum import Enum, auto
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.browser import BROWSER
from framework.elements.base_element import BaseElement
from framework.elements.button import Button
from framework.elements.container import Container
from framework.elements.dropdown import Dropdown
from framework.elements.label import Label

DEFAULT_TIMEOUT = 10


class ElementType(Enum):
    BASE = auto()
    LABEL = auto()
    BUTTON = auto()
    CONTAINER = auto()
    DROPDOWN = auto()


class ElementFactory:
    def __init__(self, driver):
        self.driver = driver

    def __get_element_internal(self, locator, timeout=DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def __get_elements_internal(self, locator, timeout=DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    def __get_element(self, type, element):
        if type == ElementType.LABEL:
            return Label(self.driver, element)
        elif type == ElementType.BUTTON:
            return Button(self.driver, element)
        elif type == ElementType.CONTAINER:
            return Container(self.driver, element)
        elif type == ElementType.DROPDOWN:
            return Dropdown(self.driver, element)
        else:
            return BaseElement(self.driver, element)

    def get_element(self, type, locator, timeout=DEFAULT_TIMEOUT):
        element = self.__get_element_internal(locator, timeout)
        return self.__get_element(type, element)

    def get_elements(self, type, locator, timeout=DEFAULT_TIMEOUT):
        elements = self.__get_elements_internal(locator, timeout)
        return map(lambda el: self.__get_element(type, el), elements)


ELEMENT_FACTORY = ElementFactory(BROWSER.driver)
