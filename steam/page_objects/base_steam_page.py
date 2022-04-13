from framework.base_page import BasePage
from framework.browser import BROWSER
from steam.page_objects.header.steam_header import SteamHeader


class BaseSteamPage(BasePage):
    """
    Base Steam page class.

    Contains basic methods available for all Steam pages.

    """
    steam_header = SteamHeader()

    def __init__(self, locator, title):
        super().__init__(locator, title)

    def get_current_appid_from_url(self):
        """
        Methond is used to get app id of the current app page URL.

        Returns -> app id (str).
        """
        url = BROWSER.get_current_url()
        url_splitted = url.split("/")
        app_index = url_splitted.index("app")
        app_id = url_splitted[app_index + 1]
        return app_id
