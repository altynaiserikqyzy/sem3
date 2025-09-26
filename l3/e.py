import sys
def count_leq(arr , x):
    left , right = 0 , len(arr)
    while left < right:
        mid = (left + right )//2
        if arr[mid] <= x:
            left = mid + 1
        else : 
            right = mid
    return left 
data = list(map(int , sys.stdin.read().split()))
n = data[0]
arr = data[1:1+n]
arr.sort()
q = data[1+n]
powers = data[2+n:]
pref = [0]
for x in arr:
    pref.append(pref[-1]+x)
for P in powers:
    idx = count_leq(arr , P)
    print(idx , pref[idx])
