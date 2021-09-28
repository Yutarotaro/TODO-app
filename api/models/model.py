from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, Boolean
from sqlalchemy.orm import relationship

from api.db import Base


class Assignee(Base):
	__tablename__ = "assignee"

	assignee_id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String(50))#TODO: ,ForeignKey("todo.assignee_name"
	role = Column(String(50))

class Todo(Base):
	__tablename__ = "todo"

	todo_id = Column(Integer, primary_key=True, autoincrement=True)
	content = Column(String(50))
	deadline = Column(TIMESTAMP)
	is_done = Column(Boolean)
	created_at = Column(TIMESTAMP)
	updated_at = Column(TIMESTAMP)
	deleted_at = Column(TIMESTAMP)

class TodoAssignee(Base):
	__tablename__ = "todo_assignee"

	todo_assignee_id = Column(Integer, primary_key=True, autoincrement=True)
	todo_id = Column(Integer)
	assignee_id = Column(Integer)
