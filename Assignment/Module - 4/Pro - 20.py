# Write python program that user to enter only odd numbers, else will raise an exception.
number=int(input('Enter Number : '))
try:
    if number %2 == 0:
        raise EnvironmentError(number)
    print('Number is Odd =', number)
except ValueError:
    print('Pleace Enter odd Number')