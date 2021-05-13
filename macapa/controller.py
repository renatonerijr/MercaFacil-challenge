from typing import Dict
from sqlalchemy.orm import Session
from macapa import models, schemas
from auth.controller import hash_password
import json


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: dict):
    hashed_password = hash_password(user['password'])
    db_user = models.User(email=user['email'], password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_contacts(db: Session, contacts: schemas.Contacts, user: dict):
    contacts = contacts.dict()
    added_contacts = []
    for contact in contacts['contacts']:
        db_contact = models.Contact(**contact, owner=user['id'])
        db.add(db_contact)
        db.commit()
        db.refresh(db_contact)
        added_contacts.append(db_contact)
    return added_contacts

def get_contacts(db: Session):
    return db.query(models.Contact).all()