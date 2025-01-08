#Day-5 assignment question-1

n = int(input("Enter a positive integer: "))

for i in range(1, n + 1):
    print(i)

sum = 0
i = 1
while i <= n:
    sum += i
    i += 1

print("Sum:", sum)

#Day-5 assignment question-2

def calculate_square(n):
    return n * n

n = int(input("Enter a positive integer: "))
result = calculate_square(n)
print("The square of", n, "is", result)
