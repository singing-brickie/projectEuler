import time

start = time.time()

lines = open('textFiles/euler8').read().splitlines()
x = ''

for i in range(0, 20):
    x += lines[i]
count = 0
for i in range(0, len(x) - 13):
    temp = 1
    for j in range(0, 13):
        temp = temp * int(x[i + j])
    if temp > count:
        count = temp

print(count)

end = time.time()

print(start-end)
