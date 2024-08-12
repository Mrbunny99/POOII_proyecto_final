from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datos.models import Base

DATABASE_URL = 'mysql+pymysql://root:admin@localhost:3307/proyecto_final'

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
