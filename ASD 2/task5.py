class Queue:
    def __init__(self):
        self.stack = []

    def enqueue(self, item):
        self.stack.append(item)

    def dequeue(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop(0)

    def size(self):
        return len(self.stack)