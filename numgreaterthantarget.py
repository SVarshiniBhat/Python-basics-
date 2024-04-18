def findgreaternumthanTarget(l,target):
   result =0  
   n=len(l)
   for i in range(n):
        if l[i]>target:
            result =result+1
            print(l[i],end=" ")
   print()
   return result 
            

l=[15,18,2,22,18,200,18]
Target=2
result= findgreaternumthanTarget(l,Target)
print("total no of num greater than Target is :",result )
