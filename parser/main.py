import json
import re

# Запуск с помощью python main.py
# Функция для чтения файла .txt и преобразования его в JSON
def txt_to_json(md_file_path, json_file_path):
    transcript = []

    with open(md_file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Используем регулярное выражение для разбора строки
            match = re.match(r'(\d+:\d+:\d+) Speaker (\w+): (.+)', line.strip())
            if match:
                timestamp, speaker, content = match.groups()
                transcript.append({
                    "timestamp": timestamp,
                    "speaker": speaker,
                    "content": content
                })

    payload = {"transcript": transcript}

    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(payload, json_file, ensure_ascii=False, indent=4)

# Путь к файлу .txt
file_path = 'интервью-павел-дуров.txt'

# Путь к выходному файлу .json
json_file_path = 'transcript.json'
txt_to_json(file_path, json_file_path)

print("Конвертация завершена!")
