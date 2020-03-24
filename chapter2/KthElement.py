from LinkedList import LinkedList
import unittest

def find_kth_element(ll,k):
    cur = ll.head
    length = 0

    while cur:
        length += 1
        cur = cur.next
    
    cur = ll.head
    distance = 0
    while cur:
        if distance == length - k:
            return cur.value
        else:
            cur = cur.next 
            distance += 1
    
    raise Exception


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([1,2,3,4,5,4,3,2,3,4], 3, 2),
        ([1,2,3,4,5,4,3,2,3,4], 4, 3),
        ([1,2,3,4,5,4,3,2,3,4], 9, 2),
        ([1,2,3,4,5,4,3,2,3,4], 1, 4),
        ([1], 1, 1),
    ]

    def test_find(self):
        for values, K , answer in self.data:
            ll = LinkedList(values=values)
            actual = find_kth_element(ll,K)
            self.assertEqual(actual, answer)

if __name__ == "__main__":
    unittest.main()