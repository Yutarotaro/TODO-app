from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from api.db import Base


class Assignee(Base):
	__tablename__ = "assignee"

	id = Column(Integer, primary_key=True)
	name = Column(String(50))#TODO: ,ForeignKey("todo.assignee_name"
	role = Column(String(50))
