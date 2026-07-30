# Ask the user for the first number.
# Ask the user for the second number.
# Ask the user for an operation to perform.
# Perform the operation on the two numbers.
# Print the result to the terminal.

print('Welcome to Calculator!')

print("What's the first number?")
number1 = int(input())

print("What's the second number?")
number2 = int(input())

print('What operation would you like to perform?\n1) Add 2) Subtract 3) Multiply 4) Divide')
operation = input()

if operation == '1':
    print(f'The result is: {number1 + number2}')
elif operation == '2':
    print(f'The result is: {number1 - number2}')
elif operation == '3':
    print(f'The result is: {number1 * number2}')
elif operation == '4':
    print(f'The result is: {number1 / number2}')
else:
    print('Please enter a number from 1 to 4')

