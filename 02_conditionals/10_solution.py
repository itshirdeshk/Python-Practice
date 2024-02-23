pet = str(input("Enter your pet's species :\t"))
age = int(input("Enter your pet's age :\t"))

if pet == "Dog":
    if age < 2:
        food = "Puppy food"
    elif age > 5:
        food = "Senior dog food"
elif pet == "Cat":
    if age < 2:
        food = "Cat baby food"
    elif age > 5:
        food = "Senior cat food"
else:
    print("Currently, I only have info about 2 pet species - Dog and Cat...")
    exit()
    
print("Recommended pet food is ", food)