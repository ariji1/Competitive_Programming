import random


def rand7():
    return random.randint(1, 7)


def rand5():
    """return a random integer from 1 to 5"""
    while True:
        r = rand7()
        if r < 6:
            return r


print 'Rolling 5-sided die...'
print rand5()