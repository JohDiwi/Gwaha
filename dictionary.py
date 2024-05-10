my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict.items()) # dict_items([('a', 1), ('b', 2), ('c', 3)])
print(my_dict.values()) # dict_values([1, 2, 3])
print(my_dict.keys()) # dict_keys(['a', 'b', 'c'])
print(my_dict)

print([keys for keys, value in my_dict.items()])

def get_keys_of_values(dictionary, value):
    keys_of_values = []
    my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
    for key, val in dictionary.items():
     if val == value:
        keys_of_values.append(key)
    return keys_of_values

# Example usage:

value_to_find = 6
keys = get_keys_of_values(my_dict, value_to_find)
print(f"The keys associated with the value {value_to_find} are: {keys}")

# Given dictionery item, names and age of student, we need to finf the name of studnts with 
# Age greater than the set value
# Method one using list compehension 
Students={"John":34, "Janeth":32, "Halima":20, "Japhet":12, "Humphery":18, "Simon":15}
Students_20_and_below=[keys for keys, values in Students.items() if values>20]
print(Students_20_and_below)

def student_20_and_below(dictionery):
    Max_age=20
    Empty_key=[]
    for key,value in dictionery.items():
        if value<Max_age:
           New_key=Empty_key.append(key)
        else:
           print("All students are older")
A=student_20_and_below({"John":34, "Janeth":32, "Halima":20, "Japhet":12, "Humphery":18, "Simon":15})
        
    
# in this code each time you start to iterate you start with Key_with_value33=[], you are not 
# keepin the track of items that you iterate thrrough
Students={"John":33, "Janeth":35, "Halima":20, "Japhet":12, "Humphery":18, "Simon":15}
for key,value in Students.items():
    Key_with_value33=[]
    if value ==33:
        Key_with_value33.append(key)
if Key_with_value33:
    print(f'Key_with_value33 = {Key_with_value33}')
else:
    print ("The key with that value does not exist") # output The key with that value does not exist


# because of the same reasoning the output will be as indicated.
Students={"John":33, "Janeth":35, "Halima":20, "Japhet":12, "Humphery":18, "Simon":33}
for key,value in Students.items():
    Key_with_value33=[]
    if value ==33:
        Key_with_value33.append(key)
if Key_with_value33:
    print(f'Key_with_value33 = {Key_with_value33}')
else:
    print ("The key with that value does not exist") # output Key_with_value33 = ['Simon']

# to keep of all the track that the program checks Key_with_value33=[] need to be defined before the loop
Students={"John":33, "Janeth":35, "Halima":20, "Japhet":12, "Humphery":18, "Simon":33}
Key_with_value33=[]
for key,value in Students.items():
    if value ==33:
        Key_with_value33.append(key)
if Key_with_value33:
    print(f'Key_with_value33 = {Key_with_value33}')
else:
    print ("The key with that value does not exist") # the output Key_with_value33 = ['John', 'Simon']


# To otain the value correspong to key in the dictionery this the code 
# dictionarty_name[key_of_the_value_to_determined], check this code 
students = {"Nora":15, "Gino":30}
print(students["Nora"]) # this code gives the value that corresponds to key "Nora" in student dictioney

print([value for key,value in students.items() if key=="Nora"]), # item() fuctio is used if we want
# to iterate in key,value item in the dictionery.

# to obtain the key that correapond to the value in  the dictionery
for key,value in students.item():
    mark_value=15
    if value==mark_value:
        print(f"the student with {mark_value} marks are [{keys}]")
else:
    print(f"Mark: {mark_value} is not in the class")

students = {"Nora":15, "Gino":30, "Rose":60, "Aisha":15}
# I  want the list of student with mark equals to 15
mark_value=15
print(f"The students with marks {mark_value} is {[key for key,value in students.items() if value==mark_value]}")

# We can also achieve this using for loop as follows 

mark_value=15
student_name=[]
for key,value in students.items():
    if value==mark_value:
     student_name.append(key)
if student_name:
    print(f"the student with {mark_value} marks are {student_name}")    
else:
    print(f"Mark: {mark_value} is not in the class")
