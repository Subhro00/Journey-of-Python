#docstrings are the string literals that appear right after the defination of a function,method,class or module

def square(n):
    '''Takes in a number n
    Returns the square of n'''
    print(n**2)


square(5)
print(square.__doc__)  

def square(n):
    print(n)               #the doc string should be just below the function else it gives none
    '''Takes in a number n
    Returns the square of n'''
    #the doc-string should always be below function and above the function body otherwise it returns none
    print(n**2)


square(5)
print(square.__doc__)   