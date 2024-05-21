
from database import session
from tables import Holiday
from datetime import date

holiday = session.query(Holiday).filter_by(holi_date=date(2024,8,11)).delete()

session.commit()