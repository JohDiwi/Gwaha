even_numbers={2,4,6,8,10}
odd_numbers={2,3,5,7,9}
print(even_numbers|odd_numbers)
print(even_numbers. union(odd_numbers))
print("Intersection using &:", even_numbers&odd_numbers)
print("intersectio using intersection()", even_numbers. intersection(odd_numbers))
print(even_numbers-odd_numbers)
print(even_numbers.difference(odd_numbers))
print("symementry difference of Numbers is:", even_numbers^odd_numbers)
print(odd_numbers.symmetric_difference(even_numbers))
if odd_numbers==even_numbers:
    print("The numbers ore the same")
else:
    print("The numbers are not the same")

Namba_shufwa=even_numbers.copy()
print(Namba_shufwa)
