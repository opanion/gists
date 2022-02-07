class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        '''
        Accepts an item as a parameter and adds to the end of a list. 
        It returns nothing
        The runtime for this method is O(1) or constant time because appending
        to the end of the list happens in constant time
        '''
        self.items.append(item)
        

    def pop(self):
        '''
        Removes the item on top of the stack and returns it
        '''
        if self.items:
            return self.items.pop()
        return None

    def peek(self):
        '''
        Returns the item on top of the stack
        '''
        if self.items:
            return self.items[-1]

    def size(self):
        '''
        Returns the number of items in the stack
        '''
        return len(self.items)

    def is_empty(self):
        '''
        Returns a boolean on whether the stack is empty or not
        '''
        return self.items == []

def match_symbols(symbol_str):
    '''
    This method accepts a string containing brackets and checks whether 
    they are balanced or not
    '''
    match_symbols ={'{': '}',
                '[': ']',
                '(': ')'
                }
    index = 0
    openers = match_symbols.keys()
    my_stack = Stack()
    while index < len(symbol_str):
        symbol = symbol_str[index]
        if symbol in openers:
            my_stack.push(symbol)
        else:
            if my_stack.is_empty(): return False
            else:
                if symbol != match_symbols[my_stack.pop()]:
                    return False
        index +=1
        
    if my_stack.is_empty():
        return True


print(match_symbols('({[{([])}]})'))
print(match_symbols('){[{([])}]})'))
print(match_symbols('([)}]})'))