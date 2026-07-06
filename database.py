from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "postgresql://postgres:admin@localhost:5432/postgres"

engine = create_engine(db_url)
session = sessionmaker(bind=engine, autocommit=False, autoflush=False)