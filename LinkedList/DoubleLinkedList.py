from tkinter import ANCHOR


class Node:
    def __init__(self, value=None):
        self.value= value
        self.next= None
        self.prev= None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def createDLL(self,nodeValue):
        node = Node(nodeValue)
        node.next = None
        node.prev = None
        self.head = node
        self.tail = node
        return "The DLL has been created"



doublyLL= DoublyLinkedList()
doublyLL.createDLL("10")
print([node.value for node in doublyLL])    