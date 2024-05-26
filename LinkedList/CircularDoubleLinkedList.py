class Node:
    def __init__(self, value=None):
        self.value= value
        self.next = None
        self.prev = None

class CircularDoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break



    def createCDLL(self, nodeValue):
        newNode = Node(nodeValue)
        self.head = newNode
        self.tail = newNode
        newNode.next = newNode
        return "The Circular Double Linked List has been created"
    



circularDLL = CircularDoubleLinkedList()
print(circularDLL.createCDLL(11))
print([node.value for node in circularDLL])