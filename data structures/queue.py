class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        '''
        Accepts an item and inserts the item into the 0th index in a list.
        Runtime is O(N) because inserting at the 0th index causes 
        the other items to be pushed 1 index to the right
        '''
        self.items.insert(0, item)

    def deque(self):
        '''
        '''
        if self.items:
            return self.items.pop()
        return None

    def peek(self):
        '''
        '''
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        '''
        '''
        return len(self.items)

    def is_empty(self):
        '''
        '''
        return self.items == []


