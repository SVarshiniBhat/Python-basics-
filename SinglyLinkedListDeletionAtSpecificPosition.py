class node:
    def __init__(self,data):
        self.data=data
        self.next =None


def printlinkedlist(head):
    cur=head
    while cur!=None:
        print(cur.data,end="-->")
        cur=cur.next
    print()


def insertatendofhead(head,ele):
    newblock=node(ele)
    if head==None:
        return newblock
    newblock.next=head
    return newblock

def deleteAtHead(head):
    if head==None:
        return None
    secondnode=head.next
    head.next=None
    return secondnode

def deleteAtSpecificPosition(head,position):
    if position==1:
        return deleteAtHead(head)
    cur=head
    index=1
    while index!=position-1:
        cur=cur.next
        index+=1
    mainnode=cur.next
    nextnode=mainnode.next
    mainnode.next=None
    cur.next=None
    cur.next=nextnode
    return head

    



l=list(map(int,input().split()))
position=int(input())

head=None

for ele in l:
    head=insertatendofhead(head,ele)
printlinkedlist(head)

head=deleteAtSpecificPosition(head,position)
printlinkedlist(head)
head=deleteAtSpecificPosition(head,position)

printlinkedlist(head)
