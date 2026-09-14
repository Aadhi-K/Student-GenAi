from langchain_text_splitters import RecursiveCharacterTextSplitter

class TextChunker:

    def __init__(self):

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )

    def create_chunks(self, text_pages,source):

        chunks = []

        for page in text_pages:

            page_chunks = self.splitter.split_text(
                page["text"]
            )

            for chunk in page_chunks:

                chunks.append({
                        "text": chunk,
                        "page_number": page["page_number"],
                        "source": source
                        })

        return chunks