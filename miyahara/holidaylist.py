from database import session
from tables import Holiday

holidaylist = session.query(Holiday).all()

for holiday in holidaylist:
    print(holiday.holi_date,holiday.holi_text)
    print(type(holiday.holi_date))