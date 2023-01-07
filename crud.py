import random, string 
from fastapi import HTTPException
from schema import UserCreate, GetUser
from sqlalchemy.orm import Session
from models import User 

def get_random_string(seed, length):
    random.seed(seed)
    return ''.join(random.choice(string.ascii_uppercase) for i in range(length))

def add_user(db: Session, user:UserCreate):
    seed = user.phone_no
    uid = get_random_string(seed, 10)
    user_db = User(uid = uid,
                    first_name=user.first_name,
                    last_name=user.last_name,
                    company_name=user.company_name,
                    email=user.email,
                    phone_no=user.phone_no,
                    country_code=user.country_code)
    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return user_db

def get_user(db:Session, user:GetUser):
    print(user)
    if user.first_name and user.last_name:
        return db.query(User).filter(User.first_name == user.first_name).first()
    if user.last_name is None:
        return db.query(User).filter(User.first_name == user.first_name).first()
    if user.first_name is None:
        return db.query(User).filter(User.last_name == user.lastname).first()
        

def edit_user(db:Session, uid:str, user:UserCreate):
    user_db = db.query(User).filter(User.uid == uid)
    if user_db:
        pass
    else:
        return HTTPException(status_code=404, detail = "Given user not found")


def delete_user(db:Session, uid:str):
    db.query(User).filter(User.uid == uid).delete()
    db.commit()

