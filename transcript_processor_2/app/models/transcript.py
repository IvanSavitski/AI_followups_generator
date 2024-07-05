from pydantic import BaseModel
from typing import List

class Transcript(BaseModel):
    timestamp: str
    speaker: str
    content: str

class TranscriptInput(BaseModel):
    transcript: List[Transcript]
