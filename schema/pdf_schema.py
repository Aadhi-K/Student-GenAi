from pydantic import BaseModel

class PDFResponse(BaseModel):
    message: str
    filename: str
    chunks: int