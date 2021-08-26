
# Python3 code to demonstrate
# generating random strings 
# using random.choices()
import string
import random

def code():  
    # initializing size of string 
    N = 200
    
    # using random.choices()
    # generating random strings 
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = N))
    return res


def code2():  
    # initializing size of string 
    N = 350
    
    # using random.choices()
    # generating random strings 
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = N))
    return res
