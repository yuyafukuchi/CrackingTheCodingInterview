from LinkedList import LinkedList

def sum_list(ll1,ll2):
    cur1 = ll1.head
    cur2 = ll2.head

    new_ll = LinkedList()
    kuriage = 0

    while cur1 and cur2:
        SUM = cur1.value + cur2.value

        if SUM+kuriage < 10:
            new_ll.add(SUM+kuriage)
            kuriage = 0
        else:
            new_ll.add(SUM+kuriage-10)
            kuriage = 1
        
        cur1 = cur1.next
        cur2 = cur2.next
    
    while cur1:
        if cur1.value+kuriage < 10:
            new_ll.add(cur1.value+kuriage)
            kuriage = 0
        else:
            new_ll.add(cur1.value+kuriage-10)
            kuriage = 1
        cur1 = cur1.next
    
    while cur2:
        if cur2.value+kuriage < 10:
            new_ll.add(cur2.value+kuriage)
            kuriage = 0
        else:
            new_ll.add(cur2.value+kuriage-10)
            kuriage = 1
        cur2 = cur2.next

    if kuriage:
        new_ll.add(kuriage)

    return new_ll

def sum_list_followup(ll1,ll2):
    if len(ll1) < len(ll2):
        for _ in range(len(ll2)-len(ll1)):
            ll1.add_to_beginning(0)
    elif len(ll1) > len(ll2):
        for _ in range(len(ll1)-len(ll2)):
            ll2.add_to_beginning(0) 

    tmp_result = 0
    n1 = ll1.head
    n2 = ll2.head

    while n1 and n2:
        tmp_result = tmp_result*10 + n1.value + n2.value
        n1 = n1.next
        n2 = n2.next
    
    res = LinkedList()
    res.add_multiple([int(s) for s in str(tmp_result)])
    return res
      
ll1 = LinkedList([7,1,6])
ll2 = LinkedList([5,9,3])
print(sum_list(ll1,ll2))
print(sum_list_followup(ll1,ll2))
