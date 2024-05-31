class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)
    
    # isEmpty
    def isEmpty(self):
        if self.list ==[]:
            return True
        else:
            return False

    def push(self, values):
        self.list.append(values)
        return "The elements has been successfully inserted"

    # pop
    def pop(self):
        if self.list == []:
            return "There is no element to pop"
        else:
            return self.list.pop()
        

    # peek
    def peek(self):
        if self.list == []:
            return "There is no element to peek"
        else:
            return self.list[len(self.list)-1]
        
    # delete
    def delete(self):
        self.list = None


customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
#print(customStack)
print(customStack.peek())
print(customStack)

print(customStack.pop())
print(customStack.pop())
print(customStack)
print(customStack.isEmpty()) 
print(customStack.delete())