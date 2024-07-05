from app.models.followup import FollowupResponse, Followup
from app.api.dependencies.gemini import fetch_gemini_insights


def generate_followups(transcript_chunks: str) -> FollowupResponse:    
    followups = []

    insights = fetch_gemini_insights(transcript_chunks)
    followups.append(Followup(topic=insights))

    #дозапись в конец
    with open('save_followups_logs_6_1.txt', 'a+') as file:
        for item in followups:
            str_item = str(item) + "\n"
            file.write(str_item)

    return FollowupResponse(followups=followups)