import sys
n = int(input())
nums = list(map(int , sys.stdin.readline().split()))
m = int(input())
def finds(x):
    left , right = 0 , len(nums)-1
    while left < right:
        mid = (left + right)//2
        if nums[mid]>=x:
            right = mid
        else:
            left = mid + 1
    return left
pos = finds(m)
if nums[pos]==m and pos < n:
    print("Yes")
else:
    print("No")