from webdriver_operations import WebDriverOperations
from json_operations import JsonOperations
from grab_pdf import PDFExtractor
from config import username, password, resident_map


class Moveout_Helper:
    def __init__(self):
        self.webdriver_operations = WebDriverOperations()
        self.webdriver_operations.driver.get(resident_map)
        self.webdriver_operations.login(username, password)
        self.webdriver_operations.driver.maximize_window()
        self.json_operations = JsonOperations()
        pdf_extractor = PDFExtractor()
        (
            self.property_names,
            self.unit_numbers,
        ) = pdf_extractor.get_property_and_unit_numbers()
        self.current_index = 0

    def next_step(self):
        if self.current_index < len(self.property_names):
            property = self.property_names[self.current_index]
            unit = self.unit_numbers[self.current_index]
            self.webdriver_operations.open_property(property)
            self.webdriver_operations.open_unit(unit)
            self.webdriver_operations.open_ledger()
            self.current_index += 1
