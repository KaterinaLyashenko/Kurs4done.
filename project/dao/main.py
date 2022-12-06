from typing import List, Optional

from sqlalchemy import desc
from werkzeug.exceptions import NotFound

from project.dao.base import BaseDAO, T
from project.models import *
from project.tools.security import generate_password_hash


class GenresDAO(BaseDAO[Genre]):
    __model__ = Genre


class DirectorDAO(BaseDAO[Director]):
    __model__ = Director


class MovieDAO(BaseDAO[Movie]):
    __model__ = Movie

    def get_all_order_by(self, page: Optional[int] = None, filter = None) -> List[T]:
        stat = self._db_session.query(self.__model__)
        if filter:
            stat = stat.order_by(desc(self.__model__.year))
        if page:
            try:
                return stat.paginate(page, self._items_per_page).items
            except NotFound:
              return []
        return stat.all()


class UserDAO(BaseDAO[User]):
    __model__ = User

    def create(self, login, password):
        try:
            self._db_session.add(
                User(
                    email=login,
                    password=generate_password_hash(password)
                )
            )
            self._db_session.commit()
            print("Пользователь добавлен")
        except Exception as e:
            print(e)
            self._db_session.rollback()

    def get_user_by_login(self, login):
        try:
            stat = self._db_session.query(self.__model__).filter(self.__model__.email==login).one()
            return stat
        except Exception as e:
            print(e)
            return {}

    def update(self, login, data):
        try:
            self._db_session.query(self.__model__).filter(self.__model__.email == login).update(
                data
            )
            self._db_session.commit()
            print("Пользователь обновлен")
        except Exception as e:
            print(e)
            self._db_session.rollback()
