import json

with open('calculator_messages.json', 'r') as file:
    messages = json.load(file)

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False

while True:
    prompt(messages['de']['greeting'])

    prompt("What's the first number?")
    number1 = input()

    while invalid_number(number1):
        prompt(messages['de']['invalid_num'])
        number1 = input()

    prompt("What's the second number?")
    number2 = input()

    while invalid_number(number2):
        prompt(messages['de']['invalid_num'])
        number2 = input()

    prompt(
    'What operation would you like to perform?\n'
    '1) Add 2) Subtract 3) Multiply 4) Divide')
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt('You must choose 1, 2, 3, or 4')
        operation = input()

    match operation:
        case '1':
            prompt(f'The result is: {float(number1)+ float(number2)}')
        case '2':
            prompt(f'The result is: {float(number1) - float(number2)}')
        case '3':
            prompt(f'The result is: {float(number1)* float(number2)}')
        case '4':
            prompt(f'The result is: {float(number1) / float(number2)}')

    prompt('Would you like to perform another calculation? (y/n) ')
    response = input()

    if response and response[0].lower() != 'y':
        break
