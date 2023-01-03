def sunday_1st():
    answer = 0
    day_diff = 365 # 'days' difference between 1900.1.1 and 1st day of the corresponding month
    for year in range(1901, 2001):
        for month in range(1, 13):
            # Check if the first day of the month is Sunday
            if day_diff % 7 == 6:
                answer += 1
            # Add the number of days in the month to 'day_diff'
            if month in [1, 3, 5, 7, 8, 10, 12]:
                day_diff += 31
            elif month in [4, 6, 9, 11]:
                day_diff += 30
            elif year % 4 == 0 and year % 100 != 0:
                day_diff += 29
            else:
                day_diff += 28
    return answer

if __name__ == '__main__':
    print('Answer:', sunday_1st(), 'Sundays fell on the first of the month during the twentieth century.')