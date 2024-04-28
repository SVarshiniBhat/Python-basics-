class node:
    def __init__(self,data):
        self.data=data
        self.next =None

def printlinkedlist(head):
    cur=head
    while cur!=None:
        print(cur.data,end=" ")
        cur=cur.next

    print()


def insertatendofhead(head,ele):
    newblock=node(ele)
    if head==None:
        return newblock
    newblock.next=head
    return newblock

def insertNodeAtSpecificPosition(head,data,position):
    newBlock=node(data)
    if position==1:
        newBlock.next=head
        return newBlock
    index=1
    curr=head
    while index!=position:
        curr=curr.next                    
        index+=1
    newBlock.next=curr.next
    curr.next=newBlock
    return head

n=int(input())
l=input()
y=l.split()
lists=list(map(int,y))
temp = list(map(int, input().split()))

position,data=temp[0],temp[1]

head=None

for ele in lists:

    head=insertatendofhead(head,ele)

printlinkedlist(head)
head=insertNodeAtSpecificPosition(head,data,position)
printlinkedlist(head)
