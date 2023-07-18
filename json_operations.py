import json
import os


class JsonOperations:
    def __init__(self, json_path):
        self.json_path = json_path

    def write_json(self, data):
        file_path = self.json_path + "completed.json"
        try:
            with open(file_path, "w") as file:
                json.dump(data, file)
        except Exception as e:
            print(e)

    def retrieve_json(self):
        try:
            file_path = self.json_path + "completed.json"
            with open(file_path, "r") as file:
                json_string = file.read()
            data = json.loads(json_string)
            return data
        except:
            return []

    def delete_json(self):
        file_path = self.json_path + "completed.json"
        if os.path.exists(self.json_path):
            os.remove(self.json_path)
