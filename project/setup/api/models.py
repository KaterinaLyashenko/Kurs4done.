from flask_restx import fields, Model

from project.setup.api import api

genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Мелодрама'),
})

director: Model = api.model('Режисер', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Кан Шин Хё'),
})

movie: Model = api.model('Фильм', {
    'id': fields.Integer(required=True, example=1),
    'title': fields.String(required=True, max_length=100, example='История о Кумихо'),
    'description': fields.String(required=True, max_length=100, example='История о девятихвостом лисе'),
    'trailer': fields.Integer(required=True, max_length=100, example='https://www.youtube.com/watch?v=gh9ATN5w7Rs'),
    'year': fields.Integer(required=True, example=2020),
    'rating': fields.Float(required=True, example=8.3),
    'genre': fields.Nested(genre),
    'director': fields.Nested(director)
})

user: Model = api.model('Пользователь', {
    'id': fields.Integer(required=True, example=1),
    'email': fields.String(required=True, max_length=100, example='some@mail.ru'),
    'password': fields.String(required=True, max_length=100, example='456721'),
    'name': fields.String(required=True, max_length=100, example='Simon'),
    'surname': fields.String(required=True, max_length=100, example='Some'),
})
