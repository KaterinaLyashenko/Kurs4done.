from project.dao import GenresDAO, MovieDAO, DirectorDAO, UserDAO

from project.services import GenresService, MoviesService, DirectorsService, UsersService
from project.setup.db import db

# DAO
genre_dao = GenresDAO(db.session)
director_dao = DirectorDAO(db.session)
movie_dao = MovieDAO(db.session)
user_dao = UserDAO(db.session)

# Services
genre_service = GenresService(dao=genre_dao)
director_service = DirectorsService(dao=genre_dao)
movie_service = MoviesService(dao=genre_dao)
user_service = UsersService(dao=user_dao)