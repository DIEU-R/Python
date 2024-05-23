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
            return "The DLL does not exist"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                newNode.prev = None
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