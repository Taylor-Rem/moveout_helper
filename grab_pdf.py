from datetime import datetime
import os
import fitz, re


class PDFExtractor:
    def __init__(self, username="taylorremund"):
        now = datetime.now()
        day = now.day
        month = now.month
        year = now.year

        path = f"/Users/{username}/Desktop/move_out_helper/{year}/{month}/{day}"
        self.json_path = f"/Users/{username}/Desktop/move_out_helper/{year}/{month}"

        file_name = os.listdir(path)[-1]
        self.file_path = os.path.join(path, file_name)

    def extract_text_and_links(self, page):
        text = page.get_text()
        links = []

        for link in page.get_links():
            if link["kind"] == 1:  # 1 represents URI links
                link_url = link["uri"]
                links.append(link_url)

        return text, links

    def get_property_and_unit_numbers(self):
        pdf_text = []
        numbers = []

        with fitz.open(self.file_path) as pdf:
            for page_number in range(pdf.page_count):
                page = pdf.load_page(page_number)
                page_text, _ = self.extract_text_and_links(page)

                # Extract property name and unit number using regular expressions
                matches = re.findall(r"([\w\s]+)\s+(\d+\.\d+)", page_text)
                if matches:
                    pdf_text.extend(match[0].split("\n")[-1] for match in matches)
                    numbers.extend(match[1] for match in matches)

        property_names = pdf_text[0::2]
        unit_numbers = numbers[0::2]

        return property_names, unit_numbers
