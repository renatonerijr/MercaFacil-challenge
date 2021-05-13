from datetime import datetime, timedelta
from jose import jwt
import hashlib, binascii, os
from db import get_db

def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')

def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                provided_password.encode('utf-8'), 
                                salt.encode('ascii'), 
                                100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password

class AuthController:
    
    def generate_token(self, data: dict, expires_delta=None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + timedelta(minutes=expires_delta)
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, 'secret', algorithm="HS256")
        return encoded_jwt

    def verify_token(self, token: str):
        return jwt.decode(token, 'secret', algorithms=["HS256"])

    def authenticate_user(self, login, user_controller):
        session = get_db(login.client)
        user = user_controller.get_user_by_email(email=login.email, db=session)
        if user:
            if verify_password(user.password, login.password): 
                return user
            else:
                return
        else:
            return