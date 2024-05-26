class Node:
    def __init__(self, value):
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

    def insertNode(self, value,location):
        if self.head is None:
            print("The DLL does not exist")
        else:
            newNode = Node(value)
            if location == 0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif location == 1:
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index <location -1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode
            return "The node has been successfully inserted"

    def traverseDLL(self):
        if self.head is None:
            return "The DLL does not exist"
        else:
            #tempNode = self.head
            while self.head:
                print(self.head.value)
                self.head = self.head.next

    def reversetraverseDLL(self):
        if self.head is None:
            return "The DLL does not exist"
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.prev


    def searchDLL(self, nodeValue):
        if self.head is None:
            return "The DLL does not exist"
        else:
            tempNode = self.head
            idx = 0
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value, idx
                tempNode = tempNode.next
                idx += 1
            return "The value does not exist in the DLL"

    def deleteNode(self,location):
        if self.head is None:
            print("The DLL does not exist")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                curNode = self.head
                index = 0
                while index <location -1:
                    curNode = curNode.next
                    index += 1
                curnode.next = curNode.next.next
                curNode.next.prev = curNode
            print( "The node has been successfully deleted" )           




doublyLL= DoublyLinkedList()
doublyLL.createDLL(10)
print([node.value for node in doublyLL])

doublyLL.insertNode(20,0)
doublyLL.insertNode(30,1)
doublyLL.insertNode(40,2)
doublyLL.insertNode(50,3)
doublyLL.insertNode(60,4)
doublyLL.insertNode(70,5)
print([node.value for node in doublyLL])
print(doublyLL.searchDLL(10))
doublyLL.reversetraverseDLL()
print(doublyLL.searchDLL(50))
doublyLL.traverseDLL()

doublyLL.deleteNode(0)
print([node.value for node in doublyLL])