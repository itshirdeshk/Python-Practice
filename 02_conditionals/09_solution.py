year = int(input("Enter the year :\t202"))

if year % 400 == 0:
    print("Leap year...")
elif year % 4 == 0:
    if year % 100 == 0:
        print("Not a leap year...")
    else:
        print("Leap year...")
else:
    print("Not a leap year...")
