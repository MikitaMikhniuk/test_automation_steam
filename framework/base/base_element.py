from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class BaseElement:
    """
    Base element class.

    Contains basic methods for working with elements.
    """

    def __init__(self, driver):
        self.driver = driver

    def find_element_by_xpath(self, xpath):
        element = self.driver.find_element(By.XPATH, xpath)
        return element

    def find_elements_by_xpath(self, xpath):
        elements = self.driver.find_elements(By.XPATH, xpath)
        return elements

    def find_element_by_id(self, id):
        element = self.driver.find_element(By.ID, id)
        return element

    def find_elements_by_id(self, id):
        elements = self.driver.find_elements(By.ID, id)
        return elements

    def click_on_element(self, element):
        element.click()

    def click_and_wait(self, element):
        self.click_on_element(element)
        # move to Browser
        page_state = self.driver.execute_script('return document.readyState;')
        try:
            assert page_state == 'complete'
        except AssertionError:
            print("Page was not loaded after click event")

    def scroll_element_into_view(self, element):
        """
        Scrolls down to the input Selenium element.

        Input-> Element (selenium element).
        """
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def move_to_element(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element)

    def send_keys(self, element, keys):
        element.send_keys(keys)

    def select_by_dropdown_value(self, element, value):
        Select(element).select_by_value(value)
