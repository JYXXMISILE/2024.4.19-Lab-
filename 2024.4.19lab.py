num1 = input('Please type in the first number:')
num2 = input('Please type in another number:')
if num1 > num2:
    print(f'The greater number was: ' + num1)
elif num2 > num1:
    print(f"The greater number was: " + num2)
else:
    print("The numbers are equal!")


year = int(input('Please type in a year: '))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print('That year is a leap year')
else:
    print('That year is not a leap year.')






