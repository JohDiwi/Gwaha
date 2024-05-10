# another_file.py
with open('open.py', 'r') as file:
    contents = file.read()
    # Extract the value of variable A
    A = contents.split('=')[1].strip().strip('"')
    print(A)
# another_file.py
with open('open.py', 'r') as file:
    contents = file.read()
    # Extract the variable name
    variable_name = contents.split('=')[0].strip()
    print(variable_name)
