first_sunday = 0

year = 1900
day = 0
month = 1
dayWk = 0


def end_of_month(month, day, year):
    if month == 9 or month == 4 or month == 6 or month == 11:
        if day == 30:
            return True
    elif month == 2:
        end_day = 28
        if year % 4 == 0:
            if year % 400 == 0:
                end_day = 29
            elif year % 100 == 0:
                end_day = 28
            else:
                end_day = 29
        if day == end_day:
##            print(month, day , year, dayWk, first_sunday)
            return True
    else:
        if day == 31:
            return True
    return False

while(True):
    if end_of_month(month, day, year):
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1
        day = 1
    else:
        day += 1
        
    if dayWk == 7:
        dayWk = 1
    else:
        dayWk += 1
    
    
    if year == 2001:
        break
    
    if day == 1 and dayWk == 7 and year > 1900:
        first_sunday += 1
##        print(month, day , year, dayWk, first_sunday)
print(month, day , year, dayWk, first_sunday)
print(first_sunday)
        
