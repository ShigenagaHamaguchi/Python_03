import sys

from sqlalchemy import Column,String,Date,Integer
from database import Base,ENGINE


class Attendnum(Base):
    __tablename__ = "attendnum"
    entry_date = Column(Date,primary_key=True)
    seq = Column(Integer,primary_key=True,autoincrement=True)
    adult = Column(Integer)
    child = Column(Integer)
    def __init__(self,entry_date,seq,adult,child):
        self.entry_date = entry_date
        self.seq = seq
        self.adult = adult
        self.child = child
def main(args):
    Base.metadata.create_all(bind=ENGINE)
if __name__ == "__main__":
    main(sys.argv)
