def balance(s : str)->str:
    stack = []
    for char in s:
        if stack and char == stack[-1]:
            stack.pop()
        else:
            stack.append(char)
    if stack:
        return "No"
    else:   
        return "Yes"
def main():
    s = input().strip()
    print(balance(s))
if __name__=="__main__":
    main()
