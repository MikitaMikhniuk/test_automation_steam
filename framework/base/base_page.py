from framework.utils.browser import Browser


class BasePage:

    # искать решение для уборки driver отсюда
    def __init__(self, driver):
        self.driver = driver

    # def __init__(self, element_locator, text):
    #     self.verify_opened_page(element_locator, text)

    # @staticmethod
    # def verify_opened_page(element_locator, text):

    
    def get_locator_with_replaced_xpath(self, input_xpath, replace_what, replace_to):
        locator_xpath = input_xpath.replace(replace_what, replace_to)
        return locator_xpath

    def verify_current_page_by_url(self, url):
        browser = Browser(self.driver)
        assert browser.get_current_url() == url

    def verify_current_page_by_title(self, title):
        browser = Browser(self.driver)
        assert browser.get_current_page_title() == title
