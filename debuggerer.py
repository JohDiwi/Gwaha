# pdb is the built-in interactive debugger that pause  the execution, inspect the variables and
# step in line-line to inspect the issues in the code
# To do debugging we use pdb and pdb.set_trace, the program pause and wait you to continuw with manipulation
# pdp commands that are used to inspect the code are 
# n (next): Execute the next line of code.
# s (step): Step into the next function call.
# c (continue): Continue execution until the next breakpoint is encountered.
# l (list): Show the current line of code and surrounding lines.
# p (print): Print the value of a variable.
# q (quit): Quit the debugger and exit the program.

import pdb
def divide(x,y):
    try:
        result=x/y
    except (ZeroDivisionError, ValueError):
        pdb.set_trace() # the breakpoint is set here, to wait for the 
        print(f"Error: ZeroDivisionError")
    else:
        return result # this block of code is executed and the result will be 5
print(divide(10,0))  # this function call will not run because ZeroDivisionError will be raised and              
                     # the execution will pause 
# At this point, you'll be dropped into the Python debugger (pdb) prompt where you can inspect 
# the program's state and diagnose the issue: 
# runnig the code, this is the output. 
#PS D:\Python module> & C:/Users/User/AppData/Local/Programs/Python/Python312/python.exe "d:/Python module/ff.py"
#> d:\python module\ff.py(7)divide()
#-> print(f"Error: ZeroDivisionError")


import pdb; pdb.set_trace() # Used when you want to start debugging right from the start of the code 
breakpoint() # is similar to writting this piece of code# import pdb; pdb.set_trace()