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
    def kth_to_last(self,k):
        b=self.root
        a=None
        d=0
        while b!=None:
            d+=1
            if d==k:
                a=self.root
            if d>k:
                a=a.next
            b=b.next
        return a
class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

linked_list=LinkedList()
linked_list.add_last(5)
linked_list.add_last(6)
linked_list.add_last(7)
linked_list.add_last(8)
linked_list.add_last(9)
linked_list.add_last(10)
c=linked_list.kth_to_last(2)
print(c.data)