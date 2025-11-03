from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///data/database.db"  # Caminho para o banco de dados

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    balance = Column(Float, default=0.0)

def get_engine():
    return create_engine(DATABASE_URL)

def create_tables():
    engine = get_engine()
    Base.metadata.create_all(engine)

def get_session():
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    return Session()