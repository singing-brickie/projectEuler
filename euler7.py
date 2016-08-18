import time

start = time.time()

primes= [2,3,5,7,11,13]

def check(num):
    for x in primes:
        if num%x==0:
            return False

    return True
count = 17
while(len(primes)<10001):
    if(check(count)):
        primes.append(count)
    count+=1

print(primes[10000])

end= time.time()

print(end)
