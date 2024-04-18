def findgreaternum(l):
    n=len(l)
    temp=0
    for i in range(n):
        if l[i]>temp:
           temp=l[i]
    return temp 
    
l=[1,2,4,2,5,2,9,5,5,4,7]
temp=findgreaternum(l)
print("greatest num =",temp)
