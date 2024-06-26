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
    
    def insertCDLL(self, value, location):
        if self.head is None:
            return " The CDLL does not exist"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode
            elif location == 1:
                newNode.next = self.head
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while location <index:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode
            return "The node has been successfully inserted in the Circular Double Linked List"

    def traverseCDLL(self):
        if self.head is None:
            return "The CDLL does not exist"
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                if tempNode == self.tail:
                    break
                tempNode = tempNode.next

    def reverseTraverseCDLL(self):
        if self.head is None:
            return "The CDLL does not Exist"
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                if tempNode == self.head:
                    break
                tempNode = tempNode.prev

    def searchCDLL(self, nodeValue):
        if self.head is None:
            return "The CDLL does not exist"
        else:
            tempNode = self.head
            idx=0
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value, idx
                if tempNode == self.tail:
                    return "The node does not exist in the CDLL"
                tempNode = tempNode.next
                idx += 1

    def deleteCDLL(self, location):
        if self.head is None:
            return "The CDLL does not Exist"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == 1:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                tempNode =self.head
                index = 0
                while index < location-1:
                    tempnode = tempNode.next
                    index += 1
                tempNode.next = tempNode.next.next
                tempNode.next.prev = tempNode
            print( "The node has been successfully deleted from the CDLL")

    def deleteEntireCDLL(self):
        if self.head is None:
            return "The CLL does not exist"
        else:
            self.tail.next = None
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None
            print( "The CDLL has been successfully deleted")


circularDLL = CircularDoubleLinkedList()
circularDLL.createCDLL(11)
print([node.value for node in circularDLL])

circularDLL.insertCDLL(5,0)
circularDLL.insertCDLL(1,1)
circularDLL.insertCDLL(2,1)
circularDLL.insertCDLL(3,1)
circularDLL.insertCDLL(30,1)
print([node.value for node in circularDLL])

circularDLL.traverseCDLL()   

circularDLL.reverseTraverseCDLL()

print(circularDLL.searchCDLL(30))

circularDLL.deleteCDLL(2)
print([node.value for node in circularDLL])

circularDLL.deleteEntireCDLL()
print([node.value for node in circularDLL])