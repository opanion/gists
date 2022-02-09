import collections

def main():
    # create point named tuple
    point = collections.namedtuple('Point', 'x y')
    p1 = point(5, 10)
    p2 = point(20, 50)
    print(p1)
    print(p2)
    print(p1.x, p2.y)

    #_replace creates a new instance
    y = p1._replace(x=100)
    print(y)
if __name__ == '__main__': main()