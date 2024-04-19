target=int(input())
n=int(input())
n1=input()
y=n1.split()
l=list(map(int,y))
visited=0
for i in range(n):
    if l[i]==target:
        print("Target is present at index:",i)
        visited=1
        break
if visited==0:
    print("Target is not present")
