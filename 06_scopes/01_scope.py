# username = "chaiaurcode"

# def func():
#     username = "chai"
#     print(username)

# print(username)
# func()

# x = 99
# def func2(y):
#     return x + y

# result = func2(1)
# print(result)

def f1():
    x = 88
    def f2():
        print(x)
    return f2

myResult = f1()
# myResult()

def chaicoder(num):
    def actual(x):
        return x ** num
    return actual

f = chaicoder(2)
print(f(4))