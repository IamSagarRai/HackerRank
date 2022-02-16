def iss_leap(year):
    leap = False
    
    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True
    return leap
    
years = int(input("Enter leap year: "))
print (iss_leap(years))