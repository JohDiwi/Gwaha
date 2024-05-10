# Enumearate() is the function that is used to iterate in a list while maintaining its value,index. 
my_list = ['apple', 'banana', 'orange'] 
for index, value in enumerate(my_list):
    print(index,value)
# This code doesnt work b'se it is not interpreted well, you can put brackets
# (value, index). This way you create a set with tupple (value, index) as its elements.
print({value,index for value, index in enumerate(my_list)})
# This code work
print({(value,index) for value, index in enumerate(my_list)}) 
# This is the output
{(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')}

# However if you want to create dictionary, this line of code work. 
print({value:index for value, index in enumerate(my_list)}) 