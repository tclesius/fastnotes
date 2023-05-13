from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# docker run --detach --name fastnotes-db --env MARIADB_ROOT_PASSWORD=secret -p 3306:3306 mariadb:latest
# docker start fastnotes-db
# docker stop fastnotes-db
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:secret@localhost:3306/fastnotes?charset=utf8mb4"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
