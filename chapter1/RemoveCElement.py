from LinkedList import LinkedList

def remove_CElement(ll):

    slow = ll.head
    fast = ll.head

    while fast.next.next:
        fast = fast.next.next
        slow = slow.next
    
    slow = slow.next
    return slow


if __name__ == "__main__":

    l = LinkedList(["a","b","c","d","e","f"])
    print(l)