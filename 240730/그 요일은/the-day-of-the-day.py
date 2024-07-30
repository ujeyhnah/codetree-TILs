from datetime import date, timedelta

def count_weekday_occurrences(m1, d1, m2, d2, A):
    weekday_map = {"Mon": 0, "Tue": 1, "Wed": 2, "Thu": 3, "Fri": 4, "Sat": 5, "Sun": 6}
    
    target_weekday = weekday_map[A]
    
    start_date = date(2024, m1, d1)
    end_date = date(2024, m2, d2)
    
    count = 0
    
    current_date = start_date
    while current_date <= end_date:
        if current_date.weekday() == target_weekday:
            count += 1
        current_date += timedelta(days=1)
    
    return count

m1, d1, m2, d2 = map(int, input().split())
A = input()
result = count_weekday_occurrences(m1, d1, m2, d2, A)
print(result)