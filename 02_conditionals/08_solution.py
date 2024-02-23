password = str(input("Enter your password :\t"))
length = len(password)

if length < 6:
    print("Weak password")
elif length < 11:
    print("Medium password")
else:
    print("Strong password")