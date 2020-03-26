from LinkedList import LinkedList

def is_palindrome(ll) -> bool:
    slow = fast = ll.head
    stack = []

    while fast and fast.next:
        stack.append(slow.value)

        slow = slow.next
        fast = fast.next.next
    
    if fast:
        slow = slow.next
    
    while slow:
        top = stack.pop()

        if top != slow.value:
            return False
        
        slow = slow.next
    
    return True

ll_true1 = LinkedList([1, 2, 3, 4, 5, 4, 3, 2, 1])
print(is_palindrome(ll_true1))
ll_true2 = LinkedList([1, 2, 3, 3, 2, 1])
print(is_palindrome(ll_true2))
ll_false = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(is_palindrome(ll_false))
