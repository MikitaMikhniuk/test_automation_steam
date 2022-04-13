from framework.browser import BROWSER
from framework.elements.element_factory import ELEMENT_FACTORY, ElementType


class BasePage:
    def __init__(self, locator, title):
        self.driver = BROWSER.driver
        self.verify_page_is_opened(locator, title)

    def verify_current_page_by_url(self, url):
        assert BROWSER.get_current_url() == url

    def verify_current_page_by_title(self, title):
        assert BROWSER.get_current_page_title() == title

    def verify_page_is_opened(self, locator, title):
        element = ELEMENT_FACTORY.get_element(ElementType.LABEL, locator)
        if element.get_text().strip().lower() != title.lower():
            raise Exception(
                f'Wrong page! Expected "{title}", got "{element.get_text()}"'
            )
