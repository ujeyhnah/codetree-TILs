m1, d1, m2, d2 = map(int, input().split())
a = input()

def day_of_week(year, month, day):
    if month < 3:
        month += 12
        year -= 1
    k = year % 100
    j = year // 100
    day_of_week = (day + ((13 * (month + 1)) // 5) + k + (k // 4) + (j // 4) - (2 * j)) % 7
    return day_of_week

def count_weekday_occurrences(m1, d1, m2, d2, A):
    days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    weekday_index = {"Mon": 0, "Tue": 1, "Wed": 2, "Thu": 3, "Fri": 4, "Sat": 5, "Sun": 6}[A]
    
    total_days = 0
    for month in range(m1, m2 + 1):
        start_day = d1 if month == m1 else 1
        end_day = d2 if month == m2 else days_in_month[month - 1]
        total_days += end_day - start_day + 1
    
    start_weekday = day_of_week(2024, m1, d1)
    
    count = 0
    current_weekday = start_weekday
    for day in range(total_days):
        if current_weekday == weekday_index:
            count += 1
        current_weekday = (current_weekday + 1) % 7
    
    return count

result = count_weekday_occurrences(m1, d1, m2, d2, a)
print(result)