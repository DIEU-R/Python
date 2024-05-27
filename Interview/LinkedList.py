from random import randint

class Node:
    def __init__(self, value =None):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)
    
class LinkedList:
    def __init__(self,values = None):
        self.head = None
        self.tail = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

    def __str__(self):
        values = [str(x.value) for x in self]
        return '->'.join(values)
    
    def __len__(self):
        curNode = self.head
        total =0
        while curNode:
            total += 1
            curNode = curNode.next
        return total
    

    def add(self,value):
        if self.head is None:
            newNode = Node(value)
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail
    

    def generate(self, n, min_values, max_values):
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(min_values,max_values))
        return self
    



customLL = LinkedList()
customLL.generate(10,0,99)
print(customLL)