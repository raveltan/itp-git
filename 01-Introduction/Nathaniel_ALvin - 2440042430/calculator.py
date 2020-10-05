while True:
    first_Number = int(input('first number: '))
    second_Number = int(input('second number: '))
    operator = input('operation: ')

    if operator == '+':
        print(first_Number + second_Number)
    elif operator == '-':
        print(first_Number - second_Number)
    elif operator == '*':
        print(first_Number * second_Number)
    elif operator == '/':
        print(first_Number / second_Number)
    else:
        print('Sorry that action is not yet supported.')

