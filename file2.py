# write only. 'w', it is used to write to the file.
# if the file already exist, its content will be truncated and the new file with the same
# name and same content will be created. if the file does not exist, the new file with specified name 
# will be created 

# open file for writting
file=open("addsing.py", "w")
#writhe to that file
file.write("I am deleting you")
# close the file
file.close()