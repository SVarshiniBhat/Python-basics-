#pattern-1
n=int(input())
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()
#output
*
**
***
****
*****

#pattern-2
n=int(input())
for i in range(n):
    for j in range(i+1):
        if i%2==0:
            print(i+1,end="")
        else:
            print("@",end="")
    print()
#output
1
@@
333
@@@@
55555



#pattern-3
n = int(input())
for row in range(n):
   for col in range(n):
       print("*", end = "")
   print()
#output
*****
*****
*****
*****
*****


#pattern-4
n = int(input())
val = 10
for i in range(1, n + 1):
   for j in range(i):
       print(val, end = " ")
       val = val+10
   print()
#output
10 
20 30 
40 50 60 
70 80 90 100 
110 120 130 140 150 


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
#output
*****
 *****
  *****
   *****
    *****

#pattern-6
n=int(input())
star=n
for i in range(n):
    for j in range(star):
        print("*",end="")
    star=star-1
    print()
   #output
*****
****
***
**
*

  
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
   #Output
    *
   **
  ***
 ****
*****


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
#output
    1
   12
  123
 1234
12345

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
#output
*****
 ****
  ***
   **
    *

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
#output
    
   *
  **
 ***
****
    

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
#Output
    *
   ***
  *****
 *******
*********

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
#Output
    1
   123
  12345
 1234567
123456789

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
#Output
    
   A
  BCD
 EFGHI
JKLMNOP


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
#Output
*********
 *******
  *****
   ***
    *


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
#Output
1 2 3 4 5 6 7 8 9 
  1 2 3 4 5 6 7 
    1 2 3 4 5 
      1 2 3 
        1 

#pattern-16
n=int(input())
for i in range(n):
    for j in range(i+1):
        if i%2==0:
            print("*",end="")
        else:
            print("#",end="")
    print()
#Output
*
##
***
####
*****

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
#Output
1 
2 1 
1 2 3 
4 3 2 1 
1 2 3 4 5


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
#Output
A B C D E 
  A B C D 
    A B C 
      A B 
        A
    
#pattern-19
n=int(input())
space=n-1
star=1
for i in range(n):
    for i in range(space):
        print(" ", end=" ")
    for j in range(star):
        print("*", end=" ")
    print()
    space=space-1
    star=star+2
space=1
for i in range(n-1,0,-1):
    for j in range(space):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    space+=1
    print()   
#Output
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 
  * * * * * * * 
    * * * * * 
      * * * 
        * 


#pattern-20
n=int(input())
space=0
for i in range(n,1,-1):
    for j in range(space):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    space+=1
    print()
space=n-1
star=1
for i in range(n):
    for i in range(space):
        print(" ", end=" ")
    for j in range(star):
        print("*", end=" ")
    print()
    space=space-1
    star=star+2
#Output
* * * * * * * * * 
  * * * * * * * 
    * * * * * 
      * * * 
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 

#pattern 21
n=int(input())
v=1
for i in range(1,n+1):
     for j in range(i):
         print(v,end=" ")
         v=v+1
     print()
#output
1
2 3
4 5 6
7 8 9 10

#pattern 22
n=int(input())
v=1
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    for j in range(i):
        print(v,end=" ")
        v=v+1
    print()
#output
4
    1 
   2 3 
  4 5 6 
 7 8 9 10 

#pattern 23
n=int(input())
v=1
for i in range(1,n+1):
    for j in range(i):
        print(v**2,end=" ")
        v=v+1
    print()
#output
4
1 
4 9 
16 25 36 
49 64 81 100 

#pattern 24
 
n=int(input())
v=1
for i in range(n):
    for j in range(2*i+1):
        print(v**2,end=" ")
        v=v+1
    print()
#output
4
1 
4 9 16
25 36 49 64 81
100 121 144 169 196 225 256

#pattern 25
n=int(input())
v=1
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(v,end=" ")
            v=v+1
    print()
#output
4
* * * * 
* 1 2 *
* 3 4 *
* * * *


#pattern 21


#pattern 22 using while loop
n=int(input())
v=1
i=1
while i<n+1:
    print(" "*(n-i),end=" ")
    j=0
    while j<i:
        print(v,end=" ")
        v=v+1
        j=j+1
    print()
    i=i+1
#output
4
    1 
   2 3
  4 5 6
 7 8 9 10

#pattern 23 using while loop
n=int(input())
i=0
v=1
while i<n:
    j=0
    while j<i+1:
        print(v**2,end=" ")
        v=v+1
        j=j+1
    print()
    i=i+1
#output
4
1 
4 9 
16 25 36 
49 64 81 100 


#pattern 24 using while loop
n=int(input())
i=0
v=1
while i<n:
    j=0
    while j<2*i+1:
        print(v**2,end=" ")
        v=v+1
        j=j+1
    print()
    i=i+1
#output
4
1 
4 9 16
25 36 49 64 81
100 121 144 169 196 225 256

#pattern 25 using while loop
n=int(input())
v=1
i=0
while i<n:
    j=0
    while j<n:
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(v,end=" ")
            v=v+1
        j=j+1
    print()
    i=i+1
#output
4
* * * * 
* 1 2 *
* 3 4 *
* * * *

   
#pattern 26
n=input()
for i in range (len(n)):
    for j in range(i,len(n)):
        print(n[i:j+1],end=" ")
    print()

#output
abcd
a ab abc abcd 
b bc bcd 
c cd 
d 

























