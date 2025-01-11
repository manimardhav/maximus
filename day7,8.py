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

#find if the length of the string is even print as even
str = " do what i say to the world"
for word in str.split():
    if len(word) % 2 == 0:
        print(word)
# find the length of the string if the length of the string is

string ="there is a string"
for word in string.split():
    if len(word)>3:
        print(word[0])

string = "session is going to start"
print(string)
result = [i for i in string.split()if len(i) == 2] 
print(result)
print(string[::-1])

for i in (0,99):
    if i % 3 == 0:
        print("buzz")
    else:
        print("not divisible by 3")

for i in range(0,25):
    if i % 5 == 0:
        print("bigg")
    if i % 3 == 0:
        print("buzz")
    elif (i % 3 & i % 5 == 0):
        print("bigg buzz")