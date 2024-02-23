fruit = "banana"
color = str(input("Enter the color of the Fruit :\t"))

if fruit == "banana":
    if color == "Green":
        print("Unripe")
    elif color == "Yellow":
        print("Ripe")
    else:
        print("Override")
else:
    print("Currently I only have info about Banana.")