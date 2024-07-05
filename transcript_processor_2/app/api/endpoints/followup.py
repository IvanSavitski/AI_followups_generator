from fastapi import APIRouter, Body, HTTPException
from app.models.transcript import TranscriptInput
from app.models.followup import FollowupResponse
from app.services.transcript_service import chunk_transcript
from app.services.followup_service import generate_followups

router = APIRouter()


@router.post("/generate_followup")
def generate_followup(transcript: TranscriptInput = Body(...)):
    chunks = chunk_transcript(transcript)
    followups = []

    for chunk in chunks:
        try:
            followup = generate_followups(chunk)
            followups.append(followup)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        
    with open('save_followups_logs6_2.txt', 'a+') as file:
        for item in followups:
            str_item = str(item) + "\n"
            file.write(str_item)

    return followups