class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

def show(node):
    p=node
    while p!=None:
        print(p.data,end=',')
        p=p.next

def intersection(l1,l2):
    p1,p2=l1,l2
    a,b=1,1
    while p1.next!=None:
        a+=1
        p1=p1.next
    while p2.next!=None:
        b+=1
        p2=p2.next
    if p1!=p2:return None
    if a>b:
        c=a-b
        p1,p2=l1,l2
        t=0
        while t<c:
            t+=1
            p1=p1.next
        while p1.next!=None:
            if p1==p2:return p1
            p1=p1.next
            p2=p2.next
    else:
        c=b-a
        p1,p2=l1,l2
        t=0
        while t<c:
            t+=1
            p2=p2.next
        while p1.next!=None:
            if p1==p2:return p1
            p1=p1.next
            p2=p2.nxet

l1=Node(4)
x=Node(3)
l1.next=x
y=Node(2)
x.next=y
z=Node(1)
y.next=z
l2=Node(5)
l2.next=y
show(l1)
print('')
show(l2)
print('')
intersection=intersection(l1,l2)
print(intersection)
print(intersection.data)
