class Locator(object):
    # web app url
    web_table_url = "http://www.way2automation.com/angularjs-protractor/webtables/"

    # web elements xpath
    add_user_modal = "//div[@class='modal ng-scope']"
    total_user_rows = "//tbody/tr[@class='smart-table-data-row ng-scope']"
    add_user_button = "//button[@type='add']"
    delete_novak_user_link = "//td[text()='novak']/..//i[@class='icon icon-remove']"
    confirm_delete_button = "//button[text()='OK']"
    first_name_input = "//input[@name='FirstName']"
    user_name_input = "//input[@name='UserName']"
    select_role_dropdown = "//select[@name='RoleId']"
    admin_role_dropdown_option = "//option[@value='2']"
    cell_phone_input = "//input[@name='Mobilephone']"
    save_user_button = "//button[@class='btn btn-success']"
    ernesto_username = "//td[text()='ernestalbrz']"
