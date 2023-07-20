from webdriver_operations import WebDriverOperations
from filter_properties import FilterProperties
from json_operations import JsonOperations
from config import username, password, resident_map
from grab_pdf import PDFExtractor


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

        self.property_names, self.unit_numbers = self.filter.filter_properties()
        self.current_index = 0
        self.temp_storage = self.json_operations.retrieve_json()
        self.next_step()

    def add_ledger(self):
        propunit = self.property + "_" + str(self.unit)
        self.temp_storage.append(propunit)
        self.json_operations.write_json(self.temp_storage)
        self.next_step()

    def next_step(self):
        if self.current_index < len(self.property_names) - 1:
            self.property = self.property_names[self.current_index]
            self.unit = self.unit_numbers[self.current_index]
            self.webdriver.open_property(self.property)
            self.webdriver.open_unit(self.unit)
            self.webdriver.open_ledger()
            self.current_index += 1
        else:
            self.app.close()
