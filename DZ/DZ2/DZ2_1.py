# Результат: 98,35,15,213,54,119
# объявляем  словарь 

ids = {
    'user1': [213, 213, 213, 15, 213],
    'user2': [54, 54, 119, 119, 119],
    'user3': [213, 98, 98, 35]
}

unique_labels = set()

for label in ids['user1']:
    unique_labels.add(label)

for label in ids['user2']:
    unique_labels.add(label)

for label in ids['user3']:
    unique_labels.add(label)

print(f"Результат: {unique_labels}")
