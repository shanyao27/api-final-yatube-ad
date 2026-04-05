# Yatube API

API для социальной сети Yatube. Позволяет создавать посты, комментарии и подписываться на авторов.

## Установка

```bash
git clone git@github.com:shanyao_27/api_final_yatube.git
cd api_final_yatube
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver

### Примеры запросов

Результат POST-запроса с токеном пользователя на добавление нового поста:

1. Пример запроса:

```
{
    "text": "Текст",
    "group": 1
}
```

2. Пример ответа:

```
{
    "id": 1,
    "text": "Текст",
    "author": "Имя",
    "image": null,
    "group": 1,
    "pub_date": "2022-05-11T08:47:10.084572Z"
}
```