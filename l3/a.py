import sys
a = sys.stdin.read().split()
t = int(a[0])
queries = list(map(int, a[1:1+t]))
n, m = map(int, a[1+t:3+t])
res = list(map(int , a[3+t:]))
pos = {}
indx = 0
for i in range(n):
    for j in range(m):
        val = res[indx]
        pos[val]=(i , j)
        indx+=1
for q in queries:
    if q in pos:
        print(pos[q][0] , pos[q][1])
    else:
        print(-1)