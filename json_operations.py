import json
import os
from grab_pdf import PDFExtractor


class JsonOperations:
    def __init__(self, pdf_extractor):
        self.pdf_extractor = pdf_extractor
        self.json_path = self.pdf_extractor.json_path
        self.json_filename = "completed.json"

    def write_json(self, data):
        file_path = self.json_path + self.json_filename
        try:
            with open(file_path, "w") as file:
                json.dump(data, file)
        except Exception as e:
            print(e)

    def retrieve_json(self):
        try:
            file_path = self.json_path + self.json_filename
            with open(file_path, "r") as file:
                json_string = file.read()
            data = json.loads(json_string)
            return data
        except:
            return []

    def delete_json(self):
        file_path = self.json_path + self.json_filename
        if os.path.exists(self.json_path):
            os.remove(file_path)
