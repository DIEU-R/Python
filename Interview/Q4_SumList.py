from LinkedList import LinkedList


def sumlist(lla,llb):
    n1 = lla.head
    n2 = llb.head
    carry = 0
    ll = LinkedList()

    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2: 
            result += n2.value
            n2 = n2.next
        ll.add(result % 10)
        carry = result // 10

    if carry:
        ll.add(carry)
    return ll

lla = LinkedList()
lla.generate(3,0,9)
llb = LinkedList()
llb.generate(3,0,9)
print(lla)
print(llb)
print(sumlist(lla,llb))