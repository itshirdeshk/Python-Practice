coffee_order = str(input("Enter your Coffee size (Small, Medium, Large) :\t"))

extra_shot = bool(input("Do you want an Extra shot (True/False)"))

if extra_shot == True:
    coffee = coffee_order + " coffee with an extra shot"
else:
    coffee = coffee_order + " coffee without an extra shot"
    
print(coffee)