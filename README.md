How to run
1) parser
python main.py

2) transcript_processor_2:   
cd....
python -m venv venv 
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload

in postman POST http://127.0.0.1:8000/api/v1/generate_followup
body - raw json - insert transcript.json
