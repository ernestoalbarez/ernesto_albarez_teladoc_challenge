from webtable.src.test_base.web_driver_setup import WebDriverSetup
from webtable.src.page_object.pages.webtable_app import WebTableApp
import unittest
from time import sleep
from webtable.src.page_object.webtable_locators import Locator


class TestWebTableApp(WebDriverSetup):
    def test_add_user(self):
        driver = self.driver
        self.driver.get(Locator.web_table_url)
        self.driver.set_page_load_timeout(30)

        webtable = WebTableApp(driver)

        webtable.click_add_user_button()
        sleep(2)
        self.assertTrue(
            webtable.find_add_user_modal(),
            "Error: Add user modal not shown"
        )

        webtable.enter_first_name("Ernesto")
        webtable.enter_username("ernestalbrz")
        webtable.select_user_role(Locator.admin_role_dropdown_option)
        webtable.enter_user_phone_number("1122334455")
        webtable.click_save_new_user()

        self.assertTrue(
            webtable.find_user_row(Locator.ernesto_username),
            "Error: just added user cannot be found"
        )

    def test_delete_user(self):
        driver = self.driver
        self.driver.get(Locator.web_table_url)
        self.driver.set_page_load_timeout(30)

        webtable = WebTableApp(driver)

        row_count = webtable.get_total_row_count()
        webtable.delete_user(Locator.delete_novak_user_link)
        self.assertNotEqual(
            row_count,
            webtable.get_total_row_count(),
            "Error: user row was not deleted"
        )

    if __name__ == '__main__':
        unittest.main()
