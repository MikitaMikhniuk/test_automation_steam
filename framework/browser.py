from framework.driver_factory import DriverFactory


class Browser:

    driver = DriverFactory().get_driver()

    def navigate(self, url):
        self.driver.get(url)

    def get_current_page_title(self):
        current_page_title = self.driver.title()
        return current_page_title

    def get_current_url(self):
        current_url = self.driver.current_url
        return current_url

    def switch_to_window(self, window_handle):
        self.driver.switch_to.window(self.driver.window_handles[window_handle])

    def page_reload(self):
        self.driver.execute_script("window.location.reload()")

    def maximize_window(self):
        self.driver.maximize_window()

    @staticmethod
    def tear_down(driver):
        if (driver != None):
            print("Cleanup of test environment!")
            driver.close()
            driver.quit()
