num = int(input("Enter any number: "))

for i in range(2, num):
    if num % i == 0:
        print("Non Prime")
        exit()

print("Prime")