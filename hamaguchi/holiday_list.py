
from database import session
from tables import Holiday
from attendnum import Attendnum
from datetime import date

def insert_holiday(day:Holiday):
    session.add(day)
    session.commit()
    return

def get_holidays() ->date:
    holi_date=session.query(Holiday.holi_date).all()
    print(holi_date)
    return list(map(lambda x:x[0],holi_date))


def count_attendnum(day:date):
    print(session.query(Attendnum).filter_by(entry_date=day).count())
    return session.query(Attendnum).filter_by(entry_date=day).count()