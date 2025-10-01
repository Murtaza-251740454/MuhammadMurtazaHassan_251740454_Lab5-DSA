class Stack():
    def __init__(self):
        self.data = []
    
    def size(self):
        return len(self.data)
    
    def is_empty(self):
        return self.data == 0

    def push(self,item):
        self.data.append(item)

    def peek(self):
        if self.is_empty():
            raise("STACK IS EMPTY!!!")
        return self.data[-1]
    
    def pop(self):
        if self.is_empty():
            raise("STACK IS EMPTY!!!")
        return self.data.pop()
    
array = Stack()
array.push(6)
array.push(8)
array.push(7)

print("Top element:",array.peek())
print("Pop element:",array.pop())
print("Pop element:",array.pop())
print("Size of Array:",array.size())
print("Is stack empty?",array.is_empty())
print("Top element:",array.peek())

