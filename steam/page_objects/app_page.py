from framework.utils.lang_utils import get_label
from steam.page_objects.base_steam_page import BaseSteamPage
from selenium.webdriver.common.by import By


class AppPage(BaseSteamPage):
    """
    App page class.

    Contains methond for working with application page.
    """

    def __init__(self):
        super().__init__(self.SYS_REQ, get_label("AppPageAnchor"))

    APP_NAME_ID = "appHubAppName"
    SYS_REQ = (By.XPATH, "//div[@class='game_page_autocollapse sys_req']/h2")

    def verify_current_app_page(self, app_id):
        """
        Assertion methond to compare current page app id with the given one (input).

        Input-> app id (str).
        """
        id = self.get_current_appid_from_url()
        assert id == app_id
