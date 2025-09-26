import sys , math
a , b = map(int , sys.stdin.readline().split())
s = list(map(int , sys.stdin.readline().split()))
def can(C):
    trips = 0
    for x in s:
        trips+=math.ceil(x/C)
        if trips > b:
            return False
    return trips <= b
left , right = 1 , max(s)
ans = right
while left <= right:
    mid = (left + right)//2
    if can(mid):
        ans = mid
        right = mid - 1
    else:
        left = mid + 1
print(ans)

