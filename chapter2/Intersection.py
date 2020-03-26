from LinkedList import LinkedList

def is_intersection(ll1,ll2):
    if ll1.tail is not ll2.tail:
        return False
    
    if len(ll1) < len(ll2):
        shorter = ll1
        longer = ll2
    else:
        shorter = ll2
        longer = ll1
    
    dif = len(longer) - len(shorter)

    shorter_node = shorter.head
    longer_node = longer.head

    # dif の分だけ長い方を詰める
    for _ in range(dif):
        longer_node = longer_node.next

    while shorter_node:
        if shorter_node == longer_node:
            return shorter_node
        
        shorter_node = shorter_node.next
        longer_node = longer_node.next
    
    return False

ll1 = LinkedList([1,2,3,4,5,6,7,8])
ll2 = LinkedList([1,4,5,6,7,8])

print(is_intersection(ll1,ll2))