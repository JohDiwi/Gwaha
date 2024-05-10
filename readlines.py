with open("open.py", "r") as file_to_read:
    lines=file_to_read.readlines()
# since readlines() read each line and return a list with each line as an item of the list
print(lines)
# will give an output ['New_Name="John_Peter"\n', 'New_Age=34\n', 'New_Country="Tanzania"\n']
# using a for loop, 
for line in lines:
    print(line.strip())