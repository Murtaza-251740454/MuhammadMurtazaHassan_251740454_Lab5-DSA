class Queue():
    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)
    
    def is_empty(self):
        return self.data == 0
    
    def first(self):
        if self.is_empty():
            raise("Queue IS EMPTY!!!")
        return self.data[0]
    
    def dequeue(self):
        return self.data.pop(0)
    
    def enqueue(self,items):
        return self.data.append(items)
    
array = Queue()
array.enqueue(3)
array.enqueue(2)
array.enqueue(1)
print("Top element:",array.first())
print("Pop element:",array.dequeue())
print("Pop element:",array.dequeue())
print("Size of Array:",array.size())
print("Is stack empty?",array.is_empty())
print("Top element:",array.first())