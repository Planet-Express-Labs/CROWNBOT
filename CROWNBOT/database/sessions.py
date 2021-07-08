from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlalchemy.orm
from CROWNBOT.config import DATABASE

engine = create_engine(DATABASE)

_MakeSession = sessionmaker(bind=engine)

Base = declarative_base()


def make_sessions():
    Base.metadata.create_all(engine)
    return _MakeSession()


def save_session(session: sqlalchemy.orm.Session, data_object):
    session.add(data_object)
    session.commit()
    session.close()

