from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "sqlite:////collars.db"

engine = create_engine(
    DATABASE_URL
)

DBSession = sessionmaker(autocommit=False,
                         autoflush=False,
                         bind=engine
                         )

BaseDBModel = declarative_base()