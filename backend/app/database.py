from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine("postgresql://azegha:Azegha2002#@db:5432/social_network_generator")
Session = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()