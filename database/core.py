from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from settings import settings

# docker run --detach --name fastnotes-db --env MARIADB_ROOT_PASSWORD=secret -p 3306:3306 mariadb:latest
# docker start fastnotes-db
# docker stop fastnotes-db

engine = create_engine(settings.get_db_url())
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
