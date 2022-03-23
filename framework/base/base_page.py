from framework.utils.browser import Browser
from framework.base.base_element import BaseElement


class BasePage:
    """
    Base page class.

    Contains basic methods available for all pages.
    """
    def __init__(self, driver):
        self.driver = driver

    HTML_HEAD_LOCATOR = '//html[@class=" responsive"]'

    def get_current_language(self):
        """
        Returns current page lang (str) based on HTML <head>.
        Example: "en".
        """
        base = BaseElement(self.driver)
        lang_element = base.find_element_by_xpath(self.HTML_HEAD_LOCATOR)
        current_lang = lang_element.get_attribute("lang")
        return current_lang

    def get_locator_with_replaced_xpath(self, input_xpath, replace_what, replace_to):
        """
        Method for getting a locator with a replaced str.

        Input xpath - str
        
        Replace what (str) - a str to be replaced.

        Replace to (str) - a str to be inserted.

        Returns an element xpath (str).
        """
        locator_xpath = input_xpath.replace(replace_what, replace_to)
        return locator_xpath

    def verify_current_page_by_url(self, url):
        """
        Assertion methond to compare current page URL with the given one (input).

        Input-> URL (str).
        """
        browser = Browser(self.driver)
        assert browser.get_current_url() == url

    def verify_current_page_by_title(self, title):
        """
        Assertion methond to compare current page title with the given one (input).

        Input-> title (str).
        """
        browser = Browser(self.driver)
        assert browser.get_current_page_title() == title
