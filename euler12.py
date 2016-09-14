import time

start= time.time()

def getDivsors(num):
    divsor = 0
    count=0
    con = True
    while con and num!=1:
        if (num%2==0):
            num=num/2
            count+=1
        else:
            con = False
    if count>0:
        divsor=count+1
    count=0
    div = 3
    while num!=1:
        con = True
        while num!=1 and con:
            if(num%div==0):
                num=num/div
                count+=1
            else:
                con=False
        if count>0:
            divsor=divsor*(count+1)
        count=0
        div+=2
    return divsor

triNum = 4
num=10
divsors = 0
while divsors<501:
    x = getDivsors(num)
    if x>divsors:
        divsors=x
    triNum+=1
    num=num+triNum

print(str(triNum-1)+" "+str(num-triNum)+" "+str(divsors))

end=time.time()
print(end-start)
