import sys , math
n , m  = map(int , sys.stdin.readline().split())
nums = list(map(int , sys.stdin.readline().split()))
def can(k):
    total = 0
    for x in nums :
        total += math.ceil(x/k)
        if total > m:
            return False
    return True
left , right = 1 , max(nums)
ans = right
while left <= right :
    mid = (left + right) //2
    if can(mid):
        ans = mid
        right = mid - 1
    else :
        left = mid + 1
print(ans)
        
