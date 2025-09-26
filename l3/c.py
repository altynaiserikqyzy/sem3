import sys 
def bisect_left(arr, x):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid
    return left
def bisect_right(arr, x):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= x:
            left = mid + 1
        else:
            right = mid
    return left
data = list(map(int , sys.stdin.read().split()))
n , q = data[0] , data[1]
arr =data[2:2+n]
queries = data[2+n:]
arr.sort()
def count(l , r):
    left = bisect_left(arr , l)
    right = bisect_right(arr , r)
    return right - left
out = []
for i in range(q):
    l1 , r1 , l2, r2 = queries[4*i:4*i+4]
    ans = count(l1 , r1)+count(l2 , r2)
    L , R = max(l1 , l2) , min(r1 , r2)
    if L<= R:
        ans -= count(L , R)
    out.append(str(ans))
print("\n".join(out))

