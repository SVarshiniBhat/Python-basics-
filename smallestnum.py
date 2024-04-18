def findsmallestnum(l):
    n=len(l)
    temp=10000
    for i in range(n):
        if l[i]<temp:
           temp=l[i]
    return temp 
l=[4,2,5,2,9,5,5,4,7]
temp=findsmallestnum(l)
print("smallest num =",temp)
