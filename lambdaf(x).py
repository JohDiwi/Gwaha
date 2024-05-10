# lambda function/expressions
Product=lambda x,y=10:x*y
Greetings=lambda: "Hello " + "World"

print(Greetings() +" You are welcomed.")
print(Product(12))
print(Product(4))