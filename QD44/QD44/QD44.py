

def factorial(x):
    if x == 1:
        return 1
    else:
        return x*factorial(x-1)

def fibonacci(x):
    if x == 1 or x == 2:
        return 1
    elif x == 0:
        return 0
    else:
        return fibonacci(x-1) + fibonacci(x-2)

def palindrome_checker(s):
    return s == s[::-1]

