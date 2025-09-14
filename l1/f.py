def primenumbers(n):
    is_prime = True
    for i in range(2 , int(n**0.5)+1):
        if n%i==0:
            is_prime = False
            break
    return is_prime
def main():
    prime = []
    n = int(input())
    for i in range (n):
        for j in range(2 , 1000000000):
            if primenumbers(j):
                prime.append(j)
                if len(prime)==n:
                    break
        if len(prime)==n:
            break
    print(prime[-1])

if __name__=="__main__":
    main()