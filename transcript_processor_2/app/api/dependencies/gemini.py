from pydantic import BaseModel
from app.core.config import settings
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from gemini import Gemini
import google.generativeai as genai
from llamaapi import LlamaAPI



llama = LlamaAPI('................................................................')

def fetch_gemini_insights(transcript_chunk: str) -> dict:

    promt = "\n\n\n" + "Ответ генерируй на русском. Для следующего чанка данных с транскрипта встречи сгенерируй followup: " + "\n" + transcript_chunk + "\n" + """Есть транскрипт встречи, сгенерируй для него followup - протокол встречи, в нем должна содержаться самая важная информация (итоги, договоренности, ключевые решения), сгруппированная по темам. Например:

    Обновление продукта:
        — новая страница подписки
        — улучшено саммари в отчете
    Конференции и встречи:
        — в среду встреча с Х в 20:00
        — с конференции Y пришло 2 новых клиента"
    """
    print(promt)
    

    api_request_json = {
    "model": "llama3-70b",
    "messages": [
            {"role": "system", "content": "Ты отвечающий на русском языке лама ассистент."},
            {"role": "user", "content": promt},
        ]
    }

    # Make your request and handle the response
    followup_response = llama.run(api_request_json)

    followup_content = followup_response.json()["choices"][0]["message"]["content"]
    print(followup_content)
    return followup_content
