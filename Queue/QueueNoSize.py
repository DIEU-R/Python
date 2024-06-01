class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x)for x in self.items]
        return '\n'.join(values)
    

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False
        
    def enqueue(self,value):
        self.items.append(value)
        return "The element has been successfully inserted"
    
    def dequeue(self):
        if self.isEmpty():
            return "There is no element to dequeue"
        else:
            return self.items.pop(0)
        
    def peek(self):
        if self.isEmpty():
            return "There is no element to peek"
        else:
            return self.items[0]
        
    def delete(self):
        self.items = None
        return "The queue has been successfully deleted"


customQueue = Queue()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue)
print(customQueue.delete())