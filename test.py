from requests import get, post, put, delete

# Проверки API на метод GET
# print(get('http://127.0.0.1:8000/api/news').json())
# print(get('http://127.0.0.1:8000/api/news/1').json())
# print(get('http://127.0.0.1:8000/api/news/6').json())
# print(get('http://127.0.0.1:8000/api/news/r').json())

# Проверки API на метод POST
# print(post('http://127.0.0.1:8000/api/news').json())
# print(put('http://127.0.0.1:8000/api/news/4',
#           json={
#               'title': 'Изменено через API',
#               'content': 'Содержание изменено через API',
#               'user_id': 3,
#               'is_private': False
#           }).json())

print(delete('http://127.0.0.1:8000/api/news/7').json())
