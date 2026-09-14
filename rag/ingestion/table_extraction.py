import pdfplumber


class TableExtractor:

    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path

    def extract_tables(self):

        extracted_tables = []

        with pdfplumber.open(self.pdf_path) as pdf:

            for page_number, page in enumerate(pdf.pages, start=1):

                tables = page.extract_tables()

                for table_number, table in enumerate(tables, start=1):

                    if table:
                        extracted_tables.append({
                            "page_number": page_number,
                            "table_number": table_number,
                            "data": table
                        })

        return extracted_tables