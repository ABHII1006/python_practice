
class Node :
    def __init__(self,data):
        self.val=data
        self.next=None

dummy=Node(0)
current=dummy
l=[1,2,3,5]
for i in l:
    current.next=Node(i)
    current=current.next
head=dummy.next

def traverse(head_node):
    cur=head_node
    while cur:
        print(cur.val, end=" -> ")
        cur=cur.next
    print("null")

# traverse(head)

def reverse(head_node):
    prev=None
    cur=head_node
    while cur:
        temp=cur.next
        cur.next=prev
        prev=cur
        cur=temp

    return prev

# traverse(reverse(head))


def insert(pos,val,head_node):
    new_node=Node(val)
    cur=head_node
    while cur:
        if cur.val==pos:
            temp=cur.next
            cur.next=new_node
            new_node.next=temp

        cur=cur.next

insert(3,4,head)
traverse(head)
