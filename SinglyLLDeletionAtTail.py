class node:
    def __init__(self,data):
        self.data=data
        self.next=None

def printlinkedlist(head):
    cur=head
    while cur!=None:
        print(cur.data,end=" ")
        cur=cur.next
    print()
    
def insertatendoftail(head,ele): 
    newblock=node(ele)
    if head==None:
        return newblock
    cur=head
    while cur.next!=None:
        cur=cur.next
    cur.next=newblock
    return head


def deleteAtTail(head):
    cur=head
    previous=None
    while cur.next!=None:
        previous=cur
        cur=cur.next
    previous.next=None
    return head

n=int(input())
n1=input()
y=n1.split()
l=list(map(int,y))
head=None
for ele in l:
    head=insertatendoftail(head,ele)
printlinkedlist(head)
head=deleteAtTail(head)
printlinkedlist(head)

        
