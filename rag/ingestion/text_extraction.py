def extract_text(loaded_pdf: dict) -> list[dict]:
    """
    Extract selectable text from a loaded PDF page by page.

    Args:
        loaded_pdf: Dictionary returned by PDFLoader.load()

    Returns:
        List of dictionaries containing page number and text.
    """

    pdf = loaded_pdf["pdf"]

    extracted_pages = []

    for page_number, page in enumerate(pdf, start=1):

        text = page.get_text("text").strip()

        if text:
            extracted_pages.append({
                "page_number": page_number,
                "text": text
            })

    return extracted_pages