my_list=[]
print(my_list)
elements1=10,20,30,40
my_list.extend(elements1)
print(my_list)
my_list[1]=15
print(my_list)
element2=[50,60,70]
my_list.extend(element2)
print(my_list)
del my_list[-1]
print(my_list)
my_list.sort()
print(my_list)
index_of_value_30=my_list.index(30)
print(index_of_value_30)