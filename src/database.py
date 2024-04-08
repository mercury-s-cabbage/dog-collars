from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
import src.users.models as models

DATABASE_URL = "sqlite:///./collars.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

DBSession = scoped_session(sessionmaker(autocommit=False,
                         autoflush=False,
                         bind=engine
                         ))

BaseDBModel = declarative_base()



