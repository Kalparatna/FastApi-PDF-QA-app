from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from datetime import datetime

# Define the database URL and setup
DATABASE_URL = "sqlite:///./test.db"  
engine = create_engine(DATABASE_URL)  
Base = declarative_base()  


class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, nullable=False)
    upload_date = Column(DateTime, default=datetime.utcnow)
    file_path = Column(String, nullable=False)

class ExtractedText(Base):
    __tablename__ = "extracted_texts"
    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(Integer, nullable=False)
    content = Column(Text, nullable=False)

#query for Database Creation
Base.metadata.create_all(bind=engine)
