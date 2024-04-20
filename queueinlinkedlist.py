class node:
    def __init__(self,data):
        self.data=data
        self.next=None

def enqueue(head,val):
    print(val,"inserted")
    newblock=node(val)
    if head==None:
        return newblock
    tail=head
    while tail.next!=None:
        tail=tail.next
    tail.next=newblock
    return head

def dequeue(head):
    if head==None:
        print("queue is empty")
        return
    print(head.data)
    secondnode=head.next
    head.next=None
    return secondnode

def printFrontQueue(head):
    if head==None:
        print("queue is empty")
        return
    print(head.data)

def printqueue(head):
    if head==None:
        print("queue is empty")
        return None
    cur=head
    while cur!=None:
        print(cur.data,end=" ")
        cur=cur.next
    print()

def queueEmpty(head):
    if head==None:
        print("Queue is empty")
    else:
        print("Queue is not empty")
    

head=None
n=int(input())
for i in range(n):
    l=list(map(int,input().split()))
    w=l[0]
    if w==1:
        ele=l[1]
        head=enqueue(head,ele)
    elif w==2:
        printFrontQueue(head)
    elif w==3:
        head=dequeue(head)
    elif w==4:
        printqueue(head)
    elif w==5:
        queueEmpty(head)
