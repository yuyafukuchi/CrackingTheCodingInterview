from LinkedList import LinkedList

def detectLoop(ll):
    slow = ll.head
    fast = ll.head

    while slow:
        slow = slow.next
        fast = fast.next.next

        if slow.value == fast.value:
            break
    
    pointer1 = ll.head
    pointer2 = slow

    while pointer1:
        if pointer1.value == pointer2.value:
            return pointer1
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    
    

ll = LinkedList([0,1,2,3,4,5,2,3,4,5,2,3,4,5])
print(detectLoop(ll))
    



