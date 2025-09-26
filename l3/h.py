import sys 
n , m = list(map(int , sys.stdin.readline().split()))
block = list(map(int , sys.stdin.readline().split()))
def bisect_left(arr , x):
    left , right = 0 , len(arr)
    while left < right :
        mid = (left+right)//2
        if arr[mid]< x:
            left = mid + 1
        else:
            right = mid
    return left
end = []
s = 0
for i in range(n):
    s+=block[i]
    end.append(s)
for _ in range(m):
    x = int(sys.stdin.readline())
    block_index = bisect_left(end , x)
    print(block_index+1)