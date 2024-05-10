# the method that takes the items of the list and write them to the file. 
# this items will be written in the separate lines of the string

# Thsi is teh code snippet
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("output.txt", "w") as file:
   file.writelines(lines)
