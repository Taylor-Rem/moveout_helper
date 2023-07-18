from webdriver_operations import WebDriverOperations
from json_operations import JsonOperations


class ReportHelper:
    def __init__(self):
        self.webdriver_operations = WebDriverOperations()
        self.json_operations = JsonOperations()
