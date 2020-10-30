class LinkedList:
    def __init__(self,root=None):
        self.root=root
    def add_last(self,data):
        if self.root:
            pointer=self.root
            while pointer.next:
                pointer=pointer.next
            node=Node(data)
            pointer.next=node
        else:
            node=Node(data)
            self.root=node
    def show(self):
        pointer=self.root
        while pointer.next:
            print(pointer.data,end=',')
            pointer=pointer.next
        print(pointer.data)
class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

def func(l1,l2):
    p1=l1.root
    p2=l2.root
    l_s=LinkedList()
    t=0
    while p1!=None and p2!=None:
        x=p1.data+p2.data
        l_s.add_last((x+t)%10)
        if x+t>=10:t=1
        else:t=0
        p1=p1.next
        p2=p2.next
    if p1==None:
        while p2!=None:
            l_s.add_last((p2.data+t)%10)
            if (p2.data+t)>=10:t=1
            else:t=0
            p2=p2.next
    if p2==None:
        while p1!=None:
            l_s.add_last((p1.data+t)%10)
            if (p1.data+t)>=10:t=1
            else:t=0
            p1=p1.next
    return l_s

L1=LinkedList()
L2=LinkedList()
L1.add_last(7)
L1.add_last(1)
L1.add_last(6)
L2.add_last(5)
L2.add_last(9)
L2.add_last(2)
L_S=func(L1,L2)
L_S.show()