from webtable.src.page_object.webtable_locators import Locator
from time import sleep


class WebTableApp(object):
    def __init__(self, driver):
        self.driver = driver

    def click_add_user_button(self):
        self.driver.find_element(
            "xpath",
            Locator.add_user_button
        ).click()

    def find_add_user_modal(self):
        return self.driver.find_element(
            "xpath",
            Locator.add_user_modal
        ).is_displayed()

    def enter_first_name(self, first_name):
        self.driver.find_element(
            "xpath",
            Locator.first_name_input
        ).send_keys(first_name)

    def enter_username(self, user_name):
        self.driver.find_element(
            "xpath",
            Locator.user_name_input
        ).send_keys(user_name)

    def select_user_role(self, role):
        self.driver.find_element(
            "xpath",
            Locator.select_role_dropdown
        ).click()
        sleep(1)

        self.driver.find_element(
            "xpath",
            role
        ).click()

    def enter_user_phone_number(self, phone_number):
        self.driver.find_element(
            "xpath",
            Locator.cell_phone_input
        ).send_keys(phone_number)

    def click_save_new_user(self):
        self.driver.find_element(
            "xpath",
            Locator.save_user_button
        ).click()

    def find_user_row(self, username):
        return self.driver.find_element(
            "xpath",
            username
        ).is_displayed()

    def get_total_row_count(self):
        return len(
            self.driver.find_elements(
                "xpath",
                Locator.total_user_rows
            )
        )

    def delete_user(self, user):
        self.driver.find_element(
            "xpath",
            user
        ).click()
        sleep(1)

        self.driver.find_element(
            "xpath",
            Locator.confirm_delete_button
        ).click()
