def sum_of_even_numbers(n):
    sum_even = 0
    for i in range(2, n + 1, 2):
        sum_even += i
    return sum_even

def main():
    while True:
        try:
            n = int(input("Enter a positive integer: "))
            if n > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid positive integer.")

    sum_even = sum_of_even_numbers(n)
    print("The sum of all even numbers between 1 and", n, "is:", sum_even)

if __name__ == "__main__":
    main()
