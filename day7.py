def dev_dec(func):
    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)
    return inner

@dev_dec
def div(a, b):
    return a / b
print(div(2,4))

def dev_dec(func):
    def inner(a, b):
        if b == 0:
            print("Error: Division by zero is not allowed.")
            return
        if a < b:
            a, b = b, a
        return func(a, b)
    return inner

@dev_dec
def div(a, b):
    return a / b   
print(div(4, 0))

def dev_dec(func):
    def inner(a, b):
        if (a * b <= 20):
            print("error for multiplication")
            return
        return func(a, b)
    return inner

@dev_dec
def div(a, b):
    return a * b   
print(div(2,2))
print(div(5,5))