'''Write a Python program that takes a student's marks in three subjects as input.
•	If the average is greater than or equal to 90, print "Grade: A".
•	If the average is between 80 and 89, print "Grade: B".
•	If the average is between 70 and 79, print "Grade: C".
•	Otherwise, print "Grade: Fail". '''
# Function to calculate the grade based on average marks
def calculate_grade(marks):
    average = sum(marks) / len(marks)

    if average >= 90:
        return "Grade: A"
    elif 80 <= average < 90:
        return "Grade: B"
    elif 70 <= average < 80:
        return "Grade: C"
    else:
        return "Grade: Fail"

# Main program
try:
    # Taking input from the user for three subjects
    marks = []
    for i in range(1, 4):
        mark = float(input(f"Enter marks for subject {i}: "))
        marks.append(mark)

    # Calculating and printing the grade
    grade = calculate_grade(marks)
    print(grade)

except ValueError:
    print("Invalid input! Please enter numeric values for marks.")
