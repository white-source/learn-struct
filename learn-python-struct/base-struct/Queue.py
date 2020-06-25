class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        self.items.pop()

    def size(self):
        return len(self.items)

q = Queue()
q.enqueue(4)
q.enqueue('dog')
q.enqueue(True)
print(q.size())
q.dequeue()
print(q.size())

