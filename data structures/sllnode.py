class SLLNode:

    def __init__(self, data):
        self.data = data
        self.next = None

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
    

class SLL:
    def __init__(self):
        self.head = None

    def __repr__(self):
        return f'SLL object: head = {self.head}'

    def is_empty(self):
        return self.head is None

    def add_front(self, new_data):
        temp = SLLNode(new_data)
        temp.set_next(self.head)
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
        #List is empty
        if self.head is None:
            return 'Linked list is empty. No node to remove'
      
        current = self.head
        previous = None
        found = False

        while not found:
            if current.get_data() == data:
                found = True
            else:
                if current.get_next() == None:
                    return 'Node with that data value not found'
                else:
                    previous = current
                    current = current.get_next()
        #first item
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

