from framework.utils.waiter import UntilNot
from steam.page_objects.base_steam_page import BaseSteamPage
from selenium.webdriver.common.by import By


class MainPage(BaseSteamPage):
    """
    Steam main page class.

    Contains methods for working with the main page objects.
    """

    def __init__(self, driver):
        super().__init__(driver)

    MENU_XPATH_LOCATOR = '//a[@class="pulldown_desktop" and text()="value"]'
    SUBMENU_XPATH_LOCATOR = '//a[@class="popup_menu_item" and normalize-space(text())="genre"]'
    TAB_XPATH_LABEL = '//span[text()="value"]'
    MODAL_TAB = (By.XPATH, '//div[@class="newmodal"]')

    def get_submenu_item(self, genre):
        """
        Method is used to get Submenu tab element.

        Input-> Submenu label (str). Example: "Action".
        """
        submenu_item = self.find_element_by_xpath(
            self.get_locator_with_replaced_xpath(
                self.SUBMENU_XPATH_LOCATOR, "genre", genre
            )
        )
        self.SELECTED_GENRE = genre
        return submenu_item, genre

    def navigate_menu(self, menu_item_name, submenu_item_name):
        """
        Complex method for navigating through the Steam navigation menu.

        Input-> Menu label (str). Example: "Categories".
        Input-> Menu label (str). Example: "Action".
        """
        wait_until_not = UntilNot(self.driver)
        wait_until_not.visibility_of_element_located(self.MODAL_TAB)
        menu_item = self.find_element_by_xpath(
            self.get_locator_with_replaced_xpath(
                self.MENU_XPATH_LOCATOR, "value", menu_item_name
            )
        )
        self.click_on_element(menu_item)
        submenu_item, genre = self.get_submenu_item(submenu_item_name)
        self.click_and_wait(submenu_item)
        return genre
