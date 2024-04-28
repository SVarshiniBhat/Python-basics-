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


n=int(input())
l=input()
y=l.split()
lists=list(map(int,y))

head=None

for ele in lists:

    head=insertatendofhead(head,ele)

printlinkedlist(head)
