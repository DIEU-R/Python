from LinkedList import LinkedList, Node

def intersection(lla,llb):
    if lla.tail is not llb.tail:
        return False
    
    lenA=len(lla)
    lenB=len(llb)

    shorter = lla if lenA < lenB else llb
    longer = llb if lenA < lenB else lla

    diff = len(longer)- len(shorter)
    longerNode = longer.head
    shorterNode = shorter.head

    for i in range(diff):
        longerNode = longerNode.next

    while shorterNode is not longerNode:
        shorterNode = shorterNode.next
        longerNode = longerNode.next

    return longerNode

#helper function to generate a linked list
def addSampleNode(lla,llb,value):
    tempNode = Node(value)
    lla.tail.next = tempNode
    lla.tail = tempNode
    llb.tail.next = tempNode
    llb.tail = tempNode

lla = LinkedList()
lla.generate(3,0,9)
llb = LinkedList()
llb.generate(4,0,9)
addSampleNode(lla,llb,7)
addSampleNode(lla,llb,2)
print(lla)
print(llb)
print(intersection(lla,llb))
