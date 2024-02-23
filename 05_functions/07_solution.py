def multiSum(*num):
    sum = 0
    for i in num:
        sum += i
    return sum

print(multiSum(1, 2, 3, 4))