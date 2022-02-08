from calendar import c


class DLLNode:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        return f'SLL node object: data = {self.data}'

    def get_data(self):
        '''
        Return self.data attr
        '''
        return self.data

    def set_data(self, new_data):
        '''
        Replace value of self.data with new_data'''
        self.data = new_data

    def get_next(self):
        '''
        Return the self.next attr'''
        return self.next

    def set_next(self, new_next):
        '''
        Replace value of self.next with new next'''
        self.next = new_next

    def get_prev(self):
        '''
        Return the self.prev attr'''
        return self.prev

    def set_prev(self, new_prev):
        '''
        Replace value of self.prev with new next'''
        self.prev = new_prev


class DLL:
    def __init__(self):
        self.head = None

    def __repr__(self):
        return f'DLL object: head = {self.head}'

    def is_empty(self):
        return self.head is None

    def add_front(self, new_data):
        temp = DLLNode(new_data)
        temp.set_next(self.head)
        if self.head is not None: 
            self.head.set_prev(temp)
        self.head = temp

    def size(self):
        size = 0
        if self.head is None:
            return size
        current = self.head
        while current is not None:
            size += 1
            current = current.get_next()
        return size

    def search(self, data):
        if self.head is None:
            return 'Linked list is empty. No node to search'
        current = self.head
        while current is not None:
            #nodes data matches what we are looking for
            if(current.get_data() == data):
                return True
            #node data doesn't match
            else: 
                current = current.get_next()
        
        return False

    def remove(self, data):
        if self.head is None:
            return 'Linked list is empty. No node to remove'
        
        current = self.head
        found = False

        while not found:
            if current.get_data() == data:
                found = True
            else:
                if current.get_next() == None:
                    return 'Node with that data value not found'
                else:
                    current = current.get_next()

        if current.prev is None:
            self.head = current.get_next()
        else:
            current.prev.set_next(current.get_next())
            current.next.set_prev(current.get_prev())


dll = DLL()
dll.remove(5)
dll.add_front(50)
dll.add_front(90)
print(dll.size())
print(dll.head)
print(dll.remove(80))