from requests import get, post, delete

print(post('http://127.0.0.1:8000/api/v2/news',
           json={
               'title': 'Заголовок через RESTApi',
               'content': 'Новость через RESTApi',
               'user_id': 1,
               'is_private': False
           }).json())
