#!/usr/bin/env python3
"""auth"""
from typing import Union
from user import User
import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4


def _hash_password(password: str) -> str:
    """_hash_password"""
    salted_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return salted_password


def _generate_uuid() -> str:
    """_generate_uuid"""
    return str(uuid4())


class Auth:
    """auth class"""

    def __init__(self):
        """init"""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """register_user"""
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            new_registry = self._db.add_user(email, _hash_password(password))
            return new_registry
        else:
            raise ValueError(f'User {email} already exists')

    def valid_login(self, email: str, password: str) -> bool:
        """valid_login"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        return bcrypt.checkpw(password.encode(), user.hashed_password)

    def create_session(self, email: str) -> str:
        """create_session"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(self, session_id: str) -> Union[str, None]:
        """get_user_from_session_id"""
        try:
            return self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """destroy_session"""
        if user_id:
            self._db.update_user(user_id, session_id=None)

    def get_reset_password_token(self, email: str) -> str:
        """get_reset_password_token"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError
        token = _generate_uuid()
        self._db.update_user(user.id, reset_token=token)
        return token

    def update_password(self, reset_token: str, password: str) -> None:
        """update_password"""
        if not reset_token:
            return None
        if not password:
            return None
        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            raise ValueError
        hashed_pwd = _hash_password(password)
        self._db.update_user(
            user.id,
            hashed_password=hashed_pwd,
            reset_token=None)
