# the remove file i.e. remove() takes the path to the file as an argument ad delete it
# this is done by importing the file tahat operate with your operating sysytem import os
# say i want to delete file named numpy.py
import os
if os.path.exists("D:\\Python module\\numpy.py"):
    os.remove("numpy.py")
    print(f"numpy.py has been deleted")
else:
    print(f"numpy.py does not exist")