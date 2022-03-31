from framework.utils.lang_utils import get_label
from framework.utils.browser import Browser
from steam.page_objects.main_page import MainPage
from steam.page_objects.category_page import CategoryPage
from steam.page_objects.download_page import DownloadPage
from steam.page_objects.app_page import AppPage
from steam.page_objects.age_check_page import AgeVerificationPage


def test_max_discount(setup, get_test_data):
    driver = setup
    browser = Browser(driver)
    browser.navigate(get_test_data["START_URL"])

    main_page = MainPage(driver)
    main_page.check_for_current_lang(
        get_test_data["DESIRED_LANG_CODE"], get_test_data["DESIRED_LANG_FULL"])
    main_page.verify_current_page_by_url(get_test_data["START_URL"])
    main_page.navigate_menu(
        get_label(driver, get_test_data["NAV_STEP_1"]), get_label(driver, get_test_data["NAV_STEP_2"]))

    category_page = CategoryPage(driver)
    category_page.verify_category_page(
        get_label(driver, get_test_data["NAV_STEP_2"]))

    app_id = category_page.click_on_max_discount_game()

    age_check = AgeVerificationPage(driver)
    age_check.wait_for_age_verification_page(app_id, get_test_data["DOB"])

    app_page = AppPage(driver)
    app_page.verify_current_app_page(app_id)
    app_page.navigate_to_download_page()

    download_page = DownloadPage(driver)
    download_page.download_installer(get_test_data["FILE_NAME"])
