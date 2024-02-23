n = int(input("Enter the nunmber :\t"))

for i in range(1, 11):
    if(i == 5):
        continue
    else:
        print(n, "X", i, "=", i * n)
        
