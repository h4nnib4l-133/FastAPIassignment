from fastapi import FastAPI, HTTPException, Depends
from crud import add_user, delete_user, get_user, edit_user
from schema import UserCreate, GetUser, UserGet
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from database import Base, engine

Base.metadata.create_all(bind=engine)


#init db 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 

app = FastAPI()

@app.get("/")
def test():
    return {"message":"Hello"}

@app.post("/getuser", response_model=UserGet)
def getUser(user: GetUser, db:Session = Depends(get_db)):
    db_user = get_user(db, user)
    print(db_user)
    if db_user is None:
        raise HTTPException(status_code=404, detail = "Given user not found")
    else:
        return db_user
     
@app.post("/createuser", response_model=UserCreate)
def CreateUser(user:UserCreate, db:Session = Depends(get_db)):
    return add_user(db, user)

@app.post("/deleteuser/{uid}")
def DelUser(uid: str, db:Session =Depends(get_db)):
    delete_user(db, uid)
    return {"message":"user succesfully delete"}

@app.post("/edituser/{uid}")
def EditUser(uid:str, db:Session =Depends(get_db)):
    edit_user(db, uid)
    return {"message":"user entry edited"}
