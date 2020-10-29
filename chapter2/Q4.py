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
    def add_node(self,node):
        if self.root:
            pointer=self.root
            while pointer.next:
                pointer=pointer.next
            pointer.next=node
        else:
            self.root=node
    def show(self):
        pointer=self.root
        while pointer.next:
            print(pointer.data,end=',')
            pointer=pointer.next
        print(pointer.data)
    def partition(self,k):
        p=self.root
        before=LinkedList()
        before_e=None
        after=LinkedList()
        while p!=None:
            next=p.next
            p.next=None
            if p.data<k:
                before.add_node(p)
                before_e=p
            else:
                after.add_node(p)
            p=next
        before_e.next=after.root
        return before

class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

L=LinkedList()
L.add_last(3)
L.add_last(5)
L.add_last(1)
L.add_last(2)
L.add_last(9)
L.add_last(5)
L.add_last(8)
L.show()
L.partition(5)
L.show()