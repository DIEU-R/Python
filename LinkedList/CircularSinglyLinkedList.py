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
    

    def insertCSLL(self,value,location):
        if self.head is None:
            return "The head reference is None"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location ==1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index <location-1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode             
            return "The node has been successfully inserted in the Circular Singly Linked List"

    def traverseCSLL(self):
        if self.head is None:
            print("The Circular Singly Linked List does not exist")
        else:
            node = self.head
            while node:
                print(node.value)
                node = node.next
                if node == self.tail.next:
                    break



    def searchCSLL(self, nodeValue):
        if self.head is None:
            return "The circular Singly Linked List does not exist"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return (list([node.value for node in circularSLL]).index(tempNode.value))
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    return "The node does not exist in the CSLL"
                

    def deleteNode(self, location):
        if self.head is None:
            return "The Circular Singly LinkedList does not exist"
        else:
            if location ==0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                    self.head.next = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location ==1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                    self.head.next = None
                else:
                    tempNode = self.head
                    while tempNode is not None:
                        if  tempNode.next == self.tail:
                            break
                        tempNode = tempNode.next
                    tempNode.next = self.head
                    self.tail = tempNode
            else:
                tempNode = self.head
                index = 0
                while index < location-1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
        return "The node has been successfully deleted"


    def deleteCSLL(self):
        if self.head is None:
            return "The Circular Singly Linked List does not exist"
        else:
            self.head = None
            self.tail.next = None
            self.tail = None


circularSLL = CircularSinglyLinkedList()
print(circularSLL.createCSLL(10))
circularSLL.insertCSLL(101,0)
circularSLL.insertCSLL(102,1)
circularSLL.insertCSLL(1003,2)

print([node.value for node in circularSLL])

circularSLL.traverseCSLL()
print(circularSLL.searchCSLL(102))

circularSLL.deleteNode(2)
print([node.value for node in circularSLL])

circularSLL.deleteCSLL()
print([node.value for node in circularSLL])