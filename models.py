from sqlalchemy import String, Integer, Column

from database import Base

class User(Base):
    __tablename__ = "users"
    uid = Column(String, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    company_name = Column(String, index=True)
    email = Column(String, index=True)
    phone_no = Column(Integer, index=True)
    country_code =Column(Integer, index=True)

