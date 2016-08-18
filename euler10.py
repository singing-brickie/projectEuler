import time
import math

start = time.time()

primes = [3]

count = 5


def isPrime(num):
    for prime in primes:
        if prime > math.sqrt(num) + 1:
            primes.append(num)
            return True

        if num % prime == 0:
            return False
    primes.append(num)
    return True


for i in range(5, 2000000, 2):
    if isPrime(i):
        count += i

print(count)

end = time.time()

print(end - start)
