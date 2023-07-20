from webdriver_operations import WebDriverOperations
from filter_properties import FilterProperties
from json_operations import JsonOperations
from config import username, password, resident_map
from grab_pdf import PDFExtractor
from selenium.common.exceptions import NoSuchElementException


class Moveout_Helper:
    def __init__(self, app):
        self.app = app
        self.webdriver = WebDriverOperations()
        self.webdriver.driver.get(resident_map)
        self.webdriver.login(username, password)
        self.webdriver.driver.maximize_window()

        self.pdf_extractor = PDFExtractor()
        self.filter = FilterProperties(self.pdf_extractor)
        self.json_operations = JsonOperations(self.pdf_extractor)

        (
            self.property_names,
            self.resident_names,
            self.unit_numbers,
        ) = self.filter.filter_properties()
        self.current_index = 0
        self.temp_storage = self.json_operations.retrieve_json()
        self.next_step()

    def add_button(self):
        self.add_to_ledger()
        self.next_step()

    def add_to_ledger(self):
        propunit = self.property + "_" + self.resident + "_" + str(self.unit)
        self.temp_storage.append(propunit)
        self.json_operations.write_json(self.temp_storage)

    def next_step(self):
        if self.current_index < len(self.property_names):
            self.load_next_property_resident_unit()
            self.process_current_property_resident_unit()
            self.current_index += 1

        if self.current_index >= len(self.property_names):
            self.close_application()

    def load_next_property_resident_unit(self):
        self.property = self.property_names[self.current_index]
        self.resident = self.resident_names[self.current_index]
        self.unit = self.unit_numbers[self.current_index]

    def process_current_property_resident_unit(self):
        self.webdriver.open_property(self.property)
        self.webdriver.open_unit(self.unit)
        if self.webdriver.compare_resident(self.resident):
            self.webdriver.open_ledger()
        else:
            self.process_former_resident()

    def process_former_resident(self):
        self.webdriver.search_former(self.resident)
        try:
            self.webdriver.open_ledger()
        except NoSuchElementException:
            self.log_error_with_property_resident_unit()
            self.add_to_ledger()

    def log_error_with_property_resident_unit(self):
        # Use appropriate logging mechanism
        print(
            f"There was a problem with Property: {self.property} - Resident: {self.resident} - Unit: {self.unit}"
        )

    def close_application(self):
        self.webdriver.driver.quit()
        self.app.close()
