class Queue(object):

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop() 

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

