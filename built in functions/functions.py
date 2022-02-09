
def my_function(*, arg1, arg2, suppressExcp = None):
    '''my_function(arg1, arg2, suppressExcp=None) --> Doesn't really do anything, just prints.
    The function accepts only keyword arguments
    Parameters:
    arg1: first argument
    arg2: second argument, defaults to zero
    arg2: third argument, defaults to none
    '''

def main():
    #variable list arguments
    print(addition(10,20,20))
    my_nums = [10, 20, 30, 40]
    print(addition(*my_nums))

    #converting temps using functions
    ctemp = [0, 12, 34, 100]
    ftemp = [32, 65, 100, 212]

    print(list(map(celcius_to_fah, ctemp)))
    print(list(map(fah_to_celcius, ftemp)))

    #using lambdas
    print(list(map(lambda temp: (temp * 9/5) + 32 , ctemp)))
    print(list(map(lambda temp: (temp -32) * 5/9 , ftemp)))

    my_function(arg1 = 1, arg2= 2, suppressExcp = False)


def addition(*args):
    result = 0
    for arg in args:
        result +=arg
    return result

def celcius_to_fah(temp):
    return (temp * 9/5) + 32

def fah_to_celcius(temp):
    return (temp -32) * 5/9


if __name__ == '__main__': main()