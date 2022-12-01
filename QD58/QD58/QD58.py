
class Error(Exception):
    '''base class for other Errors'''
    pass

class NoIntError(Error):
    '''raised when there is no int in the string
    
    Attributes:
        message -- explanation of the error
    '''
    def __init__(self):
        self.message = "There is no integer in the string"
        self.amount = '100'
        super().__init__(self.message)

    def __str__(self):
        return f'{self.amount} -> {self.message}'


class NoUpperError(Error):
    '''raised when there is no letter of uppercase in the string
    
    Attributes:
        message -- explanation of the error
    '''
    def __init__(self):
        self.message = "There is no uppercase letter in the string"
        super().__init__(self.message)
    pass

class NoLowerError(Error):
    '''raised when there is no letter of lowercase in the string
    
    Attributes:
        message -- explanation of the error
    '''
    def __init__(self):
        self.message = "There is no lowercase letter in the string"
        super().__init__(self.message)


def main():
    inp = input()
    noInt = True
    noUpper = True
    noLower = True
    
    for char in inp:
        if char.isdigit():
            noInt = False
        elif char.isupper():
            noUpper = False
        elif char.islower():
            noLower=False
        else:
            pass

    if noInt: raise NoIntError
    if noUpper: raise NoUpperError
    if noLower: raise NoLowerError

main()
