import requests
from bs4 import BeautifulSoup
import io
import pdfplumber
import csv


url = "https://spokast.ru/media/2024/08/grafich.dizajner-9_kom_08.15_stend.pdf"


def extract_tables_from_pdf():
    response = requests.get(url)
    stream = io.BytesIO(response.content)
    with pdfplumber.open(stream) as pdf:
        tables = []
        for page in pdf.pages:
            tables.extend(page.extract_tables())
        return tables

async def get_applicant_list():
    tables = extract_tables_from_pdf()
    file = io.StringIO()
    writer = csv.writer(file)
    writer.writerow((tables[0]).pop(0))
    count = 0
    for table in tables:
        for row in table:
            if row[4]:
                count += 1
                writer.writerow(row)
    writer.writerow(['Всего', count])
    file.seek(0)
    file = io.BytesIO(file.getvalue().encode())
    file.seek(0)
    return file.getvalue()

# Используйте функцию для извлечения таблиц из PDF

