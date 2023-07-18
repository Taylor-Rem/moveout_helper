from datetime import datetime
import os
import fitz, re

now = datetime.now()
day = now.day
month = now.month
year = now.year
username = "taylorremund"

path = f"/Users/{username}/Desktop/move_out_helper/{year}/{month}/{day}"

file_name = os.listdir(path)[-1]
file_path = os.path.join(path, file_name)


def extract_text_and_links(page):
    text = page.get_text()
    links = []

    for link in page.get_links():
        if link["kind"] == 1:  # 1 represents URI links
            link_url = link["uri"]
            links.append(link_url)

    return text, links


pdf_text = []
numbers = []

with fitz.open(file_path) as pdf:
    for page_number in range(pdf.page_count):
        page = pdf.load_page(page_number)
        page_text, _ = extract_text_and_links(page)

        # Extract property name and unit number using regular expressions
        matches = re.findall(r"([\w\s]+)\s+(\d+\.\d+)", page_text)
        if matches:
            pdf_text.extend(match[0].split("\n")[-1] for match in matches)
            numbers.extend(match[1] for match in matches)

property_names = pdf_text[0::2]
unit_numbers = numbers[0::2]
