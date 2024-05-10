a=[2,4,3,7,8,9]
b=[2,5,7,6,4]
def different(a,b):
    result=[]
    for x in a:
      if x not in b:
       result.append(x)
    print(result)
different(a,b)
print(__name__)
