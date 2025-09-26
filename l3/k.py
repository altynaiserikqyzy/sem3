import sys
import bisect
n, S = map(int, sys.stdin.readline().strip().split())
arr = list(map(int, sys.stdin.readline().strip().split()))
prefix = [0]
for x in arr:
    prefix.append(prefix[-1] + x)
min_len = n + 1  
for l in range(n):
    target = prefix[l] + S
    r = bisect.bisect_left(prefix, target)
    if r <= n:
        min_len = min(min_len, r - l)
print(min_len)