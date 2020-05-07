"""
ソートアルゴリズム
"""

# バブルソート (計算量O(N^2),メモリO(1))
def bubble_sort(a):
    N = len(a)
    for j in range(N-1):
        i = N-1
        while i > j:
            if a[i] < a[i-1]:
                a[i],a[i-1] = a[i-1],a[i]
            i -= 1
    return a

# 挿入ソート
def insertion_sort(a):
    N = len(a)
    for i in range(1,N):
        j = i
        while j > 0:
            if a[j] < a[j-1]:
                a[j],a[j-1] = a[j-1],a[j]
                j-=1
                continue
            else:
                break
    return a

# 選択ソート
def selection_sort(a):    
    N = len(a)
    for i in range(N-1):
        min_index = a[i:].index(min(a[i:]))
        a[i],a[i+min_index] = a[i+min_index],a[i]
    return a

# マージソート
def merge_sort(a):
    if len(a) <= 1:
        return a
    mid = len(a)//2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    return merge(left,right)

def merge(l1,l2):
    merged = []
    pointer1 = 0
    pointer2 = 0
    while pointer1 < len(l1) and pointer2 < len(l2):
        if l1[pointer1] >= l2[pointer2]:
            merged.append(l2[pointer2])
            pointer2 += 1
        else:
            merged.append(l1[pointer1])
            pointer1 += 1
    if pointer1 == len(l1):
        for i in range(pointer2,len(l2)):
            merged.append(l2[i])
    elif pointer2 == len(l2):
        for i in range(pointer1,len(l1)):
            merged.append(l1[i])
    return merged

# ヒープソート
def heap_sort(a):
    heap = Heap(a)
    sorted_list = []
    for _ in range(len(a)):
        sorted_list.append(heap.pop())
    return sorted_list

def default_sort(a):
    return sorted(a)

# 基数ソート(10進数)O(nm)
def radix_sort(a,m):
    for d in range(1,m+1): #i桁めに注目
        buckets = [[] for _ in range(10)]

        r = 10**(d-1)

        for num in a:
            key = (num//r)%10 #dけためを取り出す
            buckets[key].append(num)
            
        i = 0
        for bucket in buckets:
            for value in bucket:
                a[i] = value
                i += 1
    return a

# print(bubble_sort([1,3,2,7,5,4,100,2,1,50]))
# print(selection_sort([1,3,2,7,5,4,100,2,1,50]))
# print(merge_sort([1,3,2,7,5,4,100,2,1,50]))

"""
ヒープ
"""
class Heap():
    def __init__(self,li):
        self.tree = []
        for x in li:
            self.push(x)

    def push(self,x):        
        pointer = len(self.tree)
        self.tree.append(x)

        while pointer > 0:            
            parent_index = (pointer-1)//2
            if self.tree[pointer] < self.tree[parent_index]:
                self.tree[pointer],self.tree[parent_index] = self.tree[parent_index],self.tree[pointer]
                pointer = parent_index
            else:
                break
    
    def pop(self):
        if not self.tree:
            raise Exception('heap is empty')
        rvalue = self.tree[0]
        self.tree[0] = self.tree[-1]
        self.tree.pop()
        pointer = 0
        LEN = len(self.tree)

        while True:
            left = pointer*2+1
            right = pointer*2+2

            if left >= LEN:
                break
            elif right >= LEN:
                if self.tree[pointer] <= self.tree[left]:
                    break
                else:
                    self.tree[pointer],self.tree[left] = self.tree[left],self.tree[pointer]
                    break

            if self.tree[pointer] <= self.tree[left] and self.tree[pointer] <= self.tree[right]:
                break
            elif self.tree[left] <= self.tree[right]:
                self.tree[left],self.tree[pointer] = self.tree[pointer],self.tree[left]
                pointer = left
            elif self.tree[left] > self.tree[right]:
                self.tree[right],self.tree[pointer] = self.tree[pointer],self.tree[right]
                pointer = right
        return rvalue



import random
import timeit
li = [random.randrange(10**2) for _ in range(10**5)]
print("heapsort:{}".format(timeit.timeit(lambda: heap_sort(li), number=1)))
print("mergesort:{}".format(timeit.timeit(lambda: merge_sort(li), number=1)))
print("radixsort:{}".format(timeit.timeit(lambda: radix_sort(li,3), number=1)))