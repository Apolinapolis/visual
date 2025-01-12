import requests
import json

# Вызов API и сохранине ответа
url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
r = requests.get(url)
print(f'Status code: {r.status_code}')

# Анализ структуры данных
response_dict = r.json()
readable_file = 'CSV_format/data/readable_hh_data.json'
with open(readable_file, 'w') as f:
    json.dump(response_dict, f, indent=4)