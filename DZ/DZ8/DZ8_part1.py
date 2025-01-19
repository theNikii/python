#Задание 1. Получение данных из публичного API
#1. Выберите публичный API. Например, JSONPlaceholder.
#2. Напишите скрипт, который:
# отправляет GET-запрос к /posts,
# извлекает и выводит заголовки и тела первых 5 постов.


import requests

url = 'https://jsonplaceholder.typicode.com/posts'
response = requests.get(url)

if response.status_code == 200:
 
    posts = response.json()

    for post in posts[:5]:
        print(f"Заголовок: {post['title']}")
        print(f"Тело: {post['body']}")
        print('-' * 40)