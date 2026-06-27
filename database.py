from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

db_url = "postgresql://drishti:password123@localhost:5433/shopie"
engine = create_engine(db_url)           # connects to PostgreSQL
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()               # all your models inherit this
session = SessionLocal()                # one global session (fine for learning)