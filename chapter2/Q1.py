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
    def delete_duplicates(self):
        s=set()
        previous=None
        pointer=self.root
        while pointer is not None:
            if pointer.data in s:
                previous.next=pointer.next
            else:
                s.add(pointer.data)
                previous=pointer
            pointer=pointer.next
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
    
linked_list=LinkedList()
linked_list.add_last(1)
linked_list.add_last(2)
linked_list.add_last(1)
linked_list.show()
linked_list.delete_duplicates()
linked_list.show()