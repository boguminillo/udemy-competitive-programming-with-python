from math import sqrt


def sieveDelete(x):
    primes = [2] + list(range(3, x, 2))
    start = 1
    while primes[start] < sqrt(x):
        for i in range(len(primes)-1, start, -1):
            if primes[i] % primes[start] == 0:
                del primes[i]
        start += 1
    return primes


def sieveBool(x):
    primesBool = [True] * (x + 1)
    primesBool[0] = False
    primesBool[1] = False
    for i in range(2, int(sqrt(x))):
        if primesBool[i]:
            for j in range(i*i, x+1, i):
                primesBool[j] = False
    primes = [i for i in range(len(primesBool)) if primesBool[i]]
    return primes


def main():
    primes = sieveDelete(100)
    print(primes)
    primes = sieveBool(100)
    print(primes)


if __name__ == '__main__':
    main()
