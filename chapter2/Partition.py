from LinkedList import LinkedList

def partition(ll,x):
    current = ll.head
    ll.tail = ll.head

    while current:
        nextnode = current.next
        current.next = None

        if current.value < x:
            current.next = ll.head
            ll.head = current
        else:
            ll.tail.next = current
            ll.tail = current
        
        current = nextnode

    if ll.tail.next is not None:
        ll.tail.next = None

ll = LinkedList([3,5,8,5,10,2,1])
print(ll)
partition(ll, 5)
print(ll)