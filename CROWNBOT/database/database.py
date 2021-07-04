import sqlalchemy.orm

from confess_server import ConfessServer
from server import Server
from sessions import make_sessions


def close_session(session: sqlalchemy.orm.Session, data_object):
    session.add(data_object)
    session.commit()
    session.close()


def get_confess_server():
    session = make_sessions()
    confess_server = session.query(ConfessServer)
    session.close()
    return confess_server.all()
