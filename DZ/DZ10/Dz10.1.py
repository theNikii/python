import pandas as pd

file_path = 'events.json' 
with open(file_path, 'r', encoding='utf-8') as file:
    data = pd.read_json(file)

df = pd.json_normalize(data['events'])

print(df.head())

unique_signatures = df['signature'].unique()
print("Уникальные типы событий:", unique_signatures)

signature_counts = df['signature'].value_counts()
print("Количество событий по типам:\n", signature_counts)