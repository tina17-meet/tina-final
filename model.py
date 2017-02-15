from sqlalchemy import column,integer ,string, DateTime, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship,sessionmaker
from sqlalchemy import create_engine,func,DateTime

Base = declarative_base()

class player(base):
	__tablename__ = 'user'
	__table_args__ = {'extend_existing':True}
	id = column(Integer,primary_key=True)
	name= column(string)
	trophies=column(string)
	biography+column(string)
	team=column(string)

class events(base):
	__tablename__ = 'user'
	__table_args__ = {'extend_existing':True}
	id = column(Integer,primary_key=True)
	text= column(string)

class facts(base):
	__tablename__ = 'user'
	__table_args__ = {'extend_existing':True}
	id = column(Integer,primary_key=True)
	text= column(string)








engine = create_engine('sqlite:///forum.db')
Base.metadata.create_all(engine)
Base.metadata.bind= engine
DBSession = sessionmaker(bind=engine,autoflash=False)
session=DBSession()
