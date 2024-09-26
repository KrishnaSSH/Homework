# Write a program in Python to swap the values of two variables without using a third variable

a = int(input("Enter the Value of a: "))
b = int(input("Enter the value of b: "))

a = a+b
b = a-b 
a = a-b


print("The value of A is ", a)
print("The value of B is ", b )