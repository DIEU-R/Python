class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next


class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return '\n'.join(values)

    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False
        

    def push(self, value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node
        return "The element has been successfully inserted"
    
    def pop(self):
        if self.isEmpty():
            return "There is no element to pop"
        else:
            nodeValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return nodeValue
        
    def peek(self):
        if self.isEmpty():
            return "There is no element to peek"
        else:
            nodeValue = self.LinkedList.head.value
            return nodeValue
        
    def delete(self):
        self.LinkedList.head = None




customStack = Stack()
customStack.push(3)
customStack.push(2)
customStack.push(1)
print(customStack)
print("_________________________")
customStack.pop()
print(customStack)
print(customStack.peek())
print(customStack.delete())