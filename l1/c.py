def backspace(s : str)-> str:
    stack = []
    for char in s:
        if char == "#":
            if stack:
                stack.pop()
            else:
                continue
        else:
            stack.append(char)
    return "".join(stack)
def main():
    a,b = input().split()

    if backspace(a) == backspace(b):
        print("Yes")
    else:
        print("No")
if __name__ == "__main__":
    main()
        

