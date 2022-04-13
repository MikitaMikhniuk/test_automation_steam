from framework.elements.element_factory import ELEMENT_FACTORY, ElementType
from framework.utils.lang_utils import get_label
from steam.page_objects.base_steam_page import BaseSteamPage
from framework.browser import BROWSER
from selenium.webdriver.common.by import By

AGE_CHECK_KEYWORD_ID = "/agecheck/"

class AgePage(BaseSteamPage):
    """
    Age verification page class.

    Contains basic methods available for working with Age verification page.
    """

    def __init__(self):
        super().__init__(self.DOB_REQUEST, get_label("AgePageAnchor"))

    DOB_REQUEST = (By.XPATH, "//div[@class='agegate_birthday_desc']")
    WARNING_LOCATOR = "//h2"
    AGE_DAY_SELECTOR_ID = (By.ID, "ageDay")
    AGE_MONTH_SELECTOR_ID = (By.ID, "ageMonth")
    AGE_YEAR_SELECTOR_ID = (By.ID, "ageYear")
    VIEW_PAGE_BTN_ID = (By.ID, "view_product_page_btn")
    # AGE_CHECK_KEYWORD_ID = "/agecheck/"

    def set_day(self, day):
        # day_selector = self.find_element_by_id(self.AGE_DAY_SELECTOR_ID)
        day_selector = ELEMENT_FACTORY.get_element(ElementType.DROPDOWN, self.AGE_DAY_SELECTOR_ID)
        # self.click(day_selector)
        day_selector.click()
        # self.select_by_dropdown_value(day_selector, day)
        day_selector.select_by_dropdown_value(day)


    def set_month(self, month):
        # month_selector = self.find_element_by_id(self.AGE_MONTH_SELECTOR_ID)
        month_selector = ELEMENT_FACTORY.get_element(ElementType.DROPDOWN, self.AGE_MONTH_SELECTOR_ID)
        # self.click(month_selector)
        month_selector.click()
        # self.select_by_dropdown_value(month_selector, month)
        month_selector.select_by_dropdown_value(month)

    
    def set_year(self, year):
        # year_selector = self.find_element_by_id(self.AGE_YEAR_SELECTOR_ID)
        year_selector = ELEMENT_FACTORY.get_element(ElementType.DROPDOWN, self.AGE_YEAR_SELECTOR_ID)
        # self.click(year_selector)
        year_selector.click()
        # self.select_by_dropdown_value(year_selector, year)
        year_selector.select_by_dropdown_value(year)

    def verify_age(self, app_id, day, month, year):
        """
        A complex methond is used to wait for age verification page
        and pass through it if needed.

        Input -> app id (str).
        """
        print("Age check!")
        assert app_id == self.get_current_appid_from_url()
        self.set_day(day)
        self.set_month(month)
        self.set_year(year)
        # view_page_btn = self.find_element_by_id(self.VIEW_PAGE_BTN_ID)
        view_page_btn = ELEMENT_FACTORY.get_element(ElementType.BUTTON, self.VIEW_PAGE_BTN_ID)
        # self.click_and_wait(view_page_btn)
        view_page_btn.click_and_wait()

    @staticmethod
    def is_age_page():
        url = BROWSER.get_current_url()
        return AGE_CHECK_KEYWORD_ID in url
