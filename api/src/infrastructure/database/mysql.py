from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

user = 'root'
password = 'password'
host = 'localhost'
db_name = 'python-flask-rest-api'


DB_URI = f'mysql+pymysql://{user}:{password}@{host}/{db_name}?charset=utf8'
engine = create_engine(DB_URI, encoding='utf-8', echo=True)

session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = session.query_property()

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()