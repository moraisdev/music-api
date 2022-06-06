from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Consults(Base):
    __tablename__ = "consults"
    id = Column(Integer, primary_key=True, autoincrement=True)
    lat = Column(String)
    long = Column(String)
