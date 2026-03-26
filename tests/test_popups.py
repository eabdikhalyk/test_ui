import time
from data.login_with_arm import login_with_arm
from pages.arm.advertisement_page import AdvertisementPage


class TestPopup:
    def test_add_popup(self, driver):
        login_with_arm(driver,"MANAGER_USER","MANAGER_PASSWORD")
        advertising_page = AdvertisementPage(driver)
        advertising_page.open_popup()
        advertising_page.add_popup()
        advertising_page.fill_form()
        advertising_page.save()

        time.sleep(5)

    def test_edit_popup(self, driver):
       print("test_edit_popup")

    def test_delete_popup(self, driver):
        print("test_delete_popup")
