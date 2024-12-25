from fastapi import APIRouter, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import os
from app.services.pdf_processing import extract_text_from_pdf
from app.models import Document
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

router = APIRouter()

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

UPLOAD_FOLDER = "./uploaded_pdfs/"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@router.post("/upload/")  
async def upload_pdf(file: UploadFile):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())

    extracted_text = extract_text_from_pdf(file_path)
    if not extracted_text:
        raise HTTPException(status_code=400, detail="Failed to extract text from PDF")

    session = SessionLocal()
    document = Document(filename=file.filename, file_path=file_path)
    session.add(document)
    session.commit()

    return JSONResponse({"message": "File uploaded and text extracted successfully"})
