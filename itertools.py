import itertools

def permutations(nums):
    """
    aのありうる順列を全て返す

    Parameters
    ---------
    nums: [int]
    """
    N = len(nums)
    if N <= 1: return [nums]

    perm_list = []
    for i in range(N):
        for perm in permutations(nums[:i]+nums[i+1:]):
            perm_list.append([nums[i]]+perm)

    return perm_list

def permutaions_backtracking(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    def backtrack(first = 0):
        if first == n:  
            output.append(nums[:])
        for i in range(first, n):
            nums[first], nums[i] = nums[i], nums[first]
            backtrack(first + 1)
            nums[first], nums[i] = nums[i], nums[first]
    
    n = len(nums)
    output = []
    backtrack()
    return output  


def combinations(nums,k):
    if k <= 1:
        return [[num] for num in nums]

    N = len(nums)
    comb_list = []
    if N < k: return []

    for i in range(N):
        for comb in combinations(nums[i+1:],k-1):
            comb_list.append([nums[i]]+comb)
    
    return comb_list

def combinations_backtracking(nums, k):
    output = []
    N = len(nums)
    def backtrack(first = 0, curr = []):
        if len(curr) == k:  
            output.append(curr[:])
            return
        for i in range(first, N):
            curr.append(nums[i])
            backtrack(i+1, curr)
            curr.pop()
    
    backtrack()
    return output

nums = [1,2,3,4,5,6,7]
# print(list(itertools.combinations(nums,2)))
# print(combinations_backtracking(nums,2))

def combinations_with_replacement(nums,k,j):
    if k == 0:
        return [[]]

    output = []
    for i in range(j,len(nums)):
        for comb in combinations_with_replacement(nums,k-1,i):
            output.append([nums[i]]+comb)
    return output

def combinations_with_replacement_backtrack(nums,k):
    output = []
    def backtrack(first=0,cur=[]):
        if len(cur) == k:
            output.append(cur[:])
            return 
        for i in range(first,len(nums)):
            cur.append(nums[i])
            backtrack(i,cur) # 重複組み合わせなのでiを渡している
            cur.pop()

    backtrack()
    return output

# print(combinations_with_replacement_backtrack(nums,3))
# print(list(itertools.combinations_with_replacement(nums,3)))

def product(nums,repeat):
    if repeat == 0:
        return [[]]

    output = []
    for i in range(len(nums)):
        for p in product(nums,repeat-1):
            output.append([nums[i]]+p)
    return output

print(product([1,2,3],3))