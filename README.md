# Проект API_Yatube (API)

## Описание

API разработан для учебного проекта Yatube на DRF. API позволяет аутентифицированным пользователям управлять своим контентом. Анонимный пользователь есть доступ только на чтение ограниченной информации.

## Применяемые технологи

[![Python](https://img.shields.io/badge/Python-3.7-blue?style=flat-square&logo=Python&logoColor=3776AB&labelColor=d0d0d0)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-2.2.16-blue?style=flat-square&logo=Django&logoColor=3776AB&labelColor=d0d0d0)](https://docs.djangoproject.com/en/2.2/)
[![Django REST framework](https://img.shields.io/badge/Django_REST_framework-3.12.4-blue?style=flat-square&logo=Django&logoColor=3776AB&labelColor=d0d0d0)](https://www.django-rest-framework.org/)
[![djoser](https://img.shields.io/badge/djoser-2.1.0-blue?style=flat-square&logoColor=3776AB&labelColor=d0d0d0)](https://djoser.readthedocs.io/en/latest/)
[![Pillow](https://img.shields.io/badge/Pillow-8.3.1-blue?style=flat-square&logoColor=3776AB&labelColor=d0d0d0)](https://pillow.readthedocs.io/en/stable/)

## Установка

Клонировать репозиторий и перейти в него в командной строке:

```python
git clone https://github.com/yandex-praktikum/kittygram.git
```

Cоздать и активировать виртуальное окружение:

```python
python3 -m venv env
```

```python
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```python
python3 -m pip install --upgrade pip
```

```python
pip install -r requirements.txt
```

Выполнить миграции:

```python
python3 manage.py migrate
```

Запустить проект:

```python
python3 manage.py runserver
```


## Примеры запросов к API

#### Получение публикаций

Получить список всех публикаций. При указании параметров **limit** и **offset** выдача должна работать с пагинацией.

**GET**-запрос:

```
http://127.0.0.1:8000/api/v1/posts/?limit=2&offset=4
```

Ответ:

```json
{
    "count": 10,
    "next": "http://127.0.0.1:8000/api/v1/posts/?limit=2&offset=6",
    "previous": "http://127.0.0.1:8000/api/v1/posts/?limit=2&offset=2",
    "results": [
        {
            "id": 6,
            "author": "user_a",
            "text": "post 6",
            "image": null,
            "pub_date": "2022-03-18T12:06:06.748759Z",
            "group": 1
        },
        {
            "id": 5,
            "author": "user_a",
            "text": "post 5",
            "image": null,
            "pub_date": "2022-03-18T12:06:04.428759Z",
            "group": 1
        }
    ]
}
```


#### Получение публикации

Получение публикации по **id**.

**GET**-запрос:

```
http://127.0.0.1:8000/api/v1/posts/{id}/
```

Ответ:

```json
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```


#### Создание публикации

Добавление новой публикации в коллекцию публикаций. Анонимные запросы запрещены.

**POST**-запрос:

```
http://127.0.0.1:8000/api/v1/posts/
```

Тело запроса:

```json
{
  "text": "string",
  "image": "string",
  "group": 0
}
```

Ответ:

```json
{
  "text": "string",
  "image": "string",
  "group": 0
}
```


#### Получение комментариев

Получение всех комментариев к публикации.

**GET**-запрос:

```
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
```

Ответ:

```json
[
  {
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
  }
]
```


#### Обновление комментария

Обновление комментария к публикации по **id**. Обновить комментарий может только автор комментария. Анонимные запросы запрещены.

**PUT**-запрос:

```
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/
```

Ответ:

```json
{
  "text": "string"
}
```


#### Удаление комментария

Удаление комментария к публикации по **id**. Обновить комментарий может только автор комментария. Анонимные запросы запрещены.

**DEL**-запрос:

```
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/
```


#### Список сообществ

Получение списка доступных сообществ.

**GET**-запрос:

```
http://127.0.0.1:8000/api/v1/groups/
```

Ответ:

```json
[
  {
    "id": 0,
    "title": "string",
    "slug": "string",
    "description": "string"
  }
]
```


#### Информация о сообществе

Получение информации о сообществе по **id**.

**GET**-запрос:

```
http://127.0.0.1:8000/api/v1/groups/{id}/
```

Ответ:

```json
{
  "id": 0,
  "title": "string",
  "slug": "string",
  "description": "string"
}
```


#### Подписки

Возвращает все подписки пользователя, сделавшего запрос. Анонимные запросы запрещены.

**GET**-запрос:

```
http://127.0.0.1:8000/api/v1/follow/
```

Ответ:

```json
{
  "id": 0,
  "title": "string",
  "slug": "string",
  "description": "string"
}
```


#### Получить JWT-токен

Получение JWT-токена.

**POST**-запрос:

```
http://127.0.0.1:8000/api/v1/jwt/create/
```

Тело запроса:

```json
{
  "username": "string",
  "password": "string"
}
```

Ответ:

```json
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY0Nzc2ODQyNSwianRpIjoiMWIyZjQ3OWJiOTliNGY3MGI3N2E1MGU4YjcyNTVlZmIiLCJ1c2VyX2lkIjoyfQ.64EYjgfKYokAafeFWEJxSt09YJ9KTe4xK66rDuitT5o",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQ3NzY4NDI1LCJqdGkiOiJlN2JjZjliMGU4N2Y0OTIyOTRkNjZmMDlmYjQ2ZmYzNyIsInVzZXJfaWQiOjJ9.zYPO8-MJfH71B-VdTQWSCeWWy7agnGhj2OK8uDZDPSk"
}
```

## Автор проекта
[Владислав Василенко](https://github.com/vasilekx)
