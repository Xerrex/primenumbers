def printprimenumber(n):
    valuelist=[]
    if type(n)!=int:
        raise ValueError('number Must be integer')

    for x in range(2,n+1):
        for v in range(2,x+1):
            if x%v!=0:
                if x not in valuelist:
                    valuelist.append(x)



    return valuelist


x= printprimenumber(10)
print (x)