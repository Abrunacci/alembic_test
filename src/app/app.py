from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.app.models import Base

DB_STRING = 'postgresql://test:alembic@localhost:5432/alembic_test'

# DB CONFIGURATION
engine = create_engine(DB_STRING)

if __name__ == '__main__':
    Session = sessionmaker(bind=engine)
    db = Session()
    Base.metadata.create_all(engine)
