
# PDF QA Service

## Description

The **PDF QA Service** is a FastAPI-based application that allows users to upload PDF documents, extract the text content, and use it for real-time question answering through WebSockets. This service leverages NLP techniques to respond to user queries based on the content of the uploaded PDFs. It also supports storing document metadata and extracted text in a database for efficient retrieval and processing.

The service is designed to be scalable and includes rate-limiting to manage server load and prevent abuse. This is an excellent tool for building intelligent systems that require PDF document analysis and question-answering capabilities.

## Features

- **PDF Upload**: Allows users to upload PDF files through a RESTful API endpoint.
- **Text Extraction**: Automatically extracts text from the uploaded PDFs for further processing.
- **Real-Time Question Answering**: Users can ask questions related to the PDF's content via WebSockets, and the system uses NLP models to provide real-time responses.
- **Session-based Context**: Supports follow-up questions while maintaining the context of the conversation.
- **Data Management**: Stores metadata about uploaded PDFs and extracted text content in a database (SQLite).
- **Rate Limiting**: Implements rate limiting for both API and WebSocket endpoints to prevent abuse.

## Setup Instructions

### Prerequisites

Before you can run the application, make sure you have the following installed on your machine:

- Python 3.12.2
- pip (Python's package installer)
- Redis (for rate-limiting) 

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd <project_folder>
   ```

2. **Create a virtual environment**:
   If you're using Python 3.7 or above, it's recommended to create a virtual environment for your project:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:
   Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

   You may need to install Redis separately if you're using rate limiting:
   - Install Redis from [here](https://redis.io/download) or using your system's package manager.

5. **Setup the Database**:
   The application uses SQLite for database storage. When the application starts, it will automatically create the database tables.
   
   If you're using a different database, make sure to modify the `DATABASE_URL` in `main.py`.

### Configuration

- **File Upload Folder**: The PDFs will be stored in a folder named `uploaded_pdfs/` in the project directory. You can change the folder location in the code if needed.

- **Redis (Optional)**: If you're using Redis for rate-limiting, make sure Redis is running on your machine. You can configure it in `main.py` under `FastAPILimiter.init()`.

### Running the Application

1. **Start the FastAPI Application**:
   Once all the dependencies are installed and the configuration is set up, you can start the FastAPI app with Uvicorn:
   ```bash
   uvicorn app.main:app --reload
   ```
   The `--reload` flag allows you to see changes immediately during development.

2. **Access the Application**:
   - Open your browser and go to `http://127.0.0.1:8000/` to view the API's home page.
   - Access the **Swagger UI** for API documentation at `http://127.0.0.1:8000/docs`.
   - Alternatively, you can use **ReDoc** for API documentation at `http://127.0.0.1:8000/redoc`.

3. **WebSocket Access**:
   - For real-time question answering, connect to the WebSocket endpoint using a WebSocket client like [WebSocket King Client](https://chrome.google.com/webstore/detail/websocket-king-client/).
   
   The WebSocket URL to connect is:
   ```
   ws://127.0.0.1:8000/ws/qa/
   ```

   Send a question like "What is the summary of this document?" to interact with the uploaded PDF content.

### Example Requests

- **PDF Upload**: 
   - Method: `POST`
   - Endpoint: `/api/upload/`
   - Content-Type: `multipart/form-data`
   - Body: Choose a PDF file to upload.
   - Response: 
     ```json
     {
       "message": "File uploaded and text extracted successfully"
     }
     ```

- **Real-Time Question Answering**:
   - Method: `WebSocket`
   - Endpoint: `/ws/qa/`
   - Message: "What is the content of the document?"
   - Response: A generated response based on the PDF content.

### Testing Endpoints

1. **Test PDF Upload**: Use the `/api/upload/` endpoint to upload a PDF and get its extracted text stored.
2. **Test Real-Time QA**: Open a WebSocket connection to `/ws/qa/` and start asking questions about the uploaded PDF.

### Rate Limiting

If rate limiting is enabled, you can make up to 5 requests per minute for each user.

- This can be modified by adjusting the `@limiter.limit("5/minute")` decorator in the FastAPI code.
- For WebSocket, the rate limit is set to 10 messages per minute per user.

## Project Structure

```
.
├── app/
│   ├── main.py                # FastAPI main entry point
│   ├── models.py              # SQLAlchemy models (Document, ExtractedText)
│   ├── routes/                # API endpoints (upload, qa)
│   │   ├── upload.py          # File upload and processing logic
│   │   ├── websocket.py       # WebSocket QA logic
│   ├── services/              # Business logic (PDF processing, NLP processing)
│   │   ├── pdf_processing.py  # PDF text extraction logic
│   │   ├── nlp_processing.py  # NLP query processing logic
│   ├── requirements.txt       # Project dependencies             
└── uploaded_pdfs/             # Folder to store uploaded PDFs

```
