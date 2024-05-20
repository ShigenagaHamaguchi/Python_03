
from database import session
from tables import Holiday


holiday0 = Holiday("2024/11/11","生誕祭")
holiday1 = Holiday("2024/7/15","海の日")
holiday2 = Holiday("2024/8/11","山の日 ")

session.add(holiday0)
session.add(holiday1)
session.add(holiday2)
session.commit()

holidays = session.query(Holiday).all()
print(holidays)
