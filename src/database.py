from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

DATABASE_URL = "sqlite+aiosqlite:////./collars.db"

#engine = create_engine(
#    DATABASE_URL, pool_pre_ping=True
#)
engine = create_async_engine(DATABASE_URL)
DBSession = async_sessionmaker(engine, expire_on_commit=False)

#DBSession = sessionmaker(autocommit=False,
#                         autoflush=False,
 #                        bind=engine
  #                       )

BaseDBModel = declarative_base()

