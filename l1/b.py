def age(*n):
    stack = []
    for i in range(len(n)):
        found = -1
        for j in range(i-1 , -1 , -1):
            if n[j] <= n[i]:
                found = n[j]
                break
        stack.append(found) 
        found = -1                 
    return stack
def main():
    n = int(input().strip())
    arr = list(map(int, input().split())) # читаем n чисел в строке
    print(" ".join(map(str, age(*arr))))
if __name__=="__main__":
    main()