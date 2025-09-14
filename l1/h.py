from collections import deque
def solve():
    d = deque()
    while True:
        try:
            n= input().split()
        except EOFError:
            break
        if not n :
            continue
        if n[0]=='+':
            d.appendleft(int(n[1]))
        if n[0]=='-':
            d.append(int(n[1]))
        if n[0]=='*':
            if d:
                print(d[0]+d[-1])
                d.pop()
                if d:
                    d.popleft()
            else:
                print("error")
        if n[0]=='!':
            break
if __name__=="__main__":
    solve()