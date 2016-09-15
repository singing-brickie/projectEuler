import time

start = time.time()

units = [{'num':1,'str':"one"},{'num':2,'str':"two"},{'num':3,'str':"three"},{'num':4,'str':"four"},
    {'num':5,'str':"five"},{'num':6,'str':"six"},{'num':7,'str':"seven"},{'num':8,'str':"eight"}
    ,{'num':9,'str':"nine"},{'num':10,'str':"ten"},{'num':11,'str':"eleven"},{'num':12,'str':"twelve"},
    {'num': 13, 'str': "thirteen"}, {'num': 14, 'str': "fourteen"}, {'num': 15, 'str': "fifteen"},
         {'num': 16, 'str': "sixteen"}, {'num': 17, 'str': "seventeen"}, {'num': 18, 'str': "eighteen"},
         {'num': 19, 'str': "nineteen"}]

tens = [{'num':10,'str':'ten'},{'num':20,'str':"twenty"},{'num':30,'str':"thirty"},{'num':40,'str':"forty"},
        {'num': 50, 'str': "fifty"}, {'num': 60, 'str': "sixty"}, {'num': 70, 'str': "seventy"},
        {'num': 80, 'str': "eighty"}, {'num': 90, 'str': "ninety"}]

count=0

for i in range (1,20):
    count+=len(units[i-1]['str'])

for j in range (20,100):
    x=j%10
    myStr=''
    y=(j-x)
    for ten in tens:
        if ten['num']==y:
            myStr+=ten['str']
            break
    for unit in units:
        if unit['num'] == x:
            myStr+=unit['str']
            break
    count+=len(myStr)


for s in range(100,1000):
    x=s%100
    t=(s-x)/100
    myStr=''
    for unit in units:
        if unit['num']==t:
            myStr+=unit['str']
            myStr+='hundred'
            break
    if x<20:
        for unit in units:
            if unit['num']==x:
                myStr+='and'
                myStr+=unit['str']
                break
    else:
        v=x%10
        u=(x-v)
        for ten in tens:
            if ten['num']==u:
                myStr+='and'
                myStr+=ten['str']
        for unit in units:
            if unit['num']==v:
                myStr+=unit['str']
                break

    count+=len(myStr)

count+=len('onethousand')
print(count)
end=time.time()
print(end-start)



