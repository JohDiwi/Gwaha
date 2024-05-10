with open("open.py", "r") as file_to_read:
    lines=file_to_read.readlines()
    New_Name="Brian_Omundi"
    New_Age=37
    New_Country="kenya"
    for i,line in enumerate(lines):
        if line.startswith("Name"):
            lines[i]=f'Name = {New_Name}\n'
        elif line.startswith("Age"):
            lines[i]=f"Age = {New_Age}\n"
        else:
            lines[i]=f"Country = {New_Country}\n"
with open("open.py", "w") as file_to_write:
 file_to_write.writelines(lines)



# This task can also be done using this method
import os

# Define the new values
New_Name = "Brian_Omundi"
New_Age = 37
New_Country = "Kenya"
# Open the original file for reading and a temporary file for writing
with open("open.py", "r") as file_to_read, open("temp.py", "w") as temp_file:
    # Iterate through each line in the original file
    for line in file_to_read:
        # Check if the line starts with "Name"
        if line.startswith("Name"):
            # Replace the line with the updated name
            temp_file.write(f'Name = {New_Name}\n')
        # Check if the line starts with "Age"
        elif line.startswith("Age"):
            # Replace the line with the updated age
            temp_file.write(f"Age = {New_Age}\n")
        else:
            # Replace the line with the updated country
            temp_file.write(f"Country = {New_Country}\n")

# Replace the original file with the temporary file
os.replace("temp.py", "open.py")

import os
New_name="Brian_Onyango"
New_Age=37
New_country="kenya"


# open file with file to be replaced in read mode and template file to write in write  mode
with open("open.py", "r") as file_to_read, open("temp.py", "w") as file_to_write:
# opening file in read mode treats the lines are items to iterate over

    for line in file_to_read:
# Note: we work with file objects created after opening a file. file_to_read and file_to_write here
        if line.startswith("Name"):
            file_to_write.write(f"Name = {New_Name}\n")
        if line.startswith("Age"):
            file_to_write.write(f"Age = {New_Age}\n")
        else:
            file_to_write.write(f"New_conuntry={New_country}\n" )
# replace the content of the file
os.replace("open.py", "temp.py")
        
                                
