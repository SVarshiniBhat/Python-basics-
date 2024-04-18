#pattern-1
n=int(input())
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()


#pattern-2
n=int(input())
for i in range(n):
    for j in range(i+1):
        if i%2==0:
            print(i+1,end="")
        else:
            print("@",end="")
    print()


#pattern-3
n = int(input())
for row in range(n):
   for col in range(n):
       print("*", end = "")
   print()


#pattern-5
n=int(input())
space=0
for i in range(n):
    for j in range(space):
        print(" ",end="")
    for j in range(n):
        print("*",end="")
    space=space+1
    print()


#pattern-6
n=int(input())
star=n
for i in range(n):
    for j in range(star):
        print("*",end="")
    star=star-1
    print()

  
#pattern-7
n=int(input())
space=n-1
for i in range(n):
    for j in range(space):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    space-=1
    print()


#pattern-8
n=int(input())
space=n-1
for i in range(n):
    for j in range(space):
        print(" ",end="")
    for j in range(i+1):
        print(j+1,end="")
    space-=1
    print()


#pattern-9
n=int(input())
space=0
star=n
for i in range(n):
    for j in range(space):
        print(" ",end="")
    for j in range(star):
        print("*",end="")
    space+=1
    star-=1
    print()
    

#pattern-10
n=int(input())
space=n-1
star=0
for i in range(n):
    for j in range(space):
        print(" ",end="")
    for j in range(star):
        print("*",end="")
    space-=1
    star+=1
    print()
    

#pattern-11
n=int(input())
space=n-1
star=1
for i in range(n):
    for j in range(space):
        print(" ",end="")
    for j in range(star):
        print("*",end="")
    space-=1
    star+=2
    print()


#pattern-12
n=int(input())
space=n-1
for i in range(n):
    for j in range(space):
        print(" ",end="")
    for j in range(2*i+1):
        print(j+1,end="")
    space-=1
    print()


#patterm-13
n=int(input())
space=n-1
alpha=65
for i in range(n):
    for j in range(space):
        print(" ",end="")
    for j in range(2*i-1):
        print(chr(alpha),end="")
        alpha+=1

    space-=1

    print()
    
    
#pattern-14
n=int(input())
space=0

for i in range(n,0,-1):
    for j in range(space):
        print(" ",end="")
    for j in range(2*i-1):
        print("*",end="")
    space+=1
    
    print()


#pattern-15
n=int(input())
space=0

for i in range(n,0,-1):
    for j in range(space):
        print(" ",end=" ")
    for j in range(2*i-1):
        print(j+1,end=" ")
    space+=1
    
    print()


#pattern-16
n=int(input())
for i in range(n):
    for j in range(i+1):
        if i%2==0:
            print("*",end="")
        else:
            print("#",end="")
    print()


#pattern-17
n=int(input())
for i in range(1,n+1):
    if i%2==0:

        for j in range(i,0,-1):
            print(j,end=" ")
    else:
        for k in range(1,i+1):
                print(k,end=" ")
    print()


#pattern-18
n=int(input())
space=0
alpha=65
for i in range(n,0,-1):
    for j in range(space):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(chr(alpha),end=" ")
        alpha+=1
    alpha=65
    space+=1
    print()
    
