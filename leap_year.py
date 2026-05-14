year = int(input("enter year:"))

if ((year % 400 == 0) or (year % 4 == 0) and (year % 100 != 0)) :
    print("This year is a leapyear")

else :
    print("This year is not a leapyear")