# Write a program in Python to calculate the percentage of 5 subjects inputted by the user.

maths = int(input("Enter the Number of Maths: "))
chemistry = int(input("Enter the Number of Chemistry: "))
physics = int(input("Enter the Number of Physics: "))
english = int(input("Enter the Number of English: "))
computer = int(input("Enter the Number of Computer: "))

percentage = (maths*chemistry*physics*english*computer)/5

print(percentage)