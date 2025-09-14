from collections import deque
def build_deq(n):
    d = deque()
    for i in range(n , 0 , -1):
        d.appendleft(i)
        d.rotate(i)
    return list(d)
def main():
    n = int(input().strip())
    res = []
    for i in range(n):
        b = int(input().strip())
        deck = build_deq(b)
        res.append(" ".join(map(str , deck)))
    print("\n".join(res))
if __name__ == "__main__":
    main()
