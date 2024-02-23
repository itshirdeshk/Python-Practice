num = int(input("Enter the number: \t"))
fact = 1

while num > 0:
    fact *= num
    num -= 1
    
print(fact)