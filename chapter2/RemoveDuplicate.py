from LinkedList import LinkedList

def remove_dups(ll):
    if ll.head is None:
        return ll
    
    cur = ll.head
    seen = set([cur.value])

    while cur.next:
        if cur.next.value in seen:
            cur.next = cur.next.next
        else:
            seen.add(cur.next.value)
            cur = cur.next
    return ll

# setを使わずにやるには？
# 時間計算量O(N^2)にすればいける
def remove_dups_followup(ll):
    if ll.head is None:
        return ll

    current = ll.head

    while current:
        runner = current

        while runner.next:
            if runner.next.value == current.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        
        current = current.next
    
    return ll


data1 = [1,1,2,2,3,3,4,4,5,5]
ll = LinkedList(data1)
remove_dups(ll)
print(ll)

data1 = [1,2,3,4,5,6,7,8,9]
ll = LinkedList(data1)
remove_dups(ll)
print(ll)

data1 = [1]
ll = LinkedList(data1)
remove_dups(ll)
print(ll)



# follow-up

data1 = [1,1,2,2,3,3,4,4,5,5]
ll = LinkedList(data1)
remove_dups_followup(ll)
print(ll)

data1 = [1,2,3,4,5,6,7,8,9]
ll = LinkedList(data1)
remove_dups_followup(ll)
print(ll)

data1 = [1]
ll = LinkedList(data1)
remove_dups_followup(ll)
print(ll)
