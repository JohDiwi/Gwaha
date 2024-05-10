list1 = [3 , 2 , 5 , 6 , 0 , 7, 9]
sum1 = 0
sumw2 = 0
for elem in list1:
 if (elem % 2 == 0):
  sum1 = sum1 + elem
  continue
 if (elem % 3 == 0):
  sum2 = sum1 + elem
print(sum2 , end=" ")