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
        Returns a boolean on whether the stack is empty or not'''
        return self.items == []

my_stack = Stack()
print(my_stack.is_empty())
my_stack.push('Water')
my_stack.push('Air')
print(my_stack.pop())
print(my_stack.peek())
print(my_stack.size())
print(my_stack.is_empty())