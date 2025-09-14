def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def nth_superprime(n: int) -> int:
    primes = []          # список простых
    num = 2
    while len(primes) < 2000:    # с запасом
        if is_prime(num):
            primes.append(num)
        num += 1

    superprimes = []
    for idx, p in enumerate(primes, start=1):  # индексация с 1!
        if is_prime(idx):
            superprimes.append(p)

    return superprimes[n-1]

def main():
    n = int(input())
    print(nth_superprime(n))

if __name__ == "__main__":
    main()