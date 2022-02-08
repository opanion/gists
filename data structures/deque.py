class Deque:
    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        if self.items: 
            return self.items.pop(0)

    def remove_rear(self):
        if self.items: 
            return self.items.pop()

    def peak_front(self):
        if self.items:
            return self.items[0]

    def peak_rear(self):
        if self.items:
            return self.items[-1]

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []


#my_deque = Deque()
#print(my_deque.items)
#my_deque.add_front('Apple')
#my_deque.add_front('Banana')
#my_deque.add_rear('Orange')
#my_deque.add_rear('Mango')
#print(my_deque.items)
#Banana Apple Orange Mango

#print(my_deque.remove_front())
#Banana
#print(my_deque.remove_rear())
#Mango
#print(my_deque.items)
#Apple Orange
#print(my_deque.peak_front())
#Apple
#print(my_deque.peak_rear())
#Orange
#print(my_deque.size())
#2
#print(my_deque.is_empty())
#False