from app.models.transcript import TranscriptInput


def chunk_transcript(transcript: TranscriptInput, chunk_size: int = 3000) -> list[str]:
    chunks = []
    current_chunk = ""
    current_length = 0
    
    for entry in transcript.transcript:
        entry_length = len(entry.content)
        
        # Проверяет, не превысит ли добавление этой записи размер чанка.
        if current_length + entry_length > chunk_size:
            # Если да, завершит текущий чанк и начните новый.
            chunks.append(current_chunk)
            current_chunk = entry.content
            current_length = entry_length
        else:
            # Если нет, добавит запись в текущий чанк.
            if current_chunk:
                current_chunk += " " + entry.content
            else:
                current_chunk = entry.content
            current_length += entry_length
    
    # Добавит последний чанк, если он не пуст.
    if current_chunk:
        chunks.append(current_chunk)
    
    return chunks
