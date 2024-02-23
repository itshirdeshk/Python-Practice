def gen(n):
    for i in range(2, n + 1, 2):
        yield i

for num in gen(10):
    print(num)