from framework.utils.json_reader import get_json
from framework.utils.lang_utils import get_label
from steam.page_objects.main_page import MainPage
from steam.page_objects.category_page import CategoryPage
from steam.page_objects.download_page import DownloadPage
from steam.page_objects.app_page import AppPage
from steam.page_objects.age_page import AgePage

test_data_path = r"steam\resources\test_data.json"


def test_max_discount(setup):
    test_data = get_json(test_data_path)
    main_page = MainPage()
    main_page.check_for_current_lang(
        test_data["DESIRED_LANG_CODE"], test_data["DESIRED_LANG_FULL"]
    )
    main_page.navigate_menu(get_label("Categories"), get_label("Action"))

    category_page = CategoryPage()
    app_id = category_page.click_on_max_discount_game()

    if AgePage.is_age_page():
        age_page = AgePage()
        age_page.verify_age(
            app_id, test_data["DOB_DAY"], test_data["DOB_MONTH"], test_data["DOB_YEAR"]
        )

    app_page = AppPage()
    app_page.verify_current_app_page(app_id)
    app_page.navigate_to_download_page()

    download_page = DownloadPage()
    download_page.download_installer(test_data["FILE_NAME"])
