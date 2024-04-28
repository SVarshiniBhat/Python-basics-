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





l=[1,2,3,4,5,6,7]

head=None

for ele in l:
    head=insertatendofhead(head,ele)
printlinkedlist(head)

head=deleteAtHead(head)

printlinkedlist(head)


head=deleteAtHead(head)

printlinkedlist(head)


head=deleteAtHead(head)

printlinkedlist(head)


head=deleteAtHead(head)

printlinkedlist(head)


head=deleteAtHead(head)

printlinkedlist(head)


head=deleteAtHead(head)

printlinkedlist(head)
