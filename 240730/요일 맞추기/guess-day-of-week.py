import datetime
weeks = ['Sun', 'Mon','Tue', 'Wed', 'Thu', 'Fri', 'Sat']
m1, d1, m2, d2 = map(int, input().split())

start_date = datetime.date(2011, m1, d1)
target_date = datetime.date(2011, m2, d2)

days_diff = (target_date - start_date).days
day_of_week = (days_diff+1) % 7
print(weeks[day_of_week])