import time

start=time.time()

months = [31,28,31,30,31,30,31,31,30,31,30,31]

year = 1901
day=3
count=0
while year<2001:
    if year%4==0 and year!=1900:
        months[1]=29
    else:
        months[1]=28

    for i in range(0,12):
        for j in range(1,months[i]+1):
            if j==1 and j==day:
                count+=1
            if day==7:
                day=1
            else:
                day+=1

    year+=1
end=time.time()


print(count)

print(end-start)
