import sys
n , k  = map(int , sys.stdin.readline().split())

sheep = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
def enough(l):
    count = 0
    for x1 , y1 , x2 , y2 in sheep:
        if x1 >= 0 and y1 >= 0 and x2 <= l and y2 <= l: 
            count+=1
    return count>=k
left , right = 0 , 10**9
while left +1 < right :
    mid = (left + right)//2
    if enough(mid):
        right = mid
    else:
        left = mid
print(right)