# A simple calculator app
print("Welocme to my simple calculator")
print('''-------------------
1. Addition
2. Subtraction
3. Multiplication
4. Division
-------------------        
''')
print("Enter two numbers to add")
#Asks a user for number
first_number = float(input("First Number: "))
#Input for first number
second_number = float(input("Second Number: "))
#Input for second number
sum = float(first_number) + float(second_number)
print(f"{first_number} + {second_number} = {sum:.2f}")
#Addition function above


print("Enter two numbers to subtract")
#Asks a user for number
first_number = float(input("First Number: "))
#Input for first number
second_number = float(input("Second Number: "))
#Input for second number
subtract = float(first_number) - float(second_number)
print(f"{first_number} - {second_number} = {subtract:.2f}")
#Subtraction function above


print("Enter two numbers to multiply")
#Asks a user for number
first_number = float(input("First Number: "))
#Input for first number
second_number = float(input("Second Number: "))
#Input for second number
multiply = float(first_number) * float(second_number)
print(f"{first_number} * {second_number} = {multiply:.2f}")
#Multiplication function above


print("Enter two numbers to divide")
#Asks a user for number
first_number = float(input("First Number: "))
#Input for first number
second_number = float(input("Second Number: "))
#Input for second number
divide = float(first_number) / float(second_number)
print(f"{first_number} / {second_number} = {divide:.2f}")
#Division function abov


print("Enter two numbers to perform exponential operation")
#Asks a user for number
first_number = float(input("Number base: "))
#Input for first number
second_number = float(input("Exponential power: "))
#Input for second number
exponent = float(first_number) ** float(second_number)
print(f"{first_number} ^ {second_number} = {exponent:.2f}")
#Exponential function above
