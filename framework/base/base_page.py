from framework.utils.browser import Browser

browser = Browser()

class BasePage:

    def __init__(self):
        self.driver = Browser.driver
           
    def get_locator_with_replaced_xpath(self, input_xpath, replace_what, replace_to):
        locator_xpath = input_xpath.replace(replace_what, replace_to)
        return locator_xpath

    def verify_current_page_by_url(self, url):
        assert browser.get_current_url() == url

    def verify_current_page_by_title(self, title):
        assert browser.get_current_page_title() == title
