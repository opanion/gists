from collections import deque
import string
from typing import Deque

def main():
    #initialize deque with lowercase letters
    d = Deque(string.ascii_lowercase)

    #deques support the len() function
    print('Item count:', len(d))

    #deques can be iterated over
    for item in d:
        print(item.upper(), end='')

    #manipulate items from either end
    d.pop()
    d.popleft()
    d.append(2)
    d.appendleft(1)
    print(d)

    #rotate the deque
    print(d)
    d.rotate(1)
    print(d)

if __name__ == '__main__': main()