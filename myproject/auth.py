from passlib.context import CryptContext
import crud
from sqlalchemy.orm import Session

pwd_context = CryptContext(schemes=["argon2", "bcrypt"], deprecated="auto")


def get_password_hash(password):
    return pwd_context.hash(password)