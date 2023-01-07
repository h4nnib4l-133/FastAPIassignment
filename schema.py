from pydantic import BaseModel

class GetUser(BaseModel):
    first_name:str
    last_name:str 
    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    company_name: str
    email: str
    phone_no: str
    country_code: str

    class Config:
        orm_mode = True

class UserGet(BaseModel):
    uid:str
    first_name: str
    last_name: str
    company_name: str
    email: str
    phone_no: str
    country_code: str

    class Config:
        orm_mode = True