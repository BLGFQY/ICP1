# file contains a function that executes question three

def funcThree():
    print('\nQuestion Three')
    # user prompted to enter a sentence that includes the word python
    userStr = input('Enter a sentence with the word python: ')
    # sentence is reprinted and printed with all copies of 'python' replaced with 'pythons'
    print(userStr)
    print(userStr.replace('python', 'pythons'))