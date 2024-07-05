# Running the Project

## 1. Parser

### python main.py

## 2. Transcript Processor 2

### cd ....
### python -m venv venv
### venv\Scripts\activate
### pip install -r requirements.txt
### uvicorn app.main:app --reload

## Then, in Postman, send a POST request to http://127.0.0.1:8000/api/v1/generate_followup with the transcript.json file in the request body (raw JSON format).
