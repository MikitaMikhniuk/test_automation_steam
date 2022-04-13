from framework.elements.element_factory import ELEMENT_FACTORY, ElementType
from framework.utils.waiter import UntilNot
from steam.page_objects.base_steam_page import BaseSteamPage
from selenium.webdriver.common.by import By
from framework.utils.lang_utils import get_label


class MainPage(BaseSteamPage):
    """
    Steam main page class.

    Contains methods for working with the main page objects.
    """

    def __init__(self):
        super().__init__(self.HEADER_TITLE_LOCATOR, get_label("MainPageAnchor"))

    HEADER_TITLE_LOCATOR = (By.XPATH, "//div[@class='gutter_header']/br/parent::div")
    MENU_XPATH_LOCATOR = '//a[@class="pulldown_desktop" and text()="{0}"]'
    SUBMENU_XPATH_LOCATOR = (
        '//a[@class="popup_menu_item" and normalize-space(text())="{0}"]'
    )

    def get_submenu_item(self, genre):
        """
        Method is used to get Submenu tab element.

        Input-> Submenu label (str). Example: "Action".
        """
        submenu_item = ELEMENT_FACTORY.get_element(
            ElementType.LABEL, (By.XPATH, self.SUBMENU_XPATH_LOCATOR.format(genre))
        )
        self.SELECTED_GENRE = genre
        return submenu_item, genre

    def navigate_menu(self, menu_item_name, submenu_item_name):
        """
        Complex method for navigating through the Steam navigation menu.

        Input-> Menu label (str). Example: "Categories".
        Input-> Menu label (str). Example: "Action".
        """
        menu_item = ELEMENT_FACTORY.get_element(
            ElementType.LABEL,
            (By.XPATH, self.MENU_XPATH_LOCATOR.format(menu_item_name)),
        )
        menu_item.click()
        submenu_item, genre = self.get_submenu_item(submenu_item_name)
        submenu_item.click_and_wait()
        return genre
