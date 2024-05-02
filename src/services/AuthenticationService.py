import os
from datetime import timedelta, datetime, timezone
from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import hashlib
from jose import jwt, JWTError
from pydantic import ValidationError
from redis import Redis

from src.models.Account.Usr import Usr
from src.repositories.UsrRepository import UsrRepository
from src.services.ServiceAbstract import ServiceAbstract
from src.utils.password_validators import validate_password, verify_password


_oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

redis_cache = Redis(host='redis', port=6379, db=0, single_connection_client=False)

class AuthenticationService(ServiceAbstract):
    def __init__(self):
        super().__init__(UsrRepository)
        self.ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
        self.__SECRET_KEY: str = os.getenv("SECRET_KEY")
        self.__ENCRYPTION_ALGORITHM: str = os.getenv("ENCRYPTION_ALG")

    def create_token(self, username: str) -> str:
        try:
            to_encode = {"sub": username}
            access_token_expires = datetime.now(timezone.utc) + timedelta(minutes=self.ACCESS_TOKEN_EXPIRE_MINUTES)
            to_encode.update({"exp": access_token_expires})
            encoded_jwt = jwt.encode(to_encode, self.__SECRET_KEY, algorithm=self.__ENCRYPTION_ALGORITHM)
        except Exception as e:
            raise Exception("Token creation error: ", e)
        return encoded_jwt

    def authorise(self, username: str, password: str) -> Usr:
        user: Usr = self.__get_user(username)
        if not user:
            raise Exception("User not found")
        validate_password(password)
        verify_password(user.password, self.__hash_password(password))
        return user

    def authenticate(self, username: str, password: str) -> Usr:
        user = self.__get_user(username)
        if user:
            raise Exception("User already exists")

        validate_password(password)
        hashed_password = self.__hash_password(password)
        try:
            user: Usr = Usr(username=username, password=str(hashed_password), _id=None)
        except Exception as e:
            raise Exception("Error creating a User: ", e)

        user_id = self.repository.create(user)
        if not user_id:
            raise Exception("Error storing User information in the database")

        user: Usr = self.repository.find_by_id(user_id)
        if not user:
            raise Exception("Error finding User information in the database after creation")
        return user

    def verify_token(self, token: Annotated[str, Depends(_oauth2_scheme)]) -> bool:
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, self.__SECRET_KEY, algorithms=[self.__ENCRYPTION_ALGORITHM])
            username: str = payload.get("sub")
            if username is None:
                raise credentials_exception
        except JWTError:
            raise credentials_exception
        # check cache
        print("verifying token:")
        # TODO read from "Create an index. In this example, all JSON documents with the key prefix user: will be indexed. For more information, see Query syntax."
        #   link: https://redis.io/docs/latest/develop/connect/clients/python/
        if redis_cache.get(username):
            return redis_cache.get(username) == token
        else:
            redis_cache.set(username, token)
            # redis_cache.set(username, token, exp=self.ACCESS_TOKEN_EXPIRE_MINUTES)
        user = self.__get_user(username=username)

        if user is None:
            raise credentials_exception
        return True

    def get_all(self):
        return self.repository.find_all()

    def get_by_id(self, account_id: str) -> Usr | None:
        return self.repository.find_by_id(account_id)

    def change_password(self, username, password):
        pass

    def __get_user(self, username: str) -> Usr | None:
        user = self.repository.find_one_by({"username": username})
        return user

    def __hash_password(self, password: str) -> str:
        try:
            hash_object = hashlib.sha256()
            hash_object.update(self.__SECRET_KEY.encode() + password.encode())
            hash_password = hash_object.hexdigest()
            return hash_password
        except TypeError as e:
            raise ValidationError(f"Password hashing error: {e}")
