from sqlalchemy.orm import session
from macapa.controller import create_user as ma_create
from varejao.controller import create_user as va_create
from db import get_db

session = get_db('macapa')
ma_create(db=session, user={'email': 'renatonerijr@gmail.com', 'password': '123'})

session = get_db('varejao')
va_create(db=session, user={'email': 'renatonerijr@gmail.com', 'password': '123'})