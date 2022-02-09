import itertools

def main():

    #cycle - infinite iterator
    seq1 = ['James', 'John', 'Abu']
    cycle1 = itertools.cycle(seq1)
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))

    #count - infinite iterator
    count = itertools.count(10,10)
    print(next(count))
    print(next(count))
    print(next(count))

    #accumulator
    values = [10, 20, 30, 40, 20, 30]
    accum = itertools.accumulate(values, max)
    print(list(accum))

    #chain
    x = itertools.chain('ABCD', '1234')
    print(list(x))

    #dropwhile and takewhile
    result = itertools.dropwhile(somefunc, values)
    result1 = itertools.takewhile(somefunc, values)
    print(list(result))
    print(list(result1))

def somefunc(x):
    return x < 40


if __name__ == '__main__': main()