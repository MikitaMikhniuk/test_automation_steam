import random
from framework.browser import BROWSER, Browser
from framework.elements.element_factory import ELEMENT_FACTORY, ElementType
from framework.utils.lang_utils import get_label
from framework.utils.waiter import Until
from steam.page_objects.base_steam_page import BaseSteamPage
from selenium.webdriver.common.by import By


class CategoryPage(BaseSteamPage):
    """
    Steam Category page class.

    Contains methods for working with Category page elements.
    """

    def __init__(self):
        super().__init__(self.PAGEHEADER_LOCATOR, get_label("Action"))

    
    RECOMMENDED_SPECIALS_XPATH = (By.XPATH, "//div[@class='contenthub_specials_grid']")
    APPID_LOCATOR = (By.XPATH, '//a[@class="store_capsule app_impression_tracked"]')
    DISCOUNTED_PERCENTAGES_LOCATOR = (By.XPATH, '//a[@class="store_capsule app_impression_tracked"]//div[@class="discount_pct"]')
    GAME_ITEM_LOCATOR = '//a[@class="store_capsule app_impression_tracked" and @data-ds-appid="GAME_ID"]'
    PAGEHEADER_LOCATOR = (By.XPATH, '//h2[@class="pageheader"]')

    # def verify_category_page(self, genre):
    #     """
    #     Assertion methond to that current page is <input> page.

    #     Input-> Genre (str). e.g. "Action".
    #     """
    #     wait_until = Until(self.driver)
    #     wait_until.visibility_of_element_located((By.XPATH, self.PAGEHEADER_LOCATOR))
    #     category_header = self.find_element_by_xpath(self.PAGEHEADER_LOCATOR)
    #     category_header_text = category_header.text.strip()
    #     assert category_header_text == genre
    #     return category_header_text

    def get_max_discount_recommended_special_item(self):
        # tab = self.find_element_by_xpath(self.RECOMMENDED_SPECIALS_XPATH)
        tab = ELEMENT_FACTORY.get_element(ElementType.CONTAINER, self.RECOMMENDED_SPECIALS_XPATH)
        # self.scroll_element_into_view(tab)
        tab.scroll_to_element()
        wait_until = Until(self.driver)
        wait_until.presence_of_all_elements_located(
            self.DISCOUNTED_PERCENTAGES_LOCATOR
        )
        wait_until.presence_of_all_elements_located(self.APPID_LOCATOR)
        # app_id_elements = self.find_elements_by_xpath(self.APPID_LOCATOR)
        app_id_elements = ELEMENT_FACTORY.get_elements(ElementType.LABEL, self.APPID_LOCATOR)
        # discount_elements = self.find_elements_by_xpath(self.DISCOUNTED_PERCENTAGES_LOCATOR)
        discount_elements = ELEMENT_FACTORY.get_elements(ElementType.LABEL, self.DISCOUNTED_PERCENTAGES_LOCATOR)
        app_ids = []
        discounts = []
        for id_element in app_id_elements:
            app_id = id_element.get_attribute("data-ds-appid")
            app_ids.append(app_id)
        for discount_element in discount_elements:
            discount = discount_element.get_text()
            discounts.append(discount)
        res = dict(zip(app_ids, discounts))
        max_discount_ids = [
            key for key, value in res.items() if value == max(res.values())
        ]
        if len(max_discount_ids) > 1:
            game_id = random.choice(max_discount_ids)
        else:
            game_id = max_discount_ids[0]
        game_item_locator = (By.XPATH, self.GAME_ITEM_LOCATOR.replace("GAME_ID", game_id))
        # element = self.find_element_by_xpath(game_item_locator)
        element = ELEMENT_FACTORY.get_element(ElementType.LABEL, game_item_locator)
        return element, game_id

    def click_on_max_discount_game(self):
        """
        A complex method is used to find the app with the max discount
        and click on it.

        Retruns -> Max discount app id (str).
        """
        element, app_id = self.get_max_discount_recommended_special_item()
        # self.move_to_element(element)
        element.move_cursor_to_element()
        # self.click_and_wait(element)
        element.click_and_wait()
        BROWSER.switch_to_window(-1)
        return app_id
