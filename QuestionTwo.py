# file contains a function that executes question two

def funcTwo():
    print('\nQuestion Two')
    # user inputs a string
    userStr = input('Enter word: ')
    # 'y' and 'o' are removed from the string
    userStr = userStr.replace('y', '')
    userStr = userStr.replace('o', '')
    # string is printed regularly and in reverse
    print(userStr)
    print(userStr[::-1], '\n')

    # user is asked to enter two numbers
    userInt1 = float(input('Enter number: '))
    userInt2 = float(input('Enter number: '))
    # equation is output with expected answer
    print(userInt1, ' + ', userInt2, ' = ', userInt2 + userInt1)
