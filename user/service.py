import sqlalchemy
from sqlalchemy.orm import Session
from user.models import User, UserCreate, UserUpdate

from sqlalchemy.sql.expression import or_


def get(*, db_session: Session, username: str = None, email: str = None) -> User:
    condition = or_(User.username == username, User.email == email)
    stmt = sqlalchemy.select(User).where(condition)
    return db_session.execute(stmt).scalar()


def create(*, db_session: Session, user_in: UserCreate) -> User:
    stmt = sqlalchemy.insert(User).values(username=user_in.username, email=user_in.email, password=user_in.password)
    result = db_session.execute(stmt)
    db_session.commit()
    # user_id = result.inserted_primary_key[0]
    user = get(db_session=db_session, username=user_in.username)
    return user


def update(*, db_session: Session, user: User, user_in: UserUpdate) -> User:
    stmt = (
        sqlalchemy.update(User)
        .where(User.id == user.id)
        .values(username=user_in.username, email=user_in.email, password=user_in.password)
    )
    db_session.execute(stmt)
    db_session.commit()
    db_session.refresh(user)
    return user


def delete(*, db_session: Session, user: User):
    stmt = sqlalchemy.delete(User).where(User.id == user.id)
    db_session.execute(stmt)
    db_session.commit()
