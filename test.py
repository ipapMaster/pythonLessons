from requests import get

print(get('http://127.0.0.1:8000/api/news').json())
