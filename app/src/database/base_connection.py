"""Creating a database connection."""

import os
from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
from contextlib import contextmanager
from app.src.database.base_config import DB_POOL_SIZE, DB_MAX_OVERFLOW, DB_POOL_TIMEOUT

load_dotenv()

Base = declarative_base()


def get_engine() -> Engine:
    DB_USER = os.environ.get('DB_USER')
    DB_PASSWORD = os.environ.get('DB_PASSWORD')
    DB_HOST = os.environ.get('DB_HOST', 'localhost')
    DB_PORT = os.environ.get('DB_PORT', '5432')
    DB_NAME = os.environ.get('DB_NAME', 'silo')

    if not all([DB_USER, DB_PASSWORD, DB_NAME]):
        raise EnvironmentError("Missing database credentials")

    DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    engine = create_engine(
        DATABASE_URL,
        pool_size=DB_POOL_SIZE,
        max_overflow=DB_MAX_OVERFLOW,
        pool_timeout=DB_POOL_TIMEOUT
    )

    return engine


@contextmanager
def get_db_session() -> Generator[Session, None, None]:
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        yield session
    except Exception as e:  # noqa: F841
        session.rollback()
        raise
    finally:
        session.close()
