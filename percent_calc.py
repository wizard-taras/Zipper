"""
    Script name: percent_calc.py

    Purpose: i. Calculates the percentage of some provided value with
respect to total value
            ii. Test error handling capabilities

    Programmer      Date        Code changes
    Koziupa T.      30/11/22    Original code
"""
while True:
    try:
        value_tot_user = int(input('Enter total value: '))
        value_user = int(input('Enter value: '))

        try:
            result = value_user/value_tot_user * 100
            print(f'That is {result}%')

        except ZeroDivisionError:
            print('You cannot divide by zero')
            continue
    except ValueError:
        print('You should enter a number. The program will run again')
        continue