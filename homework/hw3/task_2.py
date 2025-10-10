def LeapYear(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False
    
year = int(input("Enter a year: "))
if LeapYear:
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")