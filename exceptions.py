try:   
    students = {"Nora":15, "Gino":30}
    Student_name=input("Enter the name of student")
    if Student_name in students: # the program takes student_name as the key. 
        print(f"The age of student is {students[Student_name]}")
    else:
        raise KeyError(f"keyError {Student_name} is not among students")
except KeyError as wrong_name:
    print(f"Error: {wrong_name}")
# Dictionary containing student names and their grades
student_grades = {'Alice': 85, 'Bob': 92, 'Charlie': 78}

# Misspelling the variable name
student_name = 'Alex'

# Attempting to print the grade of the student using the misspelled variable
print(student_grades[student_name])  # Misspelled 'student_name' as 'student_nmae'

# index error occurs when one reference indes that is beyonnd the list
a=[7,8,4,5,3,9,10]
print(a[8])

# zero division error

a=int(input("Enter the value of 'a'"))
b=int(input("Enter the value of 'b'"))
try:
    if a<0:
        raise ValueError("Error!, 'a' can only have positive value")
    if b==0:
        raise ValueError("Error!, 'b' can't be zero[o]")
    else:
     c=a/b
     print(a/b)
except ValueError as Error:
 print("Error:", Error)


try:
    num_str = input("Enter a number: ")
    num = int(num_str)
    result = 10 / num
except ValueError: # enter abf say
    print("Invalid input: Please enter a valid integer.")
except ZeroDivisionError: # enter zero
    print("Cannot divide by zero.")

 # ValueError occurs when you want to convert string to integer
A=int("Hello")
print(A) # The output of this code is ValueError 

try:
    A = int(input("Enter the value of A"))
except ValueError as ve:
    print("Invalid input for A. Please enter an integer value.")
    A = int(input("Enter the value of A again:"))

try:
    B = int(input("Enter the value of B"))
except ValueError as ve:
    print("Invalid input for B. Please enter an integer value.")
    B = int(input("Enter the value of B again:"))

try:
    C = A / B
    print(C)
except ZeroDivisionError as ze:
    print("Cannot divide by zero:", ze)

A=int(input("Enter the value of A"))
B=int(input("Enter the value of B"))
try:
    C=A/B # Not that there must be a code inside try: block for the exception to be captured and handled accordingly
    print(C)
except (ValueError, ZeroDivisionError) as e:
    print("Error:", e)

# Partial exception handling
try:
    A=int(input("Enter the value of A"))
except ValueError as ve:
    print(f"Please Enter the valid value of A")
    A=int(input("Enter another value of A"))
try:
       B=int(input("Enter the value of B"))
except ValueError as ve:
    print(f"Please Enter the valid value of B")
    B=int(input("Enter another value of B"))
try:
     C=A/B
     print(C)
except ZeroDivisionError as ve:
     print("Cannot divide by Zero", ve)

# You can handle exeption from within a try: block even if you call fuction previously defined and no 
# exeption defined to them 
def g(index):
    a = "Hello, World!"
    return a[index]

def f():
    try:
        g(50)
    except IndexError:
        print("IndexError caught in f")

f()  # Call f to execute the try-except block


try:
    x = 1 / 0
except Exception as e:
    exception_instance = e  # Assigning the exception object to a variable
    print("Exception:", exception_instance)  # Printing the default description of the exception
    print("Arguments:", exception_instance.args)  # Accessing the arguments of the exception

import pdb; pdb.set_trace()
a=12; b=5
print(a+b)