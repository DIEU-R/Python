from LinkedList import LinkedList


def removeDups(LL):
    if LL.head is None:
        return "The LinkedList does not exist"
    else:
        curNode = LL.head
        visited = set([curNode.value])
        while curNode.next:
            if curNode.next.value in visited:
                curNode.next = curNode.next.next
            else:
                visited.add(curNode.next.value)
                curNode = curNode.next
        return LL
    
def removeDups1(LL):
    if LL.head is None:
        return 
    else:
        curNode = LL.head
        while curNode:
            runner = curNode
            while runner.next:
                if runner.next.value == curNode.value:
                    runner.next = runner.next.next
                else:
                    runner =runner.next
            curNode = curNode.next
        return LL
    

customLL = LinkedList()
customLL.generate(10,0,99)
print(customLL)
removeDups(customLL)
print(customLL)
removeDups1(customLL)
print(customLL)