for x in range (1, 11):
    print(x, end ='')
odds = []
for i in range (9, 50):
    if i % 2 != 0:
        odds.append(str(i))

evens = []
for i in range(100, 50, -1):
    if i % 2 == 0:
        evens.append(str(i))

#Print results with newline between them
print(','. join(odds) + '\n')
print(','. join(evens) + '\n')

while True:
    answer = input("Are you sure you want to delete the record? (y/n): ").strip().lower()
    if answer == "y":
        print("You have deleted the record permanently")
        break
    elif answer == "n":
        print("Cancel")
        break
    else:
        print("Please only enter 'y' or 'n'.")
print("This is a calculator")

# Input values from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter the operator (+, -, *, /, %, **, //): ")


if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Cannot divide by zero")
elif operation == "%":
    result = num1 % num2
    print(f"{num1} % {num2} = {result}")
elif operation == "**":
    result = num1 ** num2
    print(f"{num1} ** {num2} = {result}")
elif operation == "//":
    if num2 != 0:
        result = num1 // num2
        print(f"{num1} // {num2} = {result}")
    else:
        print("Error: Cannot divide by zero")
else:
    print("Error: Please enter a valid operation")






