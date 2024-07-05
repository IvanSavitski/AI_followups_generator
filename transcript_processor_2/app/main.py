from fastapi import FastAPI
from app.api.endpoints import followup

app = FastAPI()

app.include_router(followup.router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


# запуск 
# venv\Scripts\activate 
# uvicorn app.main:app --reload
# in postman POST http://127.0.0.1:8000/api/v1/generate_followup
# body - raw json - insert transcript.json