from collections import deque
def vs(boris , nurs):
    move = 0
    maxmove=10**6
    while nurs and boris and move < maxmove:
        move +=1
        b = boris.popleft()
        n = nurs.popleft()
        if (b == 0 and n == 9) or (b > n and not (b == 9 and n == 0)):
            boris.append(b)
            boris.append(n)
        else:
            nurs.append(b)
            nurs.append(n)
    if move >=maxmove:
        return "blin nichya"
    elif not boris:
        return(f"Nursik {move}")
    elif not nurs:
        return(f"Boris {move}")
def main():
    boris_cards = list(map(int, input().split()))
    nursik_cards = list(map(int, input().split()))
    print(vs(deque(boris_cards) , deque(nursik_cards)))
if __name__=="__main__":
    main()
