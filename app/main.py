from fastapi import FastAPI
from app.routes.upload import router as upload_router
from app.routes.websocket import router as websocket_router
from app.models import Base, engine  

app = FastAPI()

# Creating database tables if don't exist
Base.metadata.create_all(bind=engine)

# Include Routes
app.include_router(upload_router, prefix="/api")
app.include_router(websocket_router, prefix="/ws")

@app.get("/")
def root():
    return {"message": "Welcome to the PDF QA Service"}
