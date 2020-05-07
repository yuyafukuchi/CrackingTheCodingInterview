import sys
sys.setrecursionlimit(10**9)
import timeit

# xのn乗を計算する関数 O(n)
def pow_normal(x: int, n: int):
    return x**n

def pow_recursive(x,n):
    if n == 0:
        return 1
    
    return pow_recursive(x,n-1)*x

# 2分累乗法　O(logN)
def pow_binary(x,n):
    if n == 0:
        return 1
    
    if n&1:
        return pow_binary(x,n//2)**2*x
    else:
        return pow_binary(x,n//2)**2

# loop = 10000
# result = timeit.timeit(lambda: pow_binary(3,10000), number=loop)
# print(result)
# result = timeit.timeit(lambda: pow_normal(3,10000), number=loop)
# print(result)


"""
フィボナッチ数列
"""
def fib(n):
    a = 0
    b = 1
    rvalue = []
    while a < n:
        rvalue.append(a)
        a,b = b,a+b
    return rvalue


"""
Bit演算
"""
# i桁目のbitの値を取得
def getBit(num,i):
    return num & (1<<i)

# i桁目のbitの値を1に
def setBit(num,i):
    return num | 1 << i

# i桁目のbitの値を0に
def clearBit(num,i):
    mask = ~(1<<i)
    return num & mask

# 最上位ビットからiビット目までをクリア
def clearBitsMSBthroughI(num,i):
    mask = (1<<i)-1 ## 000001111
    return num & mask

# iビット目から0ビット目までをクリア
def clearBitsIthrough0(num,i):
    mask = -1<<(i+1) # -1は全て1のビット列である
    return num&mask

# iビット目をvに
def updateBit(num,i,v):
    mask = ~(1<<i)
    return (num&mask)|(v<<i)


"""
素数
"""
# nが素数であるかどうか調べる(O(√n))
def isPrime(n):
    if n < 2: return False
    
    for i in range(2,n**(0.5)+1):
        if n%i == 0:
            return False

    return True    

# エラトステネスのふるい(n以下の素数全列挙)
def sieve(n):
    if n <= 1: return []
    is_prime = [True] * (n+1)
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2,int(n**0.5)+1):
        if not is_prime[i]: continue
        for j in range(i*2,n+1,i):
            is_prime[j] = False
    
    return [i for i in range(n+1) if is_prime[i]]


def bisect_left(a,element):
    lo = -1
    hi = len(a)
    # hiはelement以上の値を持つ最小のindex
    while hi - lo > 1:
        mid = (hi+lo)//2
        if a[mid] >= element:
            hi = mid
        else:
            lo = mid
    return hi

def bisect_right(a,element):
    lo = -1
    hi = len(a)
    # hiはelementより大きい値を持つ最小の要素のindex
    while hi - lo > 1:
        mid = (hi+lo)//2
        if a[mid] > element:
            hi = mid
        else:
            lo = mid
    return hi

# from bisect import bisect_left,bisect_right
# a = [1,3,3,5]
# print(bisect_left(a,0))
# print(bisect_left(a,1))
# print(bisect_left(a,2))
# print(bisect_left(a,3))
# print(bisect_left(a,5))
# print(bisect_left(a,6))
# print()
# print(bisect_right(a,0))
# print(bisect_right(a,1))
# print(bisect_right(a,2))
# print(bisect_right(a,3))
# print(bisect_right(a,5))
# print(bisect_right(a,6))










    