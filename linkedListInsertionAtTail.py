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


def insertatendoftail(head,ele): 
    newblock=node(ele)
    if head==None:
        return newblock
    cur=head
    while cur.next!=None:
        cur=cur.next
    cur.next=newblock
    return head

n=int(input())
l=input()
y=l.split()
lists=list(map(int,y))

head=None

for ele in lists:

    head=insertatendoftail(head,ele)

printlinkedlist(head)
