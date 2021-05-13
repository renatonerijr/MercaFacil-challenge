from macapa import db as macapa_db
from varejao import db as varejao_db

# Dependency
def get_db_macapa():
    macapa_session = macapa_db.SessionLocal()
    try:
        return macapa_session
    finally:
        macapa_session.close()

def get_db_varejao():
    varejao_session = varejao_db.SessionLocal()
    try:
        return varejao_session
    finally:
        varejao_session.close()

def get_db(client: str):
    if client == 'macapa':
        return get_db_macapa()
    elif client == 'varejao':
        return get_db_varejao()
