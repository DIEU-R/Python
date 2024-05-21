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
                



circularSLL = CircularSinglyLinkedList()
print(circularSLL.createCSLL(10))
circularSLL.insertCSLL(101,0)
circularSLL.insertCSLL(102,1)
circularSLL.insertCSLL(1003,2)

print([node.value for node in circularSLL])

circularSLL.traverseCSLL()
print(circularSLL.searchCSLL(102))