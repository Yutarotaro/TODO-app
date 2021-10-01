from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, Boolean
from sqlalchemy.orm import relationship
import datetime
from sqlalchemy.sql.sqltypes import TIME

from sqlalchemy.sql.type_api import NULLTYPE

from api.db import Base


class Assignee(Base):
	__tablename__ = "assignee"

	assignee_id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String(50))
	role = Column(String(50))
	children = relationship("AssignTodo")

class Todo(Base):
	__tablename__ = "todo"

	todo_id = Column(Integer, primary_key=True, autoincrement=True)
	content = Column(String(50))
	deadline = Column(TIMESTAMP)
	is_done = Column(Boolean)
	created_at = Column(TIMESTAMP)
	updated_at = Column(TIMESTAMP)
	deleted_at = Column(TIMESTAMP)
	children = relationship("AssignTodo")

class AssignTodo(Base):
	__tablename__ = "todo_assignee"

	todo_assignee_id = Column(Integer, primary_key=True, autoincrement=True)
	todo_id = Column(Integer, ForeignKey('todo.todo_id'))
	assignee_id = Column(Integer, ForeignKey('assignee.assignee_id'))
