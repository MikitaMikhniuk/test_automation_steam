from steam.page_objects.base_steam_page import BaseSteamPage
from framework.utils.browser import Browser


class AgeVerificationPage(BaseSteamPage):
    """
    Age verification page class.

    Contains basic methods available for working with Age verification page.
    """

    def __init__(self, driver):
        super().__init__(driver)

    WARNING_LOCATOR = '//h2'
    AGE_DAY_SELECTOR_ID = 'ageDay'
    AGE_MONTH_SELECTOR_ID = 'ageMonth'
    AGE_YEAR_SELECTOR_ID = 'ageYear'
    VIEW_PAGE_BTN_ID = 'view_product_page_btn'
    AGE_CHECK_KEYWORD_ID = "/agecheck/"

    def set_user_dob(self, day="28", month="August", year="1995"):
        """
        Methond is used to set up a User date of birth.

        Input (opt) -> Day (str). e.g. "28".

        Input (opt)-> Month (str). e.g. "August".

        Input (opt)-> Year (str). e.g. "1995".
        """
        day_selector = self.find_elements_by_id(self.AGE_DAY_SELECTOR_ID)
        self.click_on_element(day_selector)
        self.select_by_dropdown_value(day_selector, day)
        month_selector = self.find_element_by_id(self.AGE_MONTH_SELECTOR_ID)
        self.click_on_element(month_selector)
        self.select_by_dropdown_value(month_selector, month)
        year_selector = self.find_element_by_id(self.AGE_YEAR_SELECTOR_ID)
        self.click_on_element(year_selector)
        self.select_by_dropdown_value(year_selector, year)

    def wait_for_age_verification_page(self, app_id):
        """
        A complex methond is used to wait for age verification page
        and pass through it if needed.

        Input -> app id (str).
        """
        browser = Browser(self.driver)
        url = browser.get_current_url()
        print(url)
        if self.AGE_CHECK_KEYWORD_ID in url:
            print("Age check!")
            assert app_id == self.get_current_appid_from_url()
            self.set_user_dob()
            view_page_btn = self.find_element_by_id(self.VIEW_PAGE_BTN_ID)
            self.click_on_element(view_page_btn)
        else:
            print("No age check!")
            pass
