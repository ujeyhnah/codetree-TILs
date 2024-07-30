def count_weekday_occurrences(m1, d1, m2, d2, A):
    weekday_map = {
        "Mon": 0,
        "Tue": 1,
        "Wed": 2,
        "Thu": 3,
        "Fri": 4,
        "Sat": 5,
        "Sun": 6
    }
    
    days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    target_weekday = weekday_map[A]
    
    def calculate_day_of_week(month, day):
        days_since_start = sum(days_in_month[:month-1]) + (day - 1)
        return (days_since_start % 7) 
    
    current_month = m1
    current_day = d1
    occurrences = 0
    
    while (current_month < m2) or (current_month == m2 and current_day <= d2):
        if calculate_day_of_week(current_month, current_day) == target_weekday:
            occurrences += 1
        
        current_day += 1
        if current_day > days_in_month[current_month-1]:
            current_day = 1
            current_month += 1
    
    return occurrences

m1, d1, m2, d2 = map(int, input().split())
A = input()

print(count_weekday_occurrences(m1, d1, m2, d2, A))