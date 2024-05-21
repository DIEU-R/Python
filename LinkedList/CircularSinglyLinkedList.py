class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None


class CircularSinglyLinkedList:
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

    def createCSLL(self, nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node
        return "The Circular Singly Linked List has been created"
    
circularSLL = CircularSinglyLinkedList()
circularSLL.createCSLL(20)


print([node.value for node in circularSLL])