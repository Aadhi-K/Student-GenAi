import pymupdf

class PDFLoader:

    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path

    def load(self):

        pdf = pymupdf.open(self.pdf_path)

        return {
            "pdf": pdf,
            "filename": self.pdf_path,
            "page_count": pdf.page_count,
            "metadata": pdf.metadata
        }