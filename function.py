# to define a function we start with def and then followed by an agrument.
def greet(first_name, Second_name):
    print("Hi ", first_name, Second_name)
    print("Welcome aboard")


greet("Peter", "John")
def greet(first_name, second_name):
    print(f"Hi {first_name} {second_name}")
    print("Welcome aboard")

   
greet("Peter", "John")

def get_greetings(name):
    return f"Hi {name}"

message=get_greetings("John")
print(message)

def Arithmetrically_sum(*Num):
    sum=0
    for Numbers in Num:
        sum=sum+Numbers
    print(sum)

Arithmetrically_sum(1,2,3,4,5,6,7,8,9)

def save_user(**user):
    print(user)

save_user(id=1, name="John", age=34) 




def student_20_and_below(dictionery):
    Max_age=20
    Empty_key=[]
    for key,value in dictionery.items():
        if value<Max_age:
           Empty_key.append(key) # at this point the code has already finished looping
    if Empty_key: # get out of loop to check if the list is empty, Nothing has been appended
        print(f'Student 20 and older = {Empty_key}')
    else:
        print("All students are older")
A=student_20_and_below({"John":34, "Janeth":32, "Halima":20, "Japhet":12, "Humphery":18, "Simon":15})

my_list = [1, 2, 3]
result = my_list.append(4)

print(my_list)  # Output: [1, 2, 3, 4] 
print(result)   # Output: None because the append() method does not retun the modified list

        