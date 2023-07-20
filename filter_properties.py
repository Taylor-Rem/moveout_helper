from grab_pdf import PDFExtractor
from json_operations import JsonOperations


class FilterProperties:
    def __init__(self, pdf_extractor):
        self.pdf_extractor = pdf_extractor
        (
            self.property_names,
            self.unit_numbers,
        ) = self.pdf_extractor.get_property_and_unit_numbers()
        self.json_interact = JsonOperations(self.pdf_extractor)

    def current_report_items(self):
        current_report_items = []
        for i in range(len(self.property_names)):
            property = self.property_names[i]
            unit = self.unit_numbers[i]
            propunit = property + "_" + str(unit)
            current_report_items.append(propunit)
        return current_report_items

    def filter_properties(self):
        set1 = set(self.current_report_items())
        set2 = set(self.json_interact.retrieve_json())
        unique_elements = (set1 - set2) | (set2 - set1)
        properties = []
        units = []
        for item in unique_elements:
            prop, unit = item.split("_")
            properties.append(prop)
            units.append(unit)
        return properties, units
