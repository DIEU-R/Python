class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)
    
    # isEmpty
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
        
    # isFull
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False
        

    # push
    def push(self, values):
        if self.isFull():
            return "The stack is Full"
        else:
            self.list.append(values)
            return "The elements has benn successfully Inserted"
        

    # pop
    def pop(self):
        if self.isEmpty():
            return "There is no element to pop"
        else:
            return self.list.pop()
        

    # peek
    def peek(self):
        if self.isEmpty():
            return "There is no element to peek"
        else:
            return self.list[len(self.list)-1]
        
    # delete
    def delete(self):
        self.list = None


customStack = Stack(4)
print(customStack.isEmpty())
print(customStack.isFull())
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)
customStack.pop()
print(customStack.peek())
print(customStack.delete())