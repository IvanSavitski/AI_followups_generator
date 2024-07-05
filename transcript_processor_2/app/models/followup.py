from pydantic import BaseModel
from typing import List

class Followup(BaseModel):
    topic: str

class FollowupResponse(BaseModel):
    followups: List[Followup]
