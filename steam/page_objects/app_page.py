from framework.utils.waiter import Until
from steam.page_objects.base_steam_page import BaseSteamPage
from selenium.webdriver.common.by import By


class AppPage(BaseSteamPage):
    """
    App page class.

    Contains methond for working with application page.
    """

    def __init__(self):
        super().__init__()

    APP_NAME_ID = "appHubAppName"

    def verify_current_app_page(self, app_id):
        """
        Assertion methond to compare current page app id with the given one (input).

        Input-> app id (str).
        """
        wait_until = Until(self.driver)
        wait_until.visibility_of_element_located((By.ID, self.APP_NAME_ID))
        id = self.get_current_appid_from_url()
        assert id == app_id
