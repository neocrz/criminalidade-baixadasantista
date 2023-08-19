import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create an SQLite database in memory
engine = create_engine('sqlite:///db.sqlite') #, echo=True

Base = declarative_base()



Session = sessionmaker(bind=engine)

