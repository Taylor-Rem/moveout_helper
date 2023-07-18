from config import username, password, resident_map

if __name__ == "__main__":
    helper = Moveout_helper(report_types[choose_report])
    helper.webdriver_operations.driver.get(resident_map)
    helper.webdriver_operations.login(username, password)
    helper.webdriver_operations.driver.maximize_window()
    helper.reports_loop()
    helper.webdriver_operations.driver.quit()
