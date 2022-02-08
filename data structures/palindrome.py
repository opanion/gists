import deque
import re

def is_palindrome(some_str):
    
    new_str = re.sub('\W+','', some_str)
    new_str = new_str.lower()

    my_deque = deque.Deque()
    for char in new_str:
        my_deque.add_rear(char)
    
    

    while my_deque.size() >= 2:
        front = my_deque.remove_front()
        rear = my_deque.remove_rear()

        if front != rear:
            return False
    
    return True


print(is_palindrome('Ka!y,ak'))
print(is_palindrome('level'))
print(is_palindrome('range'))
