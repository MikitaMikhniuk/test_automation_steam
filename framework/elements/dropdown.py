from framework.elements.base_element import BaseElement
from selenium.webdriver.support.ui import Select


class Dropdown(BaseElement):
    def __init__(self, driver, element):
        super().__init__(driver, element)

    def select_by_dropdown_value(self, value):
        Select(self.element).select_by_value(value)
