from sqlalchemy import create_engine
from api.models.model import Base
from sqlalchemy.orm import sessionmaker
import config

DB_URL = config.DB_URL
engine = create_engine(DB_URL, echo=True)

def reset_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
"""
class insert_data():
    def __init__(self):
      Session = sessionmaker(bind=engine)
      session = Session()

      insert_command = []
      insert_command.append([])
      


    def insert(self):
      session.add
"""







if __name__ == "__main__":
    reset_database()
